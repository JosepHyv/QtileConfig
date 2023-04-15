from libqtile import bar 
from libqtile import widget
from libqtile.config import Screen
from .wallpaper import today_wall, select_wall
import subprocess 

MY_BAR_CONFIG = {
    "background" : ["#111111", "#222222"],
    "opacity" : 0.7,
}

def gen_bar(widgets, bar_configs):
    return bar.Bar(widgets,30, **bar_configs)

screens = [
    Screen(
        wallpaper=select_wall('darkest-hour1.jpg'),
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.TextBox(" "),
                widget.GroupBox(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Net(format="{down} ↓↑ {up}"),
                widget.TextBox("||"),
                widget.CPU(),
                widget.TextBox("||"),
                widget.KeyboardLayout(configured_keyboards=['us','es']),
                widget.TextBox("||"),
                widget.Systray(),
                widget.TextBox("||"),
                widget.Clock(format="%H:%M  %a-%d"),
                widget.TextBox("||"),
                widget.CurrentLayout(),
                widget.TextBox("  "),
            ],
            32,
            background=["#111111", "#222222"],
            opacity=0.7,
        ),
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
                wallpaper_mode="stretch"))

