#!/bin/python3
import os
import sys


themeFile = open("/home/chilly/Scripts/data/themeIndex.txt", "r")
themes = [
    [0, "code"],
    [1, "nord"],
    [2, "washed"],
    [3, "aqua"],
]
inde = sys.argv[1]
i = int(themeFile.read())

if inde == "u":
    i = i + 1
    if i >= len(themes):
        i = 0
    print("up", i)
elif inde == "d":
    i = i - 1
    print("down", i)
    if i < 0:
        i = len(themes) - 1
else:
    print("Input correct value!")
    exit(1)

# print(themes)
currentTheme = themes[i]

print(currentTheme)
# os.system(f"/home/chilly/Scripts/theme {currentTheme[1]} && ")
os.system(
    f"echo {i} > /home/chilly/Scripts/data/themeIndex.txt && ~/Scripts/theme {currentTheme[1]}"
)
