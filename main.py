import os
import hashlib

def hash_check(src : str, hash_func : str, benchmark : str) -> str:
    """Checks if hash of the file is correct"""
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
            
    else:
        return "NOT FOUND"

def main_processing():
    """Parses input and calls hash checks."""

    expected_hash_functions = ('md5', 'sha1', 'sha256')
    
    #if (sys.argv[0] == '')
        #print("Bad parameters passed to the program.\n")
        #return
    #mainfile = sys.argv[1]
    #maindir  = sys.argv[2]
    mainfile = r'E:\GitHub\test_task\input_file.txt'
    maindir  = r'E:\GitHub\test_task\\'
    if not os.path.isdir(maindir):
        print("Bad parameters, check if directory with data exists.\n")
        return

    if os.path.isfile(mainfile):
        try:
            with open(mainfile, 'r') as input_file:
                for line in input_file:
                    input_arguments = list(filter(None, line.strip().split()))
                    if len(input_arguments) != 3:
                        print("Bad parameters")
                        continue
                    if not input_arguments[1] in expected_hash_functions:
                        print(f"{input_arguments[0]} Bad parameters, hash function is not supported.")
                        continue
                    
                    print(input_arguments[0], hash_check(maindir + '\\' + input_arguments[0], input_arguments[1], input_arguments[2]))
                    
        except FileNotFoundError:
            print(f"Input file {FileNotFoundError.filename} access"
                  "error. Check path.\n")
            return

if __name__ == "__main__":
    main_processing()
