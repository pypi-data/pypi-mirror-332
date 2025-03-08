import os
import pytest
from crimson.code_splitter.extractor import (
    collect_chunks_from_source,
    collect_chunks,
    flat_chunks,
    Code,
)

TEST_CODE_DIR = os.path.join(os.path.dirname(__file__), "env_mock")


def test_collect_chunks_from_source():
    chunks = collect_chunks_from_source(TEST_CODE_DIR)

    assert len(chunks) > 0

    # Check if we have chunks from all files
    file_names = set(
        chunk.path.split(os.path.sep)[-1] for chunk in chunks if chunk.path
    )
    assert "example1.py" in file_names
    assert "example2.py" in file_names
    assert "example3.py" in file_names

    # Check specific chunks
    function_chunks = [chunk for chunk in chunks if chunk.type == "function"]
    class_chunks = [chunk for chunk in chunks if chunk.type == "class"]
    extra_chunks = [chunk for chunk in chunks if chunk.type == "extra"]

    assert len(function_chunks) >= 3  # At least function1, function2, function3
    assert len(class_chunks) >= 3  # At least Class1, Class2, Class3
    assert len(extra_chunks) >= 2  # At least CONSTANT1, CONSTANT2


def test_collect_chunks_from_source_with_includes():
    chunks = collect_chunks_from_source(TEST_CODE_DIR, includes=["example1.py"])

    file_names = set(
        chunk.path.split(os.path.sep)[-1] for chunk in chunks if chunk.path
    )
    assert "example1.py" in file_names
    assert "example2.py" not in file_names
    assert "example3.py" not in file_names


def test_collect_chunks_from_source_with_excludes():
    chunks = collect_chunks_from_source(TEST_CODE_DIR, excludes=["example1.py"])

    file_names = set(
        chunk.path.split(os.path.sep)[-1] for chunk in chunks if chunk.path
    )
    assert "example1.py" not in file_names
    assert "example2.py" in file_names
    assert "example3.py" in file_names


def test_collect_chunks():
    codes = [
        Code(
            content=open(os.path.join(TEST_CODE_DIR, "example1.py")).read(),
            path="example1.py",
        ),
        Code(
            content=open(os.path.join(TEST_CODE_DIR, "example2.py")).read(),
            path="example2.py",
        ),
    ]

    chunks = collect_chunks(codes)

    assert len(chunks) > 0

    file_names = set(chunk.path for chunk in chunks if chunk.path)
    assert "example1.py" in file_names
    assert "example2.py" in file_names
    assert "example3.py" not in file_names


def test_collect_chunks_not_flat():
    codes = [
        Code(
            content=open(os.path.join(TEST_CODE_DIR, "example1.py")).read(),
            path="example1.py",
        ),
    ]

    chunks = collect_chunks(codes, flat=False)

    assert len(chunks) > 0
    class_chunks = [chunk for chunk in chunks if chunk.type == "class"]
    assert len(class_chunks) > 0
    assert hasattr(class_chunks[0], "sub_chunks")
    assert len(class_chunks[0].sub_chunks) > 0


def test_flat_chunks():
    codes = [
        Code(
            content=open(os.path.join(TEST_CODE_DIR, "example1.py")).read(),
            path="example1.py",
        ),
    ]

    non_flat_chunks = collect_chunks(codes, flat=False)
    flat_chunk_list = flat_chunks(non_flat_chunks)

    # Check if the flat list contains more chunks than the non-flat list
    assert len(flat_chunk_list) > len(non_flat_chunks)

    # Check if we can find both class and method chunks in the flat list
    class_chunks = [chunk for chunk in flat_chunk_list if chunk.type == "class"]
    method_chunks = [
        chunk
        for chunk in flat_chunk_list
        if chunk.type == "function" and hasattr(chunk, "parent")
    ]
    assert len(class_chunks) > 0
    assert len(method_chunks) > 0


def test_collect_chunks_from_source_flat_and_not_flat():
    flat_chunks = collect_chunks_from_source(TEST_CODE_DIR, flat=True)
    non_flat_chunks = collect_chunks_from_source(TEST_CODE_DIR, flat=False)

    assert len(flat_chunks) > len(non_flat_chunks)


if __name__ == "__main__":
    pytest.main()
