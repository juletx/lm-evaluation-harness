import glob
import json
import os

import pandas as pd  # retained import for pandas


def check_jsonl_files(directory):
    errors_found = {}
    pattern = os.path.join(directory, "*.jsonl")
    for file in glob.glob(pattern):
        with open(file, "r") as f:
            for line_no, line in enumerate(f, start=1):
                try:
                    json.loads(line)
                except json.JSONDecodeError as e:
                    errors_found.setdefault(file, []).append((line_no, str(e)))
    return errors_found


def check_with_pandas(directory):
    # New function using pandas to read JSONL files
    pandas_errors = {}
    pattern = os.path.join(directory, "*.jsonl")
    for file in glob.glob(pattern):
        try:
            pd.read_json(file, lines=True)
        except Exception as e:
            pandas_errors[file] = str(e)
    return pandas_errors


if __name__ == "__main__":
    directory = "data/BasqBBQ"
    errors = check_jsonl_files(directory)
    if errors:
        for file, errs in errors.items():
            print(f"JSON decode errors in {file}:")
            for line_no, msg in errs:
                print(f"  Line {line_no}: {msg}")
    else:
        print("All JSONL files pass JSON decoding.")

    pandas_errors = check_with_pandas(directory)
    if pandas_errors:
        for file, msg in pandas_errors.items():
            print(f"Pandas read_json error in {file}: {msg}")
    else:
        print("All JSONL files read successfully with pandas.")
