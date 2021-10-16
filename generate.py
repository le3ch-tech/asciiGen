import os
import sys

command = lambda x: os.system(x)

argument = sys.argv[1]
title = f'{argument}'

if os.name != 'nt':
    command('clear')
else:
    command('cls')

try: 
    import pyfiglet as Figlet
except ModuleNotFoundError:
    if os.name != 'nt':
        command('python3 -m pip install pyfiglet')
    else:
        command('pip install pyfiglet')

class BColors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"	

def print_banner(text):
	print(BColors.RED + Figlet(font='banner3-D').renderText(text))

print_banner(title)