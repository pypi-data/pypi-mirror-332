### PO files translator from local codebases

A simple CLI tool that scans a codebase for translations and updates a given PO file. It automatically extracts the language from the PO file's name (for example, "ar.po" yields the language code "ar").

## Installation

Clone the repository and install with pip:

```bash
pip3 install pofiletranslate
```

## Usage

Run the tool by providing the full path to your PO file. You can also specify a codebase directory to scan and a list of directory names to exclude.

For help, run:

```bash
pofiletranslate --help
```

Here’s the updated `README` file section for the command-line arguments with the updated `--exclude` parameter:

### Command-Line Arguments

- **`po_file_path` (required):** Full path to the PO file you want to process.  
  *Example:* `/full/path/to/ar.po`
  
- **`--depth` (optional):** Backtrack depth for computing the codebase directory. Defaults to `4`.  
  *Example:* `--depth 3`
  
- **`--exclude` (optional):** Comma-separated list of directory names to exclude from the scan. 
Defaults to an empty string, meaning no directories are excluded.  
  *Example:* `--exclude "dir1,dir2"`
  - This will exclude the directories `dir1` and `dir2` from the translation scan.

### Example usage:

```bash
pofiletranslate /full/path/to/ar.po --depth 3 --exclude "dir1,dir2"
```
This example will process the `ar.po` file with a depth of `3` and will exclude 
the directories `dir1` and `dir2` from the scan.

## What It Does

The tool scans the specified codebase for PO files matching the derived language (e.g., "ar") 
and updates your provided PO file with any matching translations found.

## License

This project is licensed under the MIT License.
