"""
Tests for the JSX export functionality of the recursivist package.

This module contains comprehensive tests for the JSX export functionality:
- JSX structure generation with various directory structures
- Handling of statistics (LOC, size, modification time)
- Path display options
- Maximum depth scenarios
- Error handling in JSX exports
"""

import os
import re
import tempfile
from unittest.mock import patch

import pytest

from recursivist.jsx_export import generate_jsx_component


@pytest.fixture
def simple_structure():
    """Create a simple directory structure with files only."""
    return {
        "_files": ["file1.txt", "file2.py", "file3.md"],
    }


@pytest.fixture
def empty_structure():
    """Create an empty directory structure."""
    return {}


@pytest.fixture
def nested_structure():
    """Create a nested directory structure with multiple levels."""
    return {
        "_files": ["root_file1.txt", "root_file2.py"],
        "subdir1": {
            "_files": ["subdir1_file1.txt", "subdir1_file2.js"],
        },
        "subdir2": {
            "_files": ["subdir2_file1.md"],
            "nested": {
                "_files": ["nested_file1.json"],
                "deep": {
                    "_files": ["deep_file1.py", "deep_file2.txt"],
                },
            },
        },
    }


@pytest.fixture
def structure_with_stats():
    """Create a directory structure with statistics."""
    return {
        "_loc": 100,
        "_size": 1024,
        "_mtime": 1609459200,
        "_files": [
            ("file1.txt", "/path/to/file1.txt", 50, 512, 1609459200),
            ("file2.py", "/path/to/file2.py", 30, 256, 1609459000),
        ],
        "subdir": {
            "_loc": 20,
            "_size": 256,
            "_mtime": 1609450000,
            "_files": [
                ("subfile.md", "/path/to/subdir/subfile.md", 20, 256, 1609450000),
            ],
        },
    }


@pytest.fixture
def max_depth_structure():
    """Create a directory structure with max depth reached."""
    return {
        "_files": ["root_file.txt"],
        "subdir": {
            "_max_depth_reached": True,
        },
    }


def test_empty_structure(empty_structure, tmp_path):
    """Test JSX export with an empty directory structure."""
    output_path = os.path.join(tmp_path, "empty.jsx")

    # Generate JSX component
    generate_jsx_component(empty_structure, "empty_dir", output_path)

    # Verify file was created
    assert os.path.exists(output_path)

    # Read the content
    with open(output_path, "r", encoding="utf-8") as f:
        jsx_content = f.read()

    # Check basic structure
    assert "import React" in jsx_content
    assert "empty_dir" in jsx_content
    assert "DirectoryViewer" in jsx_content
    assert "export default DirectoryViewer" in jsx_content

    # Empty structure should not have any DirectoryItem or FileItem elements
    # beyond the root item itself
    file_items = re.findall(r"<FileItem\s", jsx_content)
    assert len(file_items) == 0


def test_simple_structure(simple_structure, tmp_path):
    """Test JSX export with a simple structure with only files, no nested directories."""
    output_path = os.path.join(tmp_path, "simple.jsx")

    # Generate JSX component
    generate_jsx_component(simple_structure, "simple_dir", output_path)

    # Verify file was created
    assert os.path.exists(output_path)

    # Read the content
    with open(output_path, "r", encoding="utf-8") as f:
        jsx_content = f.read()

    # Check for each file
    assert "<FileItem " in jsx_content
    assert 'name="file1.txt"' in jsx_content
    assert 'name="file2.py"' in jsx_content
    assert 'name="file3.md"' in jsx_content

    # Count file items
    file_items = re.findall(r"<FileItem\s", jsx_content)
    assert len(file_items) == 3

    # No subdirectories beyond root
    directory_items = re.findall(r"<DirectoryItem\s", jsx_content)
    assert len(directory_items) == 1  # Just the root
    assert 'name="simple_dir"' in jsx_content


