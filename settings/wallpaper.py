import os 
import random 

WALLPAPER_PATH = os.path.join(os.path.expanduser("~"), ".config", "qtile", "fondos")

WALL_LIST = [str(x) for x in os.listdir(WALLPAPER_PATH) if ".jpeg" in x or ".jpg" in x]


def today_wall() -> str:
    global WALL_LIST, WALLPAPER_PATH
    number = random.randint(0, len(WALL_LIST) + 1)
    number = number % len(WALL_LIST)
    return os.path.join(WALLPAPER_PATH, WALL_LIST[number])

def select_wall(name : str):
    global WALL_LIST, WALLPAPER_PATH
    lower_list = [x.lower() for x in WALL_LIST]
    name = name.lower()
    number = 0 if (not name in lower_list) else lower_list.index(name)
    return os.path.join(WALLPAPER_PATH, WALL_LIST[number])    
