from typing import List, Optional, Literal
import ast


class Chunk:
    """
    Base class for representing a chunk of code.
    
    A chunk is a segment of code with metadata including type, name, line numbers, and content.
    
    Attributes:
        type (Literal["class", "function", "extra"]): The type of code chunk
        name (str): The name identifier of the chunk
        start_line (int): The starting line number in the source
        end_line (int): The ending line number in the source
        code (str): The actual code content
        path (Optional[str]): File path of the source, if available
    """
    def __init__(
        self,
        type: Literal["class", "function", "extra"],
        name: str,
        start_line: int,
        end_line: int,
        code: str,
        path: Optional[str] = None,
    ):
        self.type = type
        self.name = name
        self.start_line = start_line
        self.end_line = end_line
        self.code = code
        self.path = path

    def __repr__(self):
        return f"{self.type.capitalize()} '{self.name}': lines {self.start_line}-{self.end_line} \ncode: \n{self.code}"


class InClassChunk(Chunk):
    """
    Represents a code chunk that exists within a class definition.
    
    Extends the Chunk class with additional parent class information.
    
    Attributes:
        parent (str): The name of the parent class containing this chunk
        + all attributes inherited from Chunk
    """
    def __init__(
        self,
        type: Literal["class", "function", "extra"],
        name: str,
        start_line: int,
        end_line: int,
        code: str,
        parent: str,
        path: Optional[str] = None,
    ):
        super().__init__(type, name, start_line, end_line, code, path)
        self.parent = parent


class CodeChunk(Chunk):
    """
    Represents a top-level code chunk that may contain sub-chunks.
    
    A CodeChunk can be a class definition with methods, a function definition,
    or other standalone code.
    
    Attributes:
        sub_chunks (List[InClassChunk]): List of chunks contained within this chunk
        + all attributes inherited from Chunk
    """
    def __init__(
        self,
        type: Literal["class", "function", "extra"],
        name: str,
        start_line: int,
        end_line: int,
        code: str,
        path: Optional[str] = None,
        sub_chunks: Optional[List[InClassChunk]] = None,
    ):
        super().__init__(type, name, start_line, end_line, code, path)
        self.sub_chunks: List[InClassChunk] = sub_chunks or []


def chunk_code(source_code: str, path: str = None) -> List[CodeChunk]:
    """
    Parse Python source code and break it into code chunks.
    
    This function analyzes Python source code using the AST parser and divides it
    into logical chunks representing classes, functions, and other code segments.
    
    Args:
        source_code (str): The Python source code to be chunked
        path (str, optional): The file path of the source code
        
    Returns:
        List[CodeChunk]: A list of CodeChunk objects representing the parsed source
    """
    tree = ast.parse(source_code)
    lines = source_code.splitlines()
    chunks: List[CodeChunk] = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            class_chunk = CodeChunk(
                type="class",
                name=node.name,
                start_line=node.lineno,
                end_line=node.end_lineno,
                code=code,
                path=path,
                sub_chunks=secondary_chunking(node, lines, path),
            )
            chunks.append(class_chunk)
        elif isinstance(node, ast.FunctionDef):
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            chunks.append(
                CodeChunk(
                    type="function",
                    name=node.name,
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                )
            )
        else:
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            chunks.append(
                CodeChunk(
                    type="extra",
                    name="extra",
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                )
            )

    return chunks


def secondary_chunking(
    class_node: ast.ClassDef, lines: List[str], path: Optional[str] = None
) -> List[InClassChunk]:
    """
    Parse the contents of a class definition into sub-chunks.
    
    This function processes a class AST node and creates chunks for its methods
    and other contents.
    
    Args:
        class_node (ast.ClassDef): AST node representing a class definition
        lines (List[str]): Source code lines
        path (Optional[str], optional): The file path of the source code
        
    Returns:
        List[InClassChunk]: A list of InClassChunk objects representing the class contents
    """

    sub_chunks: List[InClassChunk] = []

    # 클래스 선언부와 docstring을 첫 번째 청크로 만듭니다
    class_start = class_node.lineno
    class_end = class_node.body[0].lineno - 1 if class_node.body else class_node.lineno
    class_code = get_code_segment(lines, class_start, class_end)

    # docstring이 있는지 확인합니다
    docstring = ast.get_docstring(class_node)
    if docstring:
        first_stmt = class_node.body[0]
        if isinstance(first_stmt, ast.Expr) and isinstance(first_stmt.value, ast.Constant) and isinstance(first_stmt.value.value, str):
            class_end = first_stmt.end_lineno

    class_code = get_code_segment(lines, class_start, class_end)
    sub_chunks.append(
        InClassChunk(
            type="class",
            name=class_node.name,
            start_line=class_start,
            end_line=class_end,
            code=class_code,
            path=path,
            parent=class_node.name,
        )
    )

    for node in class_node.body:
        if isinstance(node, ast.FunctionDef):
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            sub_chunks.append(
                InClassChunk(
                    type="function",
                    name=node.name,
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                    parent=class_node.name,
                )
            )
        elif not (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
            and node.lineno == class_node.body[0].lineno
        ):
            # docstring이 아닌 경우에만 추가합니다
            code = get_code_segment(lines, node.lineno, node.end_lineno)
            sub_chunks.append(
                InClassChunk(
                    type="extra",
                    name="extra",
                    start_line=node.lineno,
                    end_line=node.end_lineno,
                    code=code,
                    path=path,
                    parent=class_node.name,
                )
            )

    return sub_chunks


def get_code_segment(lines: List[str], start: int, end: int) -> str:
    """
    Extract a segment of code from a list of source lines.
    
    Args:
        lines (List[str]): List of source code lines
        start (int): Starting line number (1-indexed)
        end (int): Ending line number (1-indexed)
        
    Returns:
        str: The extracted code segment as a string
    """

    return "\n".join(lines[start - 1 : end])