def test_nested_structure(nested_structure, tmp_path):
    """Test JSX export with a deeply nested structure with multiple levels."""
    output_path = os.path.join(tmp_path, "nested.jsx")

    # Generate JSX component
    generate_jsx_component(nested_structure, "nested_dir", output_path)

    # Verify file was created
    assert os.path.exists(output_path)

    # Read the content
    with open(output_path, "r", encoding="utf-8") as f:
        jsx_content = f.read()

    # Check for directories
    assert 'name="subdir1"' in jsx_content
    assert 'name="subdir2"' in jsx_content
    assert 'name="nested"' in jsx_content
    assert 'name="deep"' in jsx_content

    # Check for files at different levels
    assert 'name="root_file1.txt"' in jsx_content
    assert 'name="subdir1_file1.txt"' in jsx_content
    assert 'name="nested_file1.json"' in jsx_content
    assert 'name="deep_file1.py"' in jsx_content

    # Count directory and file items
    directory_items = re.findall(r"<DirectoryItem\s", jsx_content)
    assert len(directory_items) == 5  # Root + 4 subdirectories
    file_items = re.findall(r"<FileItem\s", jsx_content)
    assert len(file_items) == 7  # Total 7 files across all levels


def test_structure_with_stats(structure_with_stats, tmp_path):
    """Test JSX export with statistics enabled."""
    output_path = os.path.join(tmp_path, "stats.jsx")

    # Generate JSX component with statistics enabled
    generate_jsx_component(
        structure_with_stats,
        "stats_dir",
        output_path,
        sort_by_loc=True,
        sort_by_size=True,
        sort_by_mtime=True,
    )

    # Verify file was created
    assert os.path.exists(output_path)

    # Read the content
    with open(output_path, "r", encoding="utf-8") as f:
        jsx_content = f.read()

    # Check for stat props in root directory
    assert "locCount={100}" in jsx_content
    assert "sizeCount={1024}" in jsx_content
    assert "mtimeCount={1609459200}" in jsx_content

    # Check for stat props in files
    assert "locCount={50}" in jsx_content
    assert "sizeCount={512}" in jsx_content
    assert "mtimeCount={1609459200}" in jsx_content
    assert "mtimeFormatted=" in jsx_content
    assert "sizeFormatted=" in jsx_content

    # Check for stat props in subdirectory
    assert "locCount={20}" in jsx_content

    # Check for stat-related functions and state
    assert "const [showLoc, setShowLoc] = useState(true);" in jsx_content
    assert "const [showSize, setShowSize] = useState(true);" in jsx_content
    assert "const [showMtime, setShowMtime] = useState(true);" in jsx_content
    assert "toggleLocDisplay" in jsx_content
    assert "toggleSizeDisplay" in jsx_content
    assert "toggleMtimeDisplay" in jsx_content
    assert "format_size" in jsx_content
    assert "format_timestamp" in jsx_content


def test_structure_with_full_paths(structure_with_stats, tmp_path):
    """Test JSX export with full paths enabled."""
    output_path = os.path.join(tmp_path, "full_paths.jsx")

    # Generate JSX component with full paths enabled
    generate_jsx_component(
        structure_with_stats, "path_dir", output_path, show_full_path=True
    )

    # Verify file was created
    assert os.path.exists(output_path)

    # Read the content
    with open(output_path, "r", encoding="utf-8") as f:
        jsx_content = f.read()

    # Check for full paths in file items
    assert 'displayPath="/path/to/file1.txt"' in jsx_content
    assert 'displayPath="/path/to/file2.py"' in jsx_content
    assert 'displayPath="/path/to/subdir/subfile.md"' in jsx_content

    # Check path array format
    assert (
        'path={["path_dir","file1.txt"]}' in jsx_content
        or 'path={["path_dir", "file1.txt"]}' in jsx_content
    )


def test_max_depth_structure(max_depth_structure, tmp_path):
    """Test JSX export with max depth reached scenarios."""
    output_path = os.path.join(tmp_path, "max_depth.jsx")

    # Generate JSX component
    generate_jsx_component(max_depth_structure, "max_depth_dir", output_path)

    # Verify file was created
    assert os.path.exists(output_path)

    # Read the content
    with open(output_path, "r", encoding="utf-8") as f:
        jsx_content = f.read()

    # Check for max depth indicators
    assert "(max depth reached)" in jsx_content
    assert "div className=" in jsx_content and "max-depth" in jsx_content


