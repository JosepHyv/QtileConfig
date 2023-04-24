import subprocess 
from libqtile import bar
from libqtile.config import Screen
from .wallpaper import today_wall, select_wall
from .widgets import PRIMARY_WIDGETS, SECONDARY_WIDGETS



def gen_bar(_widgets, size=30):
    return bar.Bar(
        _widgets,
        size,
        background=["#111111", "#222222"],
        opacity=0.7
    )

screens = [
    Screen(
        wallpaper=select_wall('darkest-hour1.jpg'),
        wallpaper_mode="stretch",
        top=gen_bar(PRIMARY_WIDGETS)
    ),
]


xrandr_command = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr_command, 
    shell = True, 
     stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

connected_screens = 1 # es la pantalla de mi lap :p 

if  not command.returncode:
    connected_screens = int(command.stdout.decode("UTF-8"))

if connected_screens > 1:
    for _ in range (1, connected_screens):
        screens.append(Screen(
                wallpaper=today_wall(),
                wallpaper_mode="stretch",
                top=gen_bar(SECONDARY_WIDGETS, 22)))

    screen_config = "xrandr --output eDP-1 --primary --mode 1920x1080 --pos 1366x0 --rotate normal --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --mode 1366x768 --pos 0x0 --rotate normal"
    subprocess.run(screen_config, shell=True)

