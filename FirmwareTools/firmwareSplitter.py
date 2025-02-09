#!/usr/bin/env python3

# Name: firmwareSplitter.py
# Author: gerbil
# Version: 0.1 - 20241128
# Description: Splits a file into two - all even bytes in one file (U9) and odd bytes in another file (U7). 

import sys
import os

def split_firmware(input_file):
    try:
        # Derive output filenames
        base_name, ext = os.path.splitext(input_file)
        output_file_U9 = f"{base_name}_U9{ext}"
        output_file_U7 = f"{base_name}_U7{ext}"

        # Open the input file in binary mode for reading
        with open(input_file, 'rb') as infile, \
             open(output_file_U9, 'wb') as outfile_U9, \
             open(output_file_U7, 'wb') as outfile_U7:

            # Write bytes alternately to the output files
            index = 0  # 0 for U9, 1 for U7
            while True:
                byte = infile.read(1)
                if not byte:
                    break

                if index == 0:
                    outfile_U9.write(byte)
                else:
                    outfile_U7.write(byte)

                # Alternate index (round-robin)
                index = 1 - index

        print(f"Firmware split successfully into '{output_file_U9}' and '{output_file_U7}'!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure exactly one input file is specified
    if len(sys.argv) != 2:
        print("Usage: python3 firmwareSplitter.py <input_file>")
        sys.exit(1)

    # Get the input filename
    input_filename = sys.argv[1]

    # Call the function to split the firmware
    split_firmware(input_filename)
