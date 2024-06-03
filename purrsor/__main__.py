import os

import ctypes
import tkinter as tk
from infi.systray import SysTrayIcon

from purrsor import purr
from purrsor.utils import files, configs

GWL_EXSTYLE = -20
WS_EX_TOOLWINDOW = 0x80

print('WELCOME TO PURRSOR')

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


print(f'{string}')

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
