import colorama
from colorama import Fore, Back, Style

colorama.init()

def set_color(clr):
    colors = {
        "red" : Fore.RED,
        "yellow" : Fore.YELLOW,
        "green" : Fore.GREEN,
        "cyan" : Fore.CYAN,
        "blue" : Fore.BLUE,
        "purple" : Fore.MAGENTA
    }
    print(Style.BRIGHT + colors[clr], end = '')

def reset_color():
    print(Style.RESET_ALL, end = '')

# color text on terminal
def cprint(*args, clr = None, **kwargs):
    reset_color()
    if(clr != None):
        set_color(clr)
    print(*args, **kwargs)
    reset_color()