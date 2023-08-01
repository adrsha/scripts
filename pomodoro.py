import time
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


def circularDecor(icon, text, color):
    return f"{asc_colors[f'{color}']}{asc_colors[f'{color}Bg']}\033[1m{icon}{text}\033[0m{asc_colors['defBg']}{asc_colors[f'{color}']} "


count = 0
print("Pomodoro")


def wait(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(circularDecor(timer), end="\r")
        time.sleep(1)
        t -= 1


if __name__ == "__main__":
    while True:
        wait(5)
        count += 1
        print("Good work! a pomodoro Session has completed!")
        time.sleep(600)
        print("Back to work!", "Try doing another pomodoro...")
