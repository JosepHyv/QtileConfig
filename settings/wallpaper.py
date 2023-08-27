import os 
import random 
from string import ascii_lowercase

WALLPAPER_PATH = os.path.join(os.path.expanduser("~"), ".config", "qtile", "fondos")

WALL_LIST = [str(x) for x in os.listdir(WALLPAPER_PATH) if ".jpeg" in x or ".jpg" in x]


def today_wall() -> str:
    global WALL_LIST, WALLPAPER_PATH
    number = random.randint(0, len(WALL_LIST) + 1)
    number = number % len(WALL_LIST)
    return os.path.join(WALLPAPER_PATH, WALL_LIST[number])

def normalize_str(name:str):
    return "".join([str(x) for x in name if x in ascii_lowercase])

def wall_position(name : str):
    name = normalize_str(name.lower())
    for file in WALL_LIST:
        lower_file = normalize_str(file.lower())
        if name in lower_file:
            return WALL_LIST.index(file)
    return -1
        

def select_wall(name : str):
    name = name.lower()
    number = wall_position(name)
    if number == -1:
        number = 0
    return os.path.join(WALLPAPER_PATH, WALL_LIST[number])    
