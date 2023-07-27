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
    "white": "\u001b[37m",
}

val = 0
todos = []
try:
    if len(sys.argv) > 1:
        inde = sys.argv[1]
        if len(sys.argv) != 2:
            val = sys.argv[2]
        else:
            if inde == "a":
                val = input("Add: ")
            elif inde == "ai":
                ind = input("Add under [index]: ")
                val = input("Add: ")
            elif inde == "r":
                val = input("Remove: ")
            elif inde == "e":
                val = input("Give the index: ")
                newval = input("Edit: ")
            elif inde == "sw":
                oldindex = input("From: ")
                newindex = input("To: ")
            elif inde == "m":
                oldindex = input("From: ")
                newindex = input("To: ")
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
        # elif terminal:
        #     os.system("clear")
        #     output = subprocess.getoutput("ps | grep 'tty' | wc -l ")
        #     if output == "0":
        #         print(
        #             f"{asc_colors['black']}┏━━━°⌜\033[1m{asc_colors['black']}<{asc_colors['cyan']}TODOS{asc_colors['black']}>⌟°━━━┓ {asc_colors['white']}"
        #         )
        #         print(
        #             f"\n\033[1m {asc_colors['black']}  {asc_colors['red']}{len(todos)} {asc_colors['green']}Tasks Remaining"
        #         )
        #         print(
        #             f"\n{asc_colors['black']}┗━━━°⌜.✧ ✦ ✧.⌟°━━━┛{asc_colors['white']}"
        #         )
        else:
            os.system("clear")
            print(
                f"{asc_colors['black']}┏━━━°⌜\033[1m{asc_colors['black']}<{asc_colors['magenta']}TODOS{asc_colors['black']}>⌟°━━━┓ {asc_colors['white']}\n"
            )
            if len(todos) == 0:
                print(f"{asc_colors['red']}No Todos Found!{asc_colors['white']}")
            else:
                for i, x in enumerate(todos):
                    x = x.replace("\n", "")
                    if ":" in x:
                        group = x.split(":")
                        print(
                            f"{asc_colors['yellow']} {asc_colors['magenta']} {group.pop(0)} {asc_colors['green']} {i+1} ",
                        )
                        for j, el in enumerate(group):
                            print(
                                f"{asc_colors['black']}  ⊚{asc_colors['red']} {el} {asc_colors['green']} {i+1},{j+1}",
                            )
                    else:
                        print(
                            f"{asc_colors['yellow']} {asc_colors['magenta']} {x} {asc_colors['green']} {i+1} ",
                        )
                print(
                    f"\n{asc_colors['black']}┗━━━°⌜.✧ ✦ ✧.⌟°━━━┛{asc_colors['white']}"
                )

    if inde == "a":
        clearFile()
        todos.append(val)
        for t in todos:
            putVal(t)
        show()
    elif inde == "ai":
        clearFile()
        actInd = int(ind) - 1
        temp = todos.pop(actInd).replace("\n", "")
        todos.insert(actInd, f"{temp}:{val}")
        for t in todos:
            putVal(t)
        show()
    elif inde == "r":
        clearFile()
        if "," in val:
            fInd = val.split(",")[0]
            sInd = val.split(",")[1]
            elem = todos[int(fInd) - 1].split(":")[int(sInd)]
            todos[int(fInd) - 1] = (
                todos[int(fInd) - 1].replace(f":{elem}", "").replace("{elem}:", "")
            )
        else:
            todos.pop(int(val) - 1)
        for t in todos:
            putVal(t)
        show()
    elif inde == "e":
        clearFile()
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
        for t in todos:
            putVal(t)
        show()

    elif inde == "s":
        show()
    elif inde == "t":
        show(True)
    elif inde == "sw":
        clearFile()
        if "," in newindex or "," in oldindex:
            if "," not in newindex:
                newindex = newindex + ",0"
            if "," not in oldindex:
                oldindex = oldindex + ",0"
            destFInd = int(newindex.split(",")[0]) - 1
            destSInd = int(newindex.split(",")[1])
            sourceFInd = int(oldindex.split(",")[0]) - 1
            sourceSInd = int(oldindex.split(",")[1])
            source = todos[sourceFInd].split(":")[sourceSInd].replace("\n", "")
            dest = todos[destFInd].split(":")[destSInd].replace("\n", "")
            todos[sourceFInd] = todos[sourceFInd].replace(source, "%temp%")
            todos[destFInd] = todos[destFInd].replace(dest, source)
            todos[sourceFInd] = todos[sourceFInd].replace("%temp%", dest)
        else:
            popped = todos.pop(int(oldindex) - 1)
            todos.insert(int(newindex) - 1, popped)
        for t in todos:
            putVal(t)
        show()

except:
    for t in todos:
        putVal(t)
