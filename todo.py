# !TODO Move the elements (priority)
import os
import sys

asc_colors = {
    "default": "\u001b[m",
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
}

val = 0
todos = []

if len(sys.argv) > 1:
    inde = sys.argv[1]
    if len(sys.argv) != 2:
        val = sys.argv[2]
    else:
        if inde == "a":
            val = input("Add: ")
        elif inde == "r":
            val = input("Remove: ")
else:
    inde = "s"

file = open("/home/chilly/Scripts/todo.txt", "r")
for t in file:
    if t != "\n":
        todos.append(t)

def clearFile():
    os.system(
        "rm -rf /home/chilly/Scripts/todo.txt && touch /home/chilly/Scripts/todo.txt"
    )

def putVal(val):
    os.system(f'echo "{val}" >> /home/chilly/Scripts/todo.txt')


def show(terminal=False):
    if terminal and len(todos) == 0:
        pass
    else:
        os.system("clear")
        print(f"\n\033[1m  {asc_colors['black']}<{asc_colors['cyan']}TODOS{asc_colors['black']}> {asc_colors['white']}\n")
        if len(todos) == 0:
            print(f"{asc_colors['red']}No Todos Found!{asc_colors['white']}")
        else:
            for i, x in enumerate(todos):
                x = x.replace("\n", "")
                print(
                    f"{asc_colors['yellow']}↪  {i+1}.{asc_colors['green']} {x} {asc_colors['white']} ",
                )

if inde == "a":
    clearFile()
    todos.append(val)
    for t in todos:
        putVal(t)
    show()
elif inde == "r":
    clearFile()
    todos.pop(int(val) - 1)
    # if f"{val}\n" in todos:
    #     todos.remove(f"{val}\n")
    # else:
    #     print("That value doesnt exist!")
    for t in todos:
        putVal(t)
    show()

elif inde == "s":
    show()
elif inde == "t":
    show(True)
