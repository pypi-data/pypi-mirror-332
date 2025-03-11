# Test Coverage Improvement Plan

Current coverage: **62%**

## Priority 1: JSX Export Functions (38-40%)

The JSX export functionality has the lowest coverage, particularly the `_build_structure_jsx` function at 38%.

### Test Cases for `generate_jsx_component._build_structure_jsx`:

1. **Empty directory structure**

   - Test with an empty structure to ensure it handles this case gracefully

2. **Basic structure with only files, no nested directories**

   - Test with a flat file structure
   - Verify properties are correctly passed to FileItem components

3. **Deeply nested structure with multiple levels**

   - Test with 3+ levels of nesting
   - Verify the hierarchy is correctly represented

4. **Structure with statistics enabled**

   - Test with LOC, size, and mtime statistics enabled
   - Verify all props are correctly passed

5. **Structure with full paths enabled**

   - Test with show_full_path=True
   - Verify paths are formatted correctly

6. **Maximum depth reached scenarios**

   - Test with \_max_depth_reached flag set
   - Verify the indicator is rendered correctly

7. **Various file and directory sorting options**
   - Test with different combinations of sort_by_loc, sort_by_size, sort_by_mtime
   - Verify the correct sort function is applied

### Test Cases for `DirectoryExporter.to_jsx`:

1. **Exception handling**
   - Inject errors to verify error handling
   - Test with file permission issues
   - Test with disk space limitations

## Priority 2: File Operations (40-55%)

These functions interact with the filesystem and are critical for reliable operation.

### Test Cases for `get_file_size`:

1. **Normal file size retrieval**

   - Test with files of known sizes
   - Test with very small files (0 bytes)
   - Test with large files (>1GB if possible)

2. **Error conditions**

   - Test with non-existent files
   - Test with permission-denied files
   - Test with special files (symlinks, devices)

3. **Edge cases**
   - Test with files that change size during the test
   - Test with network filesystem paths

### Test Cases for `get_file_mtime`:

1. **Normal mtime retrieval**

   - Test with files with known modification times
   - Test with recently modified files
   - Test with files modified in different years

2. **Error conditions**

   - Test with non-existent files
   - Test with permission-denied files
   - Test with special files

3. **Edge cases**
   - Test with files whose timestamps change during operation
   - Test with files having future timestamps

### Test Cases for `count_lines_of_code`:

1. **Different file types**

   - Test with text files with known line counts
   - Test with binary files
   - Test with empty files
   - Test with files having only a single line
   - Test with very large files

2. **Encoding issues**

   - Test with files in different encodings (UTF-8, UTF-16, etc.)
   - Test with files containing invalid encoding

3. **Error conditions**
   - Test with non-existent files
   - Test with permission-denied files

## Priority 3: Comparison Functions (45-67%)

The comparison functionality is a key feature and needs better coverage.

### Test Cases for `build_comparison_tree`:

1. **Basic comparison scenarios**

   - Identical directories
   - One directory empty, one with content
   - Directories with no common files

2. **Different file and directory states**

   - Files only in left directory
   - Files only in right directory
   - Files in both but with different attributes

3. **Statistics display testing**

   - Test with different combinations of sort_by_loc, sort_by_size, sort_by_mtime
   - Verify correct display of statistics in all scenarios

4. **Path display testing**

   - Test with show_full_path=True and False
   - Test with very long paths that might require special handling

5. **Edge cases**
   - Test with the \_max_depth_reached flag
   - Test with empty structures

### Test Cases for `_export_comparison_to_html._build_html_tree`:

1. **Various structure combinations**

   - Test with empty structures
   - Test with deeply nested structures
   - Test with only files, no directories

2. **HTML output validation**

   - Validate HTML is well-formed
   - Test proper escaping of special characters in file/directory names
   - Test that CSS classes are correctly applied

3. **Statistic display variations**
   - Test all combinations of statistics display options
   - Verify formatting of size, LOC, and time values

## Priority 4: Tree Building Functions (44-53%)

These are core to the visualization capabilities.

### Test Cases for `build_tree`:

1. **Structure variations**

   - Test with empty structure
   - Test with files only
   - Test with directories only
   - Test with deeply nested structures

2. **Display options**

   - Test with all combinations of sort_by_loc, sort_by_size, sort_by_mtime
   - Test with show_full_path=True and False

3. **Special cases**
   - Test with \_max_depth_reached flag
   - Test with very long file/directory names
   - Test with special characters in names

### Test Cases for `DirectoryExporter.to_html._build_html_tree`:

1. **HTML structure validation**

   - Verify generated HTML is well-formed
   - Test for proper nesting of ul/li elements
   - Test correct application of CSS classes

2. **Content formatting**

   - Test proper escaping of HTML special characters
   - Test formatting of statistics in various scenarios

3. **Edge cases**
   - Test with empty structures
   - Test with \_max_depth_reached flag

### Similar tests for `DirectoryExporter.to_markdown._build_md_tree` and `DirectoryExporter.to_txt._build_txt_tree`

## Priority 5: Export Functionality (67-75%)

These functions handle the conversion to different export formats.

### Test Cases for Export Functions:

1. **Format-specific tests**

   - Verify correct formatting for each export type
   - Test for well-formed output

2. **Error handling**

   - Test with write permission issues
   - Test with disk space limitations

3. **Option combinations**
   - Test with various combinations of display options
   - Test with different depth limits

## Implementation Approach

For effective coverage improvement, I recommend:

1. **Create Mocked File Systems**:
   Use pytest fixtures to create controlled file system environments

2. **Use Parametrized Tests**:
   Create parametrized test functions to test multiple scenarios efficiently

3. **Add Error Injection**:
   Use mocking to inject errors and test error handling

4. **Output Validation**:
   For export functions, validate the structure and content of generated files
