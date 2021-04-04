#!/usr/bin/python
# -*- coding: <utf-8> -*-

import os
import sys
import hashlib

def hash_check(src : str, hash_func : str, benchmark : str) -> str:
    """Checks if hash of the file is correct and print result

    src       - source file to check
    hash_func - hash algorythm
    benchmark - correct hash"""
    if os.path.isfile(src):
        try:
            with open(src, 'rb') as file:
                hash_data_init = getattr(hashlib, hash_func)
                hash_result = hash_data_init()
                for block in iter(lambda: file.read(4096), b""):
                    hash_result.update(block)
                if hash_result.hexdigest() == benchmark:
                    return "OK"
                else:
                    return "FAIL"
        except FileNotFoundError:
            return "NOT FOUND"
        except PermissionError:
            return "NOT FOUND"

    else:
        return "NOT FOUND"

def main_processing(input_file_path : str, data_dir_path : str):
    """Parses input and calls hash checks.

    input_file_path - pat to the input file
    data_dir_path   - path to the directory containing the files to check"""

    expected_hash_functions = ('md5', 'sha1', 'sha256')

    if not os.path.isdir(data_dir_path):
        print("Bad parameters, check if directory with data exists.\n")
        return

    if os.path.isfile(input_file_path):
        try:
            with open(input_file_path, 'r') as input_file:
                for line in input_file:
                    input_arguments = list(filter(None, line.strip().split()))
                    if len(input_arguments) != 3:
                        print("Bad parameters.")
                        continue
                    if not input_arguments[1] in expected_hash_functions:
                        print(f"{input_arguments[0]} Bad parameters, hash function is not supported.")
                        continue

                    print(input_arguments[0], hash_check(os.path.join(data_dir_path, input_arguments[0]), input_arguments[1], input_arguments[2]))

        except FileNotFoundError:
            print(f"Input file {FileNotFoundError.filename} access"
                  "error. Check path.\n")
            return
        except PermissionError:
            print(f"Input file {PermissionError.filename} access"
                  "error. Check user access rights.\n")
            return
            
    else:
        print(f"Input file {input_file_path} access error. Check path.\n")

if __name__ == "__main__":
    if (sys.argv[0] == '') or (len(sys.argv) < 3):
        print("Bad parameters passed to the program.\n")
    else:
        input_file = sys.argv[1]
        input_dir  = sys.argv[2]
        main_processing(input_file, input_dir)
