#!/bin/python3
# !TODO Move the elements (priority)
import os
import subprocess
import sys

asc_colors = {
    "default": "\u001b[m",
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "grey": "\u001b[37m",
    "blackBg": "\033[37;40m",
    "redBg": "\033[37;41m",
    "greenBg": "\033[30;42m",
    "yellowBg": "\033[37;43m",
    "blueBg": "\033[30;44m",
    "magentaBg": "\033[30;45m",
    "cyanBg": "\033[30;46m",
    "defBg": "\033[37;m",
}


def findIndex(x, search, index_of_occurance):
    n = index_of_occurance
    if n == 0:
        start = -1
    else:
        start = x.find(search)
    while start >= 0 and n > 1:
        start = x.find(search, start + len(search))
        n -= 1
    return start


def circularDecor(icon, text, color):
    return f"{asc_colors[f'{color}']}{asc_colors[f'{color}Bg']}\033[1m{icon}{text}\033[0m{asc_colors['defBg']}{asc_colors[f'{color}']} "


val = 0
todos = []
# try:
if len(sys.argv) > 1:
    inde = sys.argv[1]
    if len(sys.argv) != 2:
        val = sys.argv[2]
    else:
        if inde == "a":
            val = input(circularDecor(" ", "Todo to add", "magenta"))
        elif inde == "ai":
            ind = input(circularDecor(" ", "Index to add inside", "magenta"))
            print("")
            val = input(circularDecor(" ", "Add?", "magenta"))
        elif inde == "r":
            val = input(circularDecor("󰚃 ", "Remove", "magenta"))
        elif inde == "e":
            val = input(circularDecor("󰛿 ", "Replace Index", "magenta"))
            print("")
            newval = input(circularDecor("󰛿 ", "With", "magenta"))
        elif inde == "sw":
            oldindex = input(circularDecor("󰿡 ", "Swap Index", "magenta"))
            print("")
            newindex = input(circularDecor("󰿡 ", "With", "magenta"))
        elif inde == "m":
            oldindex = input(circularDecor("󰿡 ", "Move From", "magenta"))
            print("")
            newindex = input(circularDecor("󰿡 ", "To", "magenta"))
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


def edit():
    if "," in val:
        fInd = val.split(",")[0]
        sInd = val.split(",")[1]
        elem = todos[int(fInd) - 1].split(":")[int(sInd)]
        todos[int(fInd) - 1] = (
            todos[int(fInd) - 1]
            .replace(f":{elem}", f":{newval}")
            .replace("{elem}:", "{newval}:")
        )
    else:
        todos.pop(int(val) - 1)
        todos.insert(int(val) - 1, newval)


def insertTodo(ind, val):
    if "," in str(ind):
        indF = int(ind.split(",")[0]) - 1
        indS = int(ind.split(",")[-1])
        colInd = findIndex(todos[indF], ":", indS)
        todos[indF] = todos[indF][:colInd] + f":{val}" + todos[indF][colInd:]
    else:
        todos.insert(int(ind) - 1, val)


def remove(val):
    if "," in val:
        fInd = int(val.split(",")[0]) - 1
        sInd = int(val.split(",")[1])
        stringSInit = findIndex(todos[fInd], ":", sInd)
        stringSEnd = findIndex(todos[fInd], ":", sInd + 1)
        todos[fInd] = todos[fInd][:stringSInit] + todos[fInd][stringSEnd:]
    else:
        todos.pop(int(val) - 1)


def swap(oldindex, newindex):
    if "," in newindex or "," in oldindex:
        if "," not in newindex:
            newindex = newindex + ",0"
        if "," not in oldindex:
            oldindex = oldindex + ",0"
        destArrayFInd = int(newindex.split(",")[0]) - 1
        destArraySInd = int(newindex.split(",")[1])
        sourceArrayFInd = int(oldindex.split(",")[0]) - 1
        sourceArraySInd = int(oldindex.split(",")[1])
        source = todos[sourceArrayFInd].split(":")[sourceArraySInd].replace("\n", "")
        dest = todos[destArrayFInd].split(":")[destArraySInd].replace("\n", "")
        sourceInit = findIndex(todos[sourceArrayFInd], ":", sourceArraySInd)
        sourceEnd = findIndex(todos[sourceArrayFInd], ":", sourceArraySInd + 1)
        # print(todos[destArrayFInd], todos[sourceArrayFInd])
        todos[sourceArrayFInd] = (
            todos[sourceArrayFInd][: sourceInit + 1]
            + dest
            + todos[sourceArrayFInd][sourceEnd:]
        )
        # print(todos[destArrayFInd], todos[sourceArrayFInd])
        destInit = findIndex(todos[destArrayFInd], ":", destArraySInd)
        destEnd = findIndex(todos[destArrayFInd], ":", destArraySInd + 1)
        todos[destArrayFInd] = (
            todos[destArrayFInd][: destInit + 1]
            + source
            + todos[destArrayFInd][destEnd:]
        )
        # print(todos[destArrayFInd], todos[sourceArrayFInd])
        # exit()
    else:
        popped = todos.pop(int(oldindex) - 1)
        todos.insert(int(newindex) - 1, popped)


