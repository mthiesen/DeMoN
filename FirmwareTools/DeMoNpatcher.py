#!/usr/bin/env python3

# Name: DeMoNpatcher.py
# Author: gerbil
# Version: 0.3 - 20250218
# Description: Patches the original Action Replay 3 binary ROM to be used with DeMoN.
#              First four bytes are ignored as they can differ with different ROMs.
#              Note: The version of Action Replay 3 ROM MUST be version 3.17 (12/17/91)


import sys
import os

def patch_files(AR3file, DeMoNpatch, key):
    # Uses the name of the second (patch) file and uses this as the base of the output filename,
    # then stores an XOR'd version of both files as the output.
    base_name, ext = os.path.splitext(DeMoNpatch)
    patch_filename = f"{base_name}_patched{ext}"
    ctr=0
    
    try:
        with open(AR3file, "rb") as f1, open(DeMoNpatch, "rb") as f2, open(patch_filename, "wb") as out:
            
            # Copy the first 4 bytes of AR3file to the output file, thus not changing.
            out.write(f1.read(4))

            # Skip the first 4 bytes of both input files.
            f1.seek(4)
            f2.seek(4)

            
            # Now do XOR operation on the rest of the file. 
            while True:
                byte1 = f1.read(1)
                byte2 = f2.read(1)
                
                # Stop when end of file is reached
                if not byte1 or not byte2:
                    break
                
                # XOR the bytes and write to the output file
                out.write(bytes([byte1[0] ^ byte2[0] ^ ctr]))                
                ctr = ((ctr + 10 + byte1[0] ) % 256)
        
        print(f"Patched file created: {patch_filename}")
    except FileNotFoundError:
        print("Error: One or both input files do not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 DeMoNpatcher.py <AR3rom file> <DeMoNpatch file>")
    else:
        key = "KioqIEdyZWV0cyB0byB0aGUgSGF4b3JzISBCZWZvcmUgeW91IHBvaW50IG91dCB0aGUgb2J2aW91cyB3aXRoIHRoaXMgc2NyaXB0IC0geWVzLCBJIGFscmVhZHkga25vdyEgOlAgSGF2ZSBmdW4gcGVlcHMhICoqKiAK"
        AR3file, DeMoNpatch = sys.argv[1], sys.argv[2]
        patch_files(AR3file, DeMoNpatch, key)
        

