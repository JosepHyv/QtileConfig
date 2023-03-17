from libqtile import bar,widget
from libqtile.config import Screen

# my personalization
# extra libs for autostart
import os 
import subprocess
from libqtile import hook

# main keywords config 
from settings.keys import keys
from settings.mouse import mouse
from settings.layouts import layouts, floating_layout
from settings.groups import groups
from settings.widgets import widget_defaults, extension_defaults
import settings.wallpaper as wp


@hook.subscribe.startup_once
def autostart() -> None:
    config_path = os.path.join(os.path.expanduser("~"), ".config","qtile", "autostart.sh")
    subprocess.call([config_path])
    



screens = [
    Screen(
        wallpaper=wp.today_wall(),
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
               # widget.TextBox("default config", name="default"),
               # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
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


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
