import os
import random
from string import ascii_lowercase

SUPPORTED = ["jpg", "jpeg", "png"]

WALLPAPER_PATH = os.path.join(os.path.expanduser("~"), ".config", "qtile", "fondos")

WALL_LIST = [
    str(x) for x in os.listdir(WALLPAPER_PATH) if x.lower().split(".")[-1] in SUPPORTED
]


def today_wall() -> str:
    return os.path.join(WALLPAPER_PATH, random.choice(WALL_LIST))


def normalize_str(name: str):
    name = name.lower()
    return "".join([str(x) for x in name if x in ascii_lowercase])


def wall_position(name: str):
    name = normalize_str(name)
    for i, file in enumerate(WALL_LIST):
        lower_file = normalize_str(file.lower())
        if name in lower_file:
            return i
    return -1


def select_wall(name: str):
    name = name.lower()
    number = wall_position(name)
    if number == -1:
        number = 0
    return os.path.join(WALLPAPER_PATH, WALL_LIST[number])
