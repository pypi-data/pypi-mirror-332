from .chunker import chunk_code, CodeChunk, Chunk, InClassChunk
from crimson.file_loader import filter_source, Search_
from typing import List, TypedDict, Optional


class Code(TypedDict):
    """
    TypedDict for representing a code file.
    
    Attributes:
        content (str): The actual code content as a string
        path (Optional[str]): The file path where the code is from, if available
    """

    content: str
    path: Optional[str]


def collect_chunks_from_source(
    source: str,
    includes: List[str] = [],
    excludes: List[str] = [],
    search: Search_.annotation = Search_.default,
    flat: bool = True,
) -> List[Chunk]:
    """
    Collect code chunks from a source directory with filtering options.
    
    This function scans a source directory for Python files, filters them according to 
    include/exclude patterns, parses them into chunks, and returns the resulting chunks.
    
    Args:
        source (str): The source directory to scan
        includes (List[str], optional): List of patterns to include. Defaults to [].
        excludes (List[str], optional): List of patterns to exclude. Defaults to [].
        search (Search_.annotation, optional): Search method to use. Defaults to Search_.default.
        flat (bool, optional): Whether to flatten class chunks. Defaults to True.
        
    Returns:
        List[Chunk]: List of code chunks extracted from the source
    """
    paths = filter_source(
        source=source, includes=includes, excludes=excludes, search=search
    )

    chunks = []

    for path in paths:
        with open(path, "r") as file:
            content = file.read()

        chunks.extend(chunk_code(content, path))

    chunks = flat_chunks(chunks=chunks, turn_on=flat)

    return chunks


def collect_chunks(codes: List[Code], flat: bool = True) -> List[CodeChunk]:
    """
    Collect code chunks from a list of Code objects.
    
    This function parses the content of each Code object into chunks and returns them.
    
    Args:
        codes (List[Code]): List of Code objects containing content to parse
        flat (bool, optional): Whether to flatten class chunks. Defaults to True.
        
    Returns:
        List[CodeChunk]: List of code chunks extracted from the codes
    """
    chunks = []
    for code in codes:
        content = code["content"]
        path = code["path"]
        chunks.extend(chunk_code(content, path))

    if flat is True:
        chunks = flat_chunks(chunks=chunks, turn_on=flat)
    return chunks


def flat_chunks(chunks: List[CodeChunk], turn_on: bool = True) -> List[Chunk]:
    """
    Flatten a nested structure of chunks.
    
    This function takes a list of CodeChunk objects and flattens their sub-chunks
    into a single-level list if turn_on is True.
    
    Args:
        chunks (List[CodeChunk]): List of code chunks to flatten
        turn_on (bool, optional): Whether to perform flattening. Defaults to True.
        
    Returns:
        List[Chunk]: Flattened list of chunks if turn_on is True, original list otherwise
    """
    if turn_on is False:
        return chunks

    new_chunks = []

    for chunk in chunks:
        new_chunks.append(chunk)
        if chunk.sub_chunks is not None:
            new_chunks.extend(chunk.sub_chunks)

    return new_chunks


def get_source_info_as_string(chunk: Chunk) -> str:
    """
    Get formatted source information from a chunk.
    
    This function extracts and formats metadata about a chunk's source location
    and type into a list of strings.
    
    Args:
        chunk (Chunk): The chunk to extract source information from
        
    Returns:
        str: A formatted string containing the chunk's source information
    """
    source = []
    if chunk.path is not None:
        source.append(f"path: {chunk.path}")

    source.append(f"start line: {chunk.start_line}")

    if isinstance(chunk, CodeChunk):
        source.append(f"{chunk.type}: {chunk.name}")

    if isinstance(chunk, InClassChunk):
        source.append(f"class: {chunk.parent}")
        source.append(f"{chunk.type}: {chunk.name}")

    return source
