"""
Core functionality for the Recursivist directory visualization tool.

This module provides the fundamental components for building, filtering, displaying, and exporting directory structures. It handles directory traversal, pattern matching, color coding, and tree construction for visual representation.

Key features include:
- Directory structure parsing and representation
- Flexible pattern-based filtering (glob/regex)
- Customizable depth limits and path displays
- Color-coding by file extension
- Support for ignore files (like .gitignore)
- Tree visualization with rich formatting
"""

import colorsys
import fnmatch
import hashlib
import logging
import os
import re
from typing import Any, Dict, List, Optional, Pattern, Set, Tuple, Union, cast

from rich.console import Console
from rich.text import Text
from rich.tree import Tree

logger = logging.getLogger(__name__)


def export_structure(
    structure: Dict,
    root_dir: str,
    format_type: str,
    output_path: str,
    show_full_path: bool = False,
    sort_by_loc: bool = False,
) -> None:
    """Export the directory structure to various formats.

    Maps the requested format to the appropriate export method using DirectoryExporter. Handles txt, json, html, md, and jsx formats with consistent styling.

    Args:
        structure: Directory structure dictionary
        root_dir: Root directory name
        format_type: Export format ('txt', 'json', 'html', 'md', 'jsx')
        output_path: Path where the export file will be saved
        show_full_path: Whether to show full paths instead of just filenames
        sort_by_loc: Whether to include lines of code counts in the export

    Raises:
        ValueError: If the format_type is not supported
    """
    from recursivist.exports import DirectoryExporter

    exporter = DirectoryExporter(
        structure,
        os.path.basename(root_dir),
        root_dir if show_full_path else None,
        sort_by_loc,
    )
    format_map = {
        "txt": exporter.to_txt,
        "json": exporter.to_json,
        "html": exporter.to_html,
        "md": exporter.to_markdown,
        "jsx": exporter.to_jsx,
    }
    if format_type.lower() not in format_map:
        raise ValueError(f"Unsupported format: {format_type}")
    export_func = format_map[format_type.lower()]
    export_func(output_path)


def parse_ignore_file(ignore_file_path: str) -> List[str]:
    """Parse an ignore file (like .gitignore) and return patterns.

    Reads an ignore file and extracts patterns for excluding files and directories. Handles comments and trailing slashes in directories.

    Args:
        ignore_file_path: Path to the ignore file

    Returns:
        List of patterns to ignore
    """
    if not os.path.exists(ignore_file_path):
        return []
    patterns = []
    with open(ignore_file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                if line.endswith("/"):
                    line = line[:-1]
                patterns.append(line)
    return patterns


def compile_regex_patterns(
    patterns: List[str], is_regex: bool = False
) -> List[Union[str, Pattern[str]]]:
    """Compile regex patterns if needed.

    Converts string patterns to compiled regex patterns when is_regex is True. For invalid regex patterns, logs a warning and keeps them as strings.

    Args:
        patterns: List of patterns to compile
        is_regex: Whether the patterns should be treated as regex or glob patterns

    Returns:
        List of patterns (either strings for glob patterns or compiled regex patterns)
    """
    if not is_regex:
        return cast(List[Union[str, Pattern[str]]], patterns)
    compiled_patterns: List[Union[str, Pattern[str]]] = []
    for pattern in patterns:
        try:
            compiled_patterns.append(re.compile(pattern))
        except re.error as e:
            logger.warning(f"Invalid regex pattern '{pattern}': {e}")
            compiled_patterns.append(pattern)
    return compiled_patterns


def should_exclude(
    path: str,
    ignore_context: Dict,
    exclude_extensions: Optional[Set[str]] = None,
    exclude_patterns: Optional[List[Union[str, Pattern[str]]]] = None,
    include_patterns: Optional[List[Union[str, Pattern[str]]]] = None,
) -> bool:
    """Check if a path should be excluded based on ignore patterns, extensions, and regex patterns.

    Decision hierarchy:
    1. If include_patterns match, INCLUDE the path (overrides all exclusions)
    2. If exclude_patterns match, EXCLUDE the path
    3. If file extension is in exclude_extensions, EXCLUDE the path
    4. If gitignore-style patterns match, use their rules

    Args:
        path: Path to check
        ignore_context: Dictionary with 'patterns' and 'current_dir' keys
        exclude_extensions: Set of file extensions to exclude
        exclude_patterns: List of regex patterns to exclude
        include_patterns: List of regex patterns to include (overrides exclusions)

    Returns:
        True if path should be excluded
    """
    patterns = ignore_context.get("patterns", [])
    current_dir = ignore_context.get("current_dir", os.path.dirname(path))
    if exclude_extensions and os.path.isfile(path):
        _, ext = os.path.splitext(path)
        if ext.lower() in exclude_extensions:
            return True
    rel_path = os.path.relpath(path, current_dir)
    if os.name == "nt":
        rel_path = rel_path.replace("\\", "/")
    basename = os.path.basename(path)
    if include_patterns:
        included = False
        for pattern in include_patterns:
            if isinstance(pattern, Pattern):
                if pattern.search(rel_path) or pattern.search(basename):
                    included = True
                    break
            else:
                if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(
                    basename, pattern
                ):
                    included = True
                    break
        if included:
            return False
        else:
            return True
    if exclude_patterns:
        for pattern in exclude_patterns:
            if isinstance(pattern, Pattern):
                if pattern.search(rel_path) or pattern.search(basename):
                    return True
            else:
                if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(
                    basename, pattern
                ):
                    return True
    if not patterns:
        return False
    for pattern in patterns:
        if isinstance(pattern, str):
            if pattern.startswith("!"):
                if fnmatch.fnmatch(rel_path, pattern[1:]):
                    return False
            elif fnmatch.fnmatch(rel_path, pattern):
                return True
    return False


def generate_color_for_extension(extension: str) -> str:
    """Generate a consistent color for a given file extension.

    Uses a hash function to derive a consistent color for each extension, ensuring the same extension always gets the same color within a session. Colors are in the HSV color space with fixed saturation and value but varying hue based on the hash.

    Args:
        extension: File extension (with or without leading dot)

    Returns:
        Hex color code
    """
    if not extension:
        return "#FFFFFF"
    hash_value = int(hashlib.md5(extension.encode()).hexdigest(), 16)
    hue = hash_value % 360 / 360.0
    saturation = 0.7
    value = 0.95
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
    )


