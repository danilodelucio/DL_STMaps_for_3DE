# --------------------------------------------------------------
#  DL STMAPS FOR 3DE
#  Version: v06
#  Author: Danilo de Lucio
#
#  Last Updated: December 19th, 2021
# --------------------------------------------------------------
#  USAGE:
#
#  Creates STMaps files for 3DEqualizer.
# --------------------------------------------------------------

import os
from time import sleep
from datetime import datetime
from tkinter import *
import shutil
import colorama
from colorama import Fore
colorama.init(autoreset=True)


welcome = f"{Fore.LIGHTYELLOW_EX}Welcome to DL STMaps for 3DE"
print(welcome)

version = "Dec 2021 | v06"
time_after = 3000
font_tk = ("Segoe UI", 9, "bold")

# GETTING THE CURRENT DIRECTORY
cwd_dir = os.getcwd()
print()
print(f"Your current location:\n{cwd_dir}")


def current_time():
    return datetime.now().time().strftime("[%H:%M:%S] - ")


def create_button():
    # GETTING THE PLATE RESOLUTION AND OVERSCAN VALUE
    resolution_x = entry_width.get()
    resolution_y = entry_height.get()
    overscan = entry_overscan.get()

    # VERIFYING VALUES
    verifying = [resolution_x, resolution_y, overscan]
    check = 0
    for i in verifying:
        if i.isnumeric():
            check += 1


    if check == 3:
        calc_x = int((int(resolution_x) * (int(overscan) / 100)) + int(resolution_x))
        calc_y = int((int(resolution_y) * (int(overscan) / 100)) + int(resolution_y))

        # CREATING THE FILES NAMES
        file1 = "STMap_" + str(resolution_x) + "x" + str(resolution_y) + ".exr"
        file2 = "STMap_" + str(calc_x) + "x" + str(calc_y) + ".exr"

        # CREATING STMAPS
        cmd_command = f'create_identity_uv_map.exe -out {file1} -size "{resolution_x + " " + resolution_y}"'
        os.system(cmd_command)
        cmd_command = f'create_identity_uv_map.exe -out {file2} -size "{str(calc_x) + " " + str(calc_y)}"'
        sleep(1)
        os.system(cmd_command)


        # MOVING STMAPS TO ANOTHER DIRECTORY
        new_path = entry_path.get()
        files = [file1, file2]

        if not os.path.exists(new_path):
            print()
            print(f"{Fore.LIGHTGREEN_EX}{current_time()}The STMaps have been created!")

        if os.path.exists(new_path):
            for i in files:
                old_path = cwd_dir + fr"\{i}"

                shutil.move(old_path, new_path)

            print()
            print(f"{Fore.LIGHTGREEN_EX}{current_time()}The STMaps have been created and moved!")

        elif new_path == "":
            pass

        if new_path != "" and not os.path.exists(new_path):
            print(f"{Fore.LIGHTRED_EX}The following path doesn't exist!\n-> {new_path}")

    else:
        print()
        print(f"{Fore.LIGHTRED_EX}{current_time()}You must fill all fields (Width / Height / Overscan), with an Integer value!")



##### FRONT END ####
root = Tk()
root.geometry("600x300")
root.iconbitmap(r".\img\ICON.ico")
root.resizable(False, False)
root.title(f"DL STMaps for 3DE")

# BG
bg_image = PhotoImage(file=r".\img\GUI.png")
Label(root, image=bg_image).place(relwidth=1, relheight=1)

# Width Entry
entry_width = Entry(root, relief="flat", width=12)
entry_width.place(relx=0.516, rely=0.323)
entry_width.focus()

# Height Entry
entry_height = Entry(root, relief="flat", width=12)
entry_height.place(relx=0.672, rely=0.323)

# Overscan Entry
entry_overscan = Entry(root, relief="flat", width=12)
entry_overscan.place(relx=0.825, rely=0.323)

# New Path
entry_path = Entry(root, relief="flat", width=43)
entry_path.place(relx=0.515, rely=0.492)

# Create Button
button_create = Button(root,
                       text="CREATE",
                       relief="flat",
                       font=font_tk,
                       bg="#3a3a3a",
                       fg="white",
                       activebackground="#ce7a00",
                       activeforeground="white",
                       borderwidth=0,
                       width=37,
                       height=1,
                       command=create_button)
button_create.place(relx=0.513, rely=0.62)

# Version Label
label_version = Label(root, text=f"{version}", fg="black", bg="#d9d9d9", font=("Arial", 7, "italic"))
label_version.place(relx=0.88, rely=0.857)

root.mainloop()