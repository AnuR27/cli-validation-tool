import json
from datetime import datetime
import argparse
import sys

def load_json(json_file):
    try:
        with open(json_file, "r") as file:
            jobs = json.load(file)
        return jobs
    except json.JSONDecodeError as jsonError:
        print("Invalid JSON Syntax: ", jsonError)
        return None
    except FileNotFoundError as FileError:
        print("File not Found: ", FileError)
        return None

def process_jobs(jobs):
    passed = failed = 0
    for job in jobs:
        if job["status"]=="passed":
            passed += 1
        elif job["status"] == "failed":
            failed += 1
    overall_status = "Failed" if failed !=0 else "Passed"
    return passed, failed, overall_status

def generate_report(output_file, jobs, passed, failed, overall_status):
    total = len(jobs)
    original_datetime = datetime.now()
    report_time = original_datetime.strftime("%Y-%m-%d %H:%M")
    with open(output_file,"w") as reportfile:
        reportfile.write("=== Validation report ===\n")
        reportfile.write(f"Generated on: {report_time}\n")
        reportfile.write(f"Total Jobs: {total}")
        reportfile.write(f"\nPassed: {passed}")
        reportfile.write(f"\nFailed: {failed}\n\n")
        reportfile.write("=== Job wise details ===\n")
        for job in jobs:
            reportfile.write(f"{job['job']} - {job['status']}\n")
        reportfile.write(f"\nOverall Status : {overall_status}")

def main():
    parser = argparse.ArgumentParser(description="Job Validation Tool") # creating the parser
    parser.add_argument("input_file", help="Path to JSON File") # Add Mandatory Argument
    parser.add_argument("--output", help="Path to report file") # optional argument
    parser.add_argument("--verbose", action="store_true", help="Enable detailed logs") # optional argument
    args = parser.parse_args() # Parse Arguments
    if args.verbose:
        print("[INFO] Loading input file...")
    jobs = load_json(args.input_file)
    if jobs is None:
        print("[ERROR] Report Generation failed")
        sys.exit(1)
    else:
        if args.verbose:
            print("[INFO] Processing jobs...")
        passed, failed, overall_status = process_jobs(jobs)
        if args.verbose:
            print("[INFO] Generating the report...")
        output_file = args.output if args.output else "report.txt"
        generate_report(output_file, jobs, passed, failed, overall_status)
        if args.verbose:
            print(f"[INFO] Report saved to {output_file}")


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