def get_directory_structure(
    root_dir: str,
    exclude_dirs: Optional[List[str]] = None,
    ignore_file: Optional[str] = None,
    exclude_extensions: Optional[Set[str]] = None,
    parent_ignore_patterns: Optional[List[str]] = None,
    exclude_patterns: Optional[List[Union[str, Pattern[str]]]] = None,
    include_patterns: Optional[List[Union[str, Pattern[str]]]] = None,
    max_depth: int = 0,
    current_depth: int = 0,
    current_path: str = "",
    show_full_path: bool = False,
    sort_by_loc: bool = False,
) -> Tuple[Dict[str, Any], Set[str]]:
    """Build a nested dictionary representing the directory structure.

    Recursively traverses the file system starting at root_dir, applying filters and building a structured representation. When sort_by_loc is True, calculates lines of code for files and directories.

    Args:
        root_dir: Root directory path to start from
        exclude_dirs: List of directory names to exclude
        ignore_file: Name of ignore file (like .gitignore)
        exclude_extensions: Set of file extensions to exclude
        parent_ignore_patterns: Patterns from parent directories
        exclude_patterns: List of regex patterns to exclude
        include_patterns: List of regex patterns to include (overrides exclusions)
        max_depth: Maximum depth to traverse (0 for unlimited)
        current_depth: Current depth in the directory tree
        current_path: Current path for full path display
        show_full_path: Whether to show full paths instead of just filenames
        sort_by_loc: Whether to calculate and display lines of code counts

    Returns:
        Tuple of (structure dictionary, set of extensions found)
    """
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_extensions is None:
        exclude_extensions = set()
    if exclude_patterns is None:
        exclude_patterns = []
    if include_patterns is None:
        include_patterns = []
    ignore_patterns = parent_ignore_patterns.copy() if parent_ignore_patterns else []
    if ignore_file and os.path.exists(os.path.join(root_dir, ignore_file)):
        current_ignore_patterns = parse_ignore_file(os.path.join(root_dir, ignore_file))
        ignore_patterns.extend(current_ignore_patterns)
    ignore_context = {"patterns": ignore_patterns, "current_dir": root_dir}
    structure: Dict[str, Any] = {}
    extensions_set: Set[str] = set()
    total_loc = 0
    if max_depth > 0 and current_depth >= max_depth:
        return {"_max_depth_reached": True}, extensions_set
    try:
        items = os.listdir(root_dir)
    except PermissionError:
        logger.warning(f"Permission denied: {root_dir}")
        return structure, extensions_set
    except Exception as e:
        logger.error(f"Error reading directory {root_dir}: {e}")
        return structure, extensions_set
    for item in items:
        item_path = os.path.join(root_dir, item)
        if item in exclude_dirs or should_exclude(
            item_path,
            ignore_context,
            exclude_extensions,
            exclude_patterns,
            include_patterns,
        ):
            continue
        if not os.path.isdir(item_path):
            _, ext = os.path.splitext(item)
            if ext.lower() not in exclude_extensions:
                if "_files" not in structure:
                    structure["_files"] = []
                file_loc = 0
                if sort_by_loc:
                    file_loc = count_lines_of_code(item_path)
                    total_loc += file_loc
                if show_full_path:
                    abs_path = os.path.abspath(item_path)
                    abs_path = abs_path.replace(os.sep, "/")
                    if sort_by_loc:
                        structure["_files"].append((item, abs_path, file_loc))
                    else:
                        structure["_files"].append((item, abs_path))
                else:
                    if sort_by_loc:
                        structure["_files"].append((item, item, file_loc))
                    else:
                        structure["_files"].append(item)
                if ext:
                    extensions_set.add(ext.lower())
    for item in items:
        item_path = os.path.join(root_dir, item)
        if item in exclude_dirs or should_exclude(
            item_path,
            ignore_context,
            exclude_extensions,
            exclude_patterns,
            include_patterns,
        ):
            continue
        if os.path.isdir(item_path):
            next_path = os.path.join(current_path, item) if current_path else item
            substructure, sub_extensions = get_directory_structure(
                item_path,
                exclude_dirs,
                ignore_file,
                exclude_extensions,
                ignore_patterns,
                exclude_patterns,
                include_patterns,
                max_depth,
                current_depth + 1,
                next_path,
                show_full_path,
                sort_by_loc,
            )
            structure[item] = substructure
            extensions_set.update(sub_extensions)
            if sort_by_loc and "_loc" in substructure:
                total_loc += substructure["_loc"]
    if sort_by_loc:
        structure["_loc"] = total_loc
    return structure, extensions_set


