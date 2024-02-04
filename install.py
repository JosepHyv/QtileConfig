#!/usr/bin/python

import os
import shutil
import math
from zipfile import ZipFile
from typing import List
from shlex import split
from libqtile import qtile
from subprocess import run, PIPE
from datetime import datetime

HOME = os.path.expanduser("~")

CONFIG_DIR = os.path.join(HOME, ".config")
LOCAL_DIR = os.getcwd()
LOCAL_QTILE = os.path.join(LOCAL_DIR, "qtile")

IGNORE_DIRS = [os.path.join(LOCAL_QTILE, "fondos")]

ELEMENTS = [
    "dunst",
    "gtk-3.0",
    "gtk-4.0",
    "kitty",
    "picom",
    "rofi",
    "qtile",
]

INSTALLS = [(os.path.join(LOCAL_DIR, x), os.path.join(CONFIG_DIR, x)) for x in ELEMENTS]
BACKUP = [os.path.join(CONFIG_DIR, x) for x in ELEMENTS]


def ask_continue(message="Dou you want to continue with installation?"):
    print(message)
    print("[Y/yes, N/no]")
    choise = input().lower()
    if "y" == choise[0]:
        return True
    return False


def backup(origin: List[str], create: bool):
    BACK_DIR = os.path.join(HOME, ".qtile_backup")
    exist = False
    if not os.path.exists(BACK_DIR):
        print("{} does not exist, creating....".format(BACK_DIR))
        try:
            os.mkdir(path=BACK_DIR)
            exist = True
        except Exception as e:
            print("Cant Create {} directory\n{}".format(BACK_DIR, str(e)))
    else:
        exist = True

    create = ask_continue("Dou you want create a backup of current config?")

    if exist:
        if create:
            print("Creating Backup of current configuration")
            curr_date = datetime.utcnow()
            name = "backup-{}.zip".format(math.ceil(datetime.timestamp(curr_date)))
            name = os.path.join(BACK_DIR, name)

            command = ["zip", name, "-r", "-9"]
            for curr in origin:
                print(5 * "-", "append to compress {}".format(curr))
                command.append(curr)

            print("Starting Compression using UNIX zip")
            output = run(args=command, stderr=PIPE)
            if output.stderr:
                print("Error Creating Backup :(")
                print("An error happend in compression process")
                print(output.stderr)
            else:
                print("Backup Finished in {}".format(name))
        else:
            print("WARNING BACKUP IS DISABLED")
    else:
        print("WARNING CANT CREATE BACKUP")
    return ask_continue()


# process start


def install(create_backup: bool = True):
    can_install = backup(BACKUP, create_backup)
    if can_install:
        print("Installing")
        for element in INSTALLS:
            print(6 * "-", element)
            shutil.copytree(element[0], element[1], dirs_exist_ok=True)
            # os.path.(element[0], element[1])

        print("Installation Finished")
        print("Starting integrity check")

        command = split("qtile check")
        output = run(args=command, stderr=PIPE)
        if output.stderr:
            print(
                "Error in integrity test, dont reload qtile, please revert your backup."
            )
            print(output.stderr)
    print("Finish")


install(create_backup=False)
