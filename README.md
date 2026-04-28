# CLI Validation Report Tool

A Python-based command-line tool to process job execution data from JSON files and generate structured validation reports.

# Features
- CLI-based execution using argparse
- Processes job status (passed/failed)
- Generates detailed report files
- Supports optional arguments:
  - --output for custom report file
  - --verbose for detailed logs
- Error handling for invalid JSON and missing files

# Tech Stack
- Python
- argparse
- JSON
- File Handling

# Usage
python tool.py jobs_data.json
python tool.py jobs_data.json --output report.txt --verbose
