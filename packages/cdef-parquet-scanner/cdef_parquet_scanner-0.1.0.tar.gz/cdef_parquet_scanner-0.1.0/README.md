# CDEF Parquet Scanner

A tool for scanning Parquet files, analyzing their schema structures, and generating reports about schema patterns and data characteristics.

## Features

- Scans directories recursively for Parquet files
- Groups files by schema similarity
- Analyzes column characteristics (types, compression, cardinality)
- Detects potentially sensitive columns with high cardinality
- Generates detailed reports on schema patterns

## Installation

```bash
pip install cdef-parquet-scanner
```

## Usage

```bash
# As a module
python -m cdef_parquet_scanner.schema <directory_path> [output_file]

# As a command-line tool
cdef-parquet-scanner <directory_path> [output_file]
```

If no output file is specified, the report will be saved as `parquet_schema_report.txt` in the current directory.

## Example

```bash
cdef-parquet-scanner /path/to/data/directory report.txt
```

## License

MIT