def addInside(ind, val):
    actInd = int(ind) - 1
    temp = todos.pop(actInd).replace("\n", "")
    todos.insert(actInd, f"{temp}:{val}")


def putVal(val):
    os.system(f'echo "{val}" >> /home/chilly/Scripts/todo.txt')


def show(terminal=False):
    if terminal and len(todos) == 0:
        pass
    elif terminal:
        os.system("clear")
        output = subprocess.getoutput("ps | grep 'tty' | wc -l ")
        output1 = subprocess.getoutput("ps | grep 'pts' | wc -l ")
        if output == "0" and int(output1) > 0:
            show()
    else:
        os.system("clear")
        print(
            f"\033[1m{asc_colors['magenta']}{asc_colors['magentaBg']}\033[38;2;48;48;68m TODOS{asc_colors['defBg']}{asc_colors['magenta']}\033[0m\n"
        )
        if len(todos) == 0:
            print(f"{asc_colors['red']}No Todos Found!{asc_colors['default']}")
        else:
            for i, x in enumerate(todos):
                x = x.replace("\n", "")
                if ":" in x:
                    group = x.split(":")
                    print(
                        f"\033[1m{asc_colors['yellow']} {asc_colors['magenta']} {group.pop(0)} {asc_colors['green']}{asc_colors['green']}{asc_colors['greenBg']} {i+1}{asc_colors['defBg']}{asc_colors['green']}",
                    )
                    for j, el in enumerate(group):
                        print(
                            f"{asc_colors['black']}   {asc_colors['red']} {el} {asc_colors['green']} {i+1},{j+1}\033[0m",
                        )
                else:
                    print(
                        f"\033[0m{asc_colors['yellow']} {asc_colors['magenta']} {x} {asc_colors['green']}{asc_colors['greenBg']} {i+1}{asc_colors['defBg']}{asc_colors['green']}",
                    )


if inde == "a":
    clearFile()
    todos.append(val)
    for t in todos:
        putVal(t)
    show()
elif inde == "ai":
    clearFile()
    addInside(ind, val)
    for t in todos:
        putVal(t)
    show()

elif inde == "r":
    clearFile()
    remove(val)
    for t in todos:
        putVal(t)
    show()
elif inde == "e":
    clearFile()
    edit()
    for t in todos:
        putVal(t)
    show()
elif inde == "s":
    show()
elif inde == "t":
    show(True)
elif inde == "m":
    clearFile()
    if "," in oldindex or "," in newindex:
        if "," not in oldindex:
            oldindex = oldindex + ",0"
        elif "," not in newindex:
            newindex = newindex + ",0"
        moveVal = (
            todos[int(oldindex.split(",")[0]) - 1]
            .split(":")[int(oldindex.split(",")[1])]
            .replace("\n", "")
        )
        # print(todos, newindex, oldindex)
        if newindex.split(",")[0] == oldindex.split(",")[0]:
            if newindex.split(",")[1] < oldindex.split(",")[1]:
                insertTodo(newindex, moveVal)
                oldindex = (
                    oldindex.split(",")[0] + "," + str(int(oldindex.split(",")[1]) + 1)
                )
            else:
                insertTodo(
                    newindex.split(",")[0] + "," + str(int(newindex.split(",")[1]) + 1),
                    moveVal,
                )
    else:
        insertTodo(newindex, todos[int(oldindex) - 1])
        if int(newindex) < int(oldindex):
            oldindex = str(int(oldindex) + 1)
    remove(oldindex)
    # print(todos)
    for t in todos:
        putVal(t)
    show()
elif inde == "sw":
    clearFile()
    swap(oldindex, newindex)
    for t in todos:
        putVal(t)
    show()

#
# except Exception as e:
#     print(e)
#     for t in todos:
#         putVal(t)
