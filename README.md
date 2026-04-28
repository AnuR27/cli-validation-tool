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

# Example output
=== Validation report ===
Generated on: 2026-04-25 12:42
Total Jobs: 3
Passed: 2
Failed: 1

=== Job wise details ===
Build - passed
Test - failed
Deploy - passed

# PROJECT STRUCTURE
.
├── tool.py
├── jobs_data.json
├── report.txt
