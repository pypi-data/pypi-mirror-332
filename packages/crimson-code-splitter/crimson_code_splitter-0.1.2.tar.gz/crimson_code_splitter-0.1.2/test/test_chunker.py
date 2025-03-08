import pytest
from crimson.code_splitter.chunker import Chunk, CodeChunk, InClassChunk, chunk_code


def test_chunk_initialization():
    chunk = Chunk(
        type="function",
        name="test_func",
        start_line=1,
        end_line=5,
        code="def test_func():\n    pass",
    )
    assert chunk.type == "function"
    assert chunk.name == "test_func"
    assert chunk.start_line == 1
    assert chunk.end_line == 5
    assert chunk.code == "def test_func():\n    pass"
    assert chunk.path is None


def test_in_class_chunk_initialization():
    in_class_chunk = InClassChunk(
        type="function",
        name="method",
        start_line=2,
        end_line=4,
        code="def method(self):\n    pass",
        parent="TestClass",
    )
    assert in_class_chunk.type == "function"
    assert in_class_chunk.name == "method"
    assert in_class_chunk.parent == "TestClass"


def test_code_chunk_initialization():
    sub_chunks = [
        InClassChunk(
            type="function",
            name="method1",
            start_line=2,
            end_line=3,
            code="def method1(self):\n    pass",
            parent="TestClass",
        ),
        InClassChunk(
            type="function",
            name="method2",
            start_line=4,
            end_line=5,
            code="def method2(self):\n    pass",
            parent="TestClass",
        ),
    ]
    code_chunk = CodeChunk(
        type="class",
        name="TestClass",
        start_line=1,
        end_line=5,
        code="class TestClass:\n    pass",
        sub_chunks=sub_chunks,
    )
    assert code_chunk.type == "class"
    assert code_chunk.name == "TestClass"
    assert len(code_chunk.sub_chunks) == 2


def test_chunk_code():
    source_code = """
class TestClass:
    def method1(self):
        pass

    def method2(self):
        pass

def standalone_function():
    pass

CONSTANT = 42
"""
    chunks = chunk_code(source_code)

    assert len(chunks) == 3
    assert chunks[0].type == "class"
    assert chunks[0].name == "TestClass"
    assert len(chunks[0].sub_chunks) == 3  # Class definition, method1, method2
    assert chunks[1].type == "function"
    assert chunks[1].name == "standalone_function"
    assert chunks[2].type == "extra"
    assert chunks[2].name == "extra"


def test_chunk_code_with_docstrings():
    source_code = '''
class DocStringClass:
    """This is a class docstring."""

    def method_with_docstring(self):
        """This is a method docstring."""
        pass

def function_with_docstring():
    """This is a function docstring."""
    pass
'''
    chunks = chunk_code(source_code)

    assert len(chunks) == 2
    assert chunks[0].type == "class"
    assert chunks[0].name == "DocStringClass"
    assert len(chunks[0].sub_chunks) == 2  # Class definition (with docstring), method
    assert "This is a class docstring." in chunks[0].sub_chunks[0].code
    assert "This is a method docstring." in chunks[0].sub_chunks[1].code
    assert chunks[1].type == "function"
    assert chunks[1].name == "function_with_docstring"
    assert "This is a function docstring." in chunks[1].code


if __name__ == "__main__":
    pytest.main()
