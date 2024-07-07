#
# SaphireOS (v1.0) ApplePie
# made by DDavid701 [ 2024 ]
#
import os
import threading
import time

import requests
from customtkinter import *
from PIL import ImageTk, Image
from distro import id
from platform import system
version = 'applepie-1.0-2024'

GEOMETRY_WIDTH  = 1000
GEOMETRY_HEIGHT = 650


PLATFORM = system()
if PLATFORM == 'Linux':
    DISTRO = id()
    if DISTRO == 'saphire_debian':
        OVERRIDE = True
        TITLE = 'saphire_os_gui'
    else:
        TITLE    = 'Saphire Indev'
        OVERRIDE = False
else:
    raise SystemError(f"project can't run on {PLATFORM}")
print(PLATFORM)


def _load_sys():
    prog(0.05)
    sound = 'mplayer'
    prog(0.1)
    req = requests.get('https://pastebin.com/raw/isMUskNF')
    prog(0.15)
    latest = req.text
    prog(0.2)
    if latest == version:
        print('Up to date!')
    else:
        print('Outdated!')
        #update(latest)
    prog(0.25)
    time.sleep(0.3)
    prog(0.67)
    os.system('python3 application/main.py')
    prog(1)
    time.sleep(0.25)
    main()

def prog(int):
    boot_progress.set(int)

def _load_saphire():
    global placeholder, bootlogo, boot_progress
    win.title(TITLE)
    win.geometry(f'{GEOMETRY_WIDTH}x{GEOMETRY_HEIGHT}')
    win.overrideredirect(OVERRIDE)
    win.resizable(FALSE, FALSE)
    iconpath = ImageTk.PhotoImage(file=os.path.join("logo.png"))
    win.wm_iconbitmap()
    win.iconphoto(True, str(iconpath))
    bootlogo_img = CTkImage(dark_image=Image.open('logo.png'), size=(128,128))

    placeholder = CTkLabel(master=win, text="")
    placeholder.pack(pady=80)

    bootlogo = CTkLabel(master=win, image=bootlogo_img, text="")
    bootlogo.pack()

    boot_progress = CTkProgressBar(master=win, progress_color='gray28', fg_color='gray16', width=260, determinate_speed=0.2, corner_radius=0)
    boot_progress.pack(pady=60)
    boot_progress.set(.0)

    smain_thrd = threading.Thread(target=_load_sys).start()


def main():

    placeholder.pack_forget()
    bootlogo.pack_forget()
    boot_progress.pack_forget()

    button = CTkButton(win, text="Das ist der main Button")
    button.pack()

win = CTk(fg_color='gray8')

load = threading.Thread(target=_load_saphire).run()

win.mainloop()