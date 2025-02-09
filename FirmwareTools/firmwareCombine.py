#!/usr/bin/env python3

# Name: firmwareCombine.py
# Author: gerbil
# Version: 0.1 - 20241128
# Description: Combines many files into one file by interleaving. 
#              Perfect for combining U9 and U7 images into one firmware.

import sys

def interleave_files(input_files, output_file):
    file_handlers = [open(file, 'rb') for file in input_files]
    try:
        with open(output_file, 'wb') as output:
            while True:
                all_done = True
                for file_handler in file_handlers:
                    byte = file_handler.read(1)
                    if byte:
                        output.write(byte)
                        all_done = False
                if all_done:
                    break
    finally:
        for file_handler in file_handlers:
            file_handler.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 firmwareCombine.py <input_file1> <input_file2> ... <input_fileN> <output_file>")
        sys.exit(1)
    
    input_files = sys.argv[1:-1]
    output_file = sys.argv[-1]
    
    interleave_files(input_files, output_file)
