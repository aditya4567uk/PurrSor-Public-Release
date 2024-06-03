import os

import ctypes
import tkinter as tk
from infi.systray import SysTrayIcon
from rich.console import Console
#from rich.table import Table

from purrsor import purr
from purrsor.utils import files, configs

GWL_EXSTYLE = -20
WS_EX_TOOLWINDOW = 0x80

print('WELCOME TO PURRSOR')

console = Console()
'''
table = Table(title="Welcome to PurrSor", style="bold red")

table.add_column("Cat Description", style="cyan")
table.add_column("config code", style="bold green")

table.add_row("Black cat","black")
#console.print(table)
'''
string = '''


───────────────────────────────────────████████████████████████████████████████
───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────█░░░░░░░██░█░░░░░░░░░░░░░░▐█▌░░░░░░░░░░█
──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────█░░░░░░░██▀█▐▀█░█░█▐▀█░░░██▀██░░░░░░░░░█
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────█░░░░░░░██░█▐▀█░▀▄▀▐█▄░▄██▀▀▀██▄░░░░░░░█
▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄█░░░░░░░░░░░░░░░░░██▀▀▀░░░░░░░░█░░░░░░░█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒██░░░░░░░░░░░░░░░░░██─▄▄▐▀█▐▀█▐▀█░░░░░░░█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─█░░░░░░░░░░░░░░░░░██▄██▐▄█▐▄█▐▄█░░░░░░░█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────█░░░░░░░░▀██▀▄░░░░░░░░░░░░░░░░░░░░░░░░░█
─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────█░░░░░░░░░██░▐█▐▀█▐▄█░░░░░░░░░░░░░░░░░░█
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────█░░░░░░░░▄██▄▀░▐▀█░▄█░░░░░░░░░░░░░░░░░░█
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────████████████████████████████████████████
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────



'''
string2 = '''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ██████╗ ██╗   ██╗██████╗ ██████╗ ███████╗ ██████╗ ██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ██████╔╝██║   ██║██████╔╝██████╔╝███████╗██║   ██║██████╔╝
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██╔═══╝ ██║   ██║██╔══██╗██╔══██╗╚════██║██║   ██║██╔══██╗
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ██║     ╚██████╔╝██║  ██║██║  ██║███████║╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝                                                                                                                                                  
'''

print(f'{string2}')
print(f'{string}')

print("List of all available cats")
path = "./resource"
listofcats = os.listdir(path)

console.print(listofcats, style="bold red")
console.print(" If you want to change cat then NOTE any one of the NAMES listed above", style="bold underline yellow on black")
console.print(" then go to config folder", style="bold cyan")
console.print(" there you will find a file name default_config.yml", style="bold cyan")
console.print(" open that file and at 2nd last line after animal: give any name you noted previously", style="bold cyan")
console.print(" For example ->  animal: silver , this will give you grey color cat", style="bold cyan")

#inp = input('what cat do you want??')

def timer(root, myPurr, fps=200):
    myPurr.update()
    root.after(fps, lambda: timer(root, myPurr, fps))


def quit(systray, root):
    root.quit()


def _hide_from_alt_tab(root):
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style |= WS_EX_TOOLWINDOW
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)


if __name__ == "__main__":
    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    canvas = tk.Canvas(bg="green", width=w, height=h, highlightthickness=0)
    canvas.place(x=0, y=0)
    root.overrideredirect(True)
    root.geometry(f"{w}x{h}+0+0")
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "green")

    root.after(10, _hide_from_alt_tab, root)

    root.update()

    myPurr = purr.Purr(root, canvas)
    fps = configs.get_int("fps")

    animal = configs.get_string("animal")
    #animal = "black"
    if animal == "random":
        animal = "neko"
    with SysTrayIcon(
        os.path.join(
            files.get_project_root(), "resource", animal, "Awake.ico",
        ),
        animal,
        set(),
        on_quit=lambda systray: quit(systray, root),
    ):
        timer(root, myPurr, fps)
        root.mainloop()