def test_various_sorting_options(structure_with_stats, tmp_path):
    """Test JSX export with different combinations of sorting options."""
    test_combinations = [
        (True, False, False),  # Only LOC
        (False, True, False),  # Only Size
        (False, False, True),  # Only Mtime
        (True, True, False),  # LOC and Size
        (True, False, True),  # LOC and Mtime
        (False, True, True),  # Size and Mtime
    ]

    for sort_by_loc, sort_by_size, sort_by_mtime in test_combinations:
        output_path = os.path.join(
            tmp_path, f"sort_{sort_by_loc}_{sort_by_size}_{sort_by_mtime}.jsx"
        )

        # Generate JSX component with specific sorting options
        generate_jsx_component(
            structure_with_stats,
            "sort_dir",
            output_path,
            sort_by_loc=sort_by_loc,
            sort_by_size=sort_by_size,
            sort_by_mtime=sort_by_mtime,
        )

        # Verify file was created
        assert os.path.exists(output_path)

        # Read the content
        with open(output_path, "r", encoding="utf-8") as f:
            jsx_content = f.read()

        # Check for state variables based on sorting options
        if sort_by_loc:
            assert "const [showLoc, setShowLoc] = useState(true);" in jsx_content
        else:
            assert "const [showLoc, setShowLoc] = useState(true);" not in jsx_content

        if sort_by_size:
            assert "const [showSize, setShowSize] = useState(true);" in jsx_content
        else:
            assert "const [showSize, setShowSize] = useState(true);" not in jsx_content

        if sort_by_mtime:
            assert "const [showMtime, setShowMtime] = useState(true);" in jsx_content
        else:
            assert (
                "const [showMtime, setShowMtime] = useState(true);" not in jsx_content
            )


def test_error_handling(structure_with_stats):
    """Test error handling in JSX export."""
    # Create a non-writable directory
    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, "error.jsx")

        # Create the file first so we can make it read-only
        with open(output_path, "w") as f:
            f.write("")

        # Make the file read-only
        os.chmod(output_path, 0o444)

        # Mock logger to check for error logging
        with patch("recursivist.jsx_export.logger") as mock_logger:
            # Generate JSX component which should fail due to permission error
            with pytest.raises(Exception):
                generate_jsx_component(structure_with_stats, "error_dir", output_path)

            # Verify error was logged
            mock_logger.error.assert_called_once()
            # Check that the error message mentions the problem
            assert (
                "Error exporting to React component"
                in mock_logger.error.call_args[0][0]
            )


def test_special_characters_in_names(tmp_path):
    """Test JSX export with special characters in file and directory names."""
    special_structure = {
        "_files": ["normal.txt", "special&.txt", 'quotes".txt', "tags<>.txt"],
        "special dir & more": {
            "_files": ["file in special dir.txt"],
        },
    }

    output_path = os.path.join(tmp_path, "special_chars.jsx")

    # Generate JSX component
    generate_jsx_component(special_structure, "special_chars_dir", output_path)

    # Verify file was created
    assert os.path.exists(output_path)

    # Read the content
    with open(output_path, "r", encoding="utf-8") as f:
        jsx_content = f.read()

    # Check that special characters are properly escaped in JSX
    assert (
        'name="special&amp;.txt"' in jsx_content
        or 'name="special&#x26;.txt"' in jsx_content
    )
    assert (
        'name="quotes&quot;.txt"' in jsx_content
        or 'name="quotes&#x22;.txt"' in jsx_content
    )
    assert (
        'name="tags&lt;&gt;.txt"' in jsx_content
        or 'name="tags&#x3C;&#x3E;.txt"' in jsx_content
    )
    assert (
        'name="special dir &amp; more"' in jsx_content
        or 'name="special dir &#x26; more"' in jsx_content
    )