def sort_files_by_type(
    files: List[Union[str, Tuple[str, str], Tuple[str, str, int]]],
    sort_by_loc: bool = False,
) -> List[Union[str, Tuple[str, str], Tuple[str, str, int]]]:
    """Sort files by extension and then by name, or by LOC if requested.

    Handles mixed input of both strings and tuples, ensuring correct sorting in either case. When sort_by_loc is True, files are sorted by lines of code (descending).

    Args:
        files: List of filenames or tuples to sort
        sort_by_loc: Whether to sort by lines of code instead of file type

    Returns:
        Sorted list of filenames or tuples
    """
    if not files:
        return []
    has_loc = any(isinstance(item, tuple) and len(item) > 2 for item in files)
    if sort_by_loc and has_loc:
        return sorted(
            files, key=lambda f: (-(f[2] if isinstance(f, tuple) and len(f) > 2 else 0))
        )
    all_tuples = all(isinstance(item, tuple) for item in files)
    all_strings = all(isinstance(item, str) for item in files)
    if all_strings:
        files_as_strings = cast(List[str], files)
        return cast(
            List[Union[str, Tuple[str, str], Tuple[str, str, int]]],
            sorted(
                files_as_strings,
                key=lambda f: (os.path.splitext(f)[1].lower(), f.lower()),
            ),
        )
    elif all_tuples:
        return sorted(
            files,
            key=lambda t: (os.path.splitext(t[0])[1].lower(), t[0].lower()),
        )
    else:
        str_items: List[str] = []
        tuple_items: List[Union[Tuple[str, str], Tuple[str, str, int]]] = []
        for item in files:
            if isinstance(item, tuple):
                tuple_items.append(item)
            else:
                str_items.append(cast(str, item))
        sorted_strings = sorted(
            str_items, key=lambda f: (os.path.splitext(f)[1].lower(), f.lower())
        )
        sorted_tuples = sorted(
            tuple_items, key=lambda t: (os.path.splitext(t[0])[1].lower(), t[0].lower())
        )
        result: List[Union[str, Tuple[str, str], Tuple[str, str, int]]] = []
        result.extend(sorted_strings)
        result.extend(sorted_tuples)
        return result


