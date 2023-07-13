import os
import sys


themeFile = open("/home/chilly/Scripts/data/themeIndex.txt", "r")
themes = [[0, "special"], [1, "code"], [2, "dreamy"]]
inde = sys.argv[1]
i = int(themeFile.read())

if inde == "u":
    i = i + 1
    if i > len(themes) - 1:
        i = 0
    print("Top", i)
elif inde == "d":
    i = i - 1
    if i < 0:
        i = len(themes) - 1
    print("Bot", i)
else:
    print("Input correct value!")
    exit(1)

print(themes)
currentTheme = themes[i]

os.system(
    f"/home/chilly/Scripts/theme {currentTheme[1]} && echo {i} > /home/chilly/Scripts/data/themeIndex.txt"
)
