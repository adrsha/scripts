#!/bin/python3

import subprocess
import os
import sys

dirs = []

if len(sys.argv) > 1:
    print(len(sys.argv))
    for i in range(len(sys.argv)):
        dirs.append(sys.argv[i])
else:
    dirs = subprocess.getoutput("ls").split("\n")

for i, d in enumerate(dirs):
    change = (
        d.replace(" ", "")
        .replace("-", "")
        .replace("(", "")
        .replace(")", "")
        .replace("'", "")
    )
    if d != change:
        os.system(f"mv '{d}' {change}")
        print(change)