def build_tree(
    structure: Dict,
    tree: Tree,
    color_map: Dict[str, str],
    parent_name: str = "Root",
    show_full_path: bool = False,
    sort_by_loc: bool = False,
) -> None:
    """Build the tree structure with colored file names.

    Recursively builds a rich.Tree representation of the directory structure with files color-coded by extension. When sort_by_loc is True, displays lines of code counts for files and directories.

    Args:
        structure: Dictionary representation of the directory structure
        tree: Rich Tree object to build upon
        color_map: Mapping of file extensions to colors
        parent_name: Name of the parent directory
        show_full_path: Whether to show full paths instead of just filenames
        sort_by_loc: Whether to display lines of code counts
    """
    for folder, content in sorted(structure.items()):
        if folder == "_files":
            for file_item in sort_files_by_type(content, sort_by_loc):
                if sort_by_loc and isinstance(file_item, tuple) and len(file_item) > 2:
                    file_name, display_path, loc = file_item
                    ext = os.path.splitext(file_name)[1].lower()
                    color = color_map.get(ext, "#FFFFFF")
                    colored_text = Text(f"📄 {display_path} ({loc} lines)", style=color)
                    tree.add(colored_text)
                elif show_full_path and isinstance(file_item, tuple):
                    if len(file_item) > 2:
                        file_name, full_path, _ = file_item
                    else:
                        file_name, full_path = file_item
                    ext = os.path.splitext(file_name)[1].lower()
                    color = color_map.get(ext, "#FFFFFF")
                    colored_text = Text(f"📄 {full_path}", style=color)
                    tree.add(colored_text)
                else:
                    if isinstance(file_item, tuple):
                        if len(file_item) > 2:
                            file_name, _, _ = file_item
                        else:
                            file_name, _ = file_item
                    else:
                        file_name = cast(str, file_item)
                    ext = os.path.splitext(file_name)[1].lower()
                    color = color_map.get(ext, "#FFFFFF")
                    colored_text = Text(f"📄 {file_name}", style=color)
                    tree.add(colored_text)
        elif folder == "_loc" or folder == "_max_depth_reached":
            pass
        else:
            if sort_by_loc and isinstance(content, dict) and "_loc" in content:
                folder_loc = content["_loc"]
                subtree = tree.add(f"📁 {folder} ({folder_loc} lines)")
            else:
                subtree = tree.add(f"📁 {folder}")
            if isinstance(content, dict) and content.get("_max_depth_reached"):
                subtree.add(Text("⋯ (max depth reached)", style="dim"))
            else:
                build_tree(
                    content, subtree, color_map, folder, show_full_path, sort_by_loc
                )


def display_tree(
    root_dir: str,
    exclude_dirs: Optional[List[str]] = None,
    ignore_file: Optional[str] = None,
    exclude_extensions: Optional[Set[str]] = None,
    exclude_patterns: Optional[List[str]] = None,
    include_patterns: Optional[List[str]] = None,
    use_regex: bool = False,
    max_depth: int = 0,
    show_full_path: bool = False,
    sort_by_loc: bool = False,
) -> None:
    """Display the directory tree with color-coded file types.

    Prepares the directory structure with all filtering options applied, then builds and displays a Rich tree visualization with color-coding based on file extensions. When sort_by_loc is True, displays and sorts by lines of code counts.

    Args:
        root_dir: Root directory path to display
        exclude_dirs: List of directory names to exclude from the tree
        ignore_file: Name of ignore file (like .gitignore)
        exclude_extensions: Set of file extensions to exclude (e.g., {'.pyc', '.log'})
        exclude_patterns: List of patterns to exclude
        include_patterns: List of patterns to include (overrides exclusions)
        use_regex: Whether to treat patterns as regex instead of glob patterns
        max_depth: Maximum depth to display (0 for unlimited)
        show_full_path: Whether to show full paths instead of just filenames
        sort_by_loc: Whether to sort files by lines of code and display LOC counts
    """
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_extensions is None:
        exclude_extensions = set()
    if exclude_patterns is None:
        exclude_patterns = []
    if include_patterns is None:
        include_patterns = []
    exclude_extensions = {
        ext.lower() if ext.startswith(".") else f".{ext.lower()}"
        for ext in exclude_extensions
    }
    compiled_exclude = compile_regex_patterns(exclude_patterns, use_regex)
    compiled_include = compile_regex_patterns(include_patterns, use_regex)
    structure, extensions = get_directory_structure(
        root_dir,
        exclude_dirs,
        ignore_file,
        exclude_extensions,
        exclude_patterns=compiled_exclude,
        include_patterns=compiled_include,
        max_depth=max_depth,
        show_full_path=show_full_path,
        sort_by_loc=sort_by_loc,
    )
    color_map = {ext: generate_color_for_extension(ext) for ext in extensions}
    console = Console()
    if sort_by_loc and "_loc" in structure:
        tree = Tree(f"📂 {os.path.basename(root_dir)} ({structure['_loc']} lines)")
    else:
        tree = Tree(f"📂 {os.path.basename(root_dir)}")
    build_tree(
        structure,
        tree,
        color_map,
        show_full_path=show_full_path,
        sort_by_loc=sort_by_loc,
    )
    console.print(tree)


def count_lines_of_code(file_path: str) -> int:
    """Count the number of lines of code in a file.

    Attempts to read the file in UTF-8 encoding with fallback error handling. Skips binary files and handles various encoding issues gracefully.

    Args:
        file_path: Path to the file

    Returns:
        Number of lines in the file, or 0 if the file cannot be read or is binary
    """
    try:
        with open(file_path, "rb") as f:
            sample = f.read(1024)
            if b"\0" in sample:
                logger.debug(f"Skipping binary file: {file_path}")
                return 0
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            return sum(1 for _ in f)
    except Exception as e:
        logger.debug(f"Could not count lines in {file_path}: {e}")
        return 0
