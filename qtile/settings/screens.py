import os
import subprocess
from libqtile import bar
from libqtile.config import Screen
from .wallpaper import today_wall, select_wall
from .widgets import PRIMARY_WIDGETS, SECONDARY_WIDGETS
from .themes import colors


PRIMARY_WALL: str = f"{os.getenv("PRIMARY_SCREEN_WALLPAPER")}"
SECONDARY_WALL: str = f"{os.getenv("SECONDARY_SCREEN_WALLPAPER")}"


def gen_bar(_widgets, size=27):
    return bar.Bar(
        _widgets,
        size,
        background=colors[0],
        opacity=0.7,
        widget_shadow=True,
    )


current_config = [
    Screen(
        wallpaper=select_wall("almso"),
        wallpaper_mode="stretch",
        top=gen_bar(PRIMARY_WIDGETS),
    ),
]


xrandr_command = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr_command,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

connected_screens = 1  # es la pantalla de mi lap :p

if not command.returncode:
    connected_screens = int(command.stdout.decode("UTF-8"))


for _ in range(1, connected_screens):
    current_config.append(
        Screen(
            wallpaper=select_wall("rasikraj"),
            wallpaper_mode="stretch",
            top=gen_bar(SECONDARY_WIDGETS, 27),
        )
    )

# if connected_screens > 1:
#     screen_config = "xrandr --output eDP-1 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --primary --mode 1920x1080 --pos 0x0 --rotate normal"
#     for _ in range(1, connected_screens):
#         current_config.append(
#             Screen(
#                 wallpaper=select_wall("ravi"),
#                 wallpaper_mode="stretch",
#                 top=gen_bar(SECONDARY_WIDGETS, 27),
#             )
#         )
#         subprocess.Popen(screen_config, shell=True, stdout=subprocess.PIPE)
# else:
#     laptop = "xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --off"
#     subprocess.Popen(laptop, shell=True, stdout=subprocess.PIPE)


screens = current_config
