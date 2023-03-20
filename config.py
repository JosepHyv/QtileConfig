from libqtile import bar,widget
from libqtile.config import Screen

# my personalization
import os 
import subprocess
import settings.keys as KeyConfig
import settings.mouse as MouseConfig
import settings.layouts as LayoutsConfig 
import settings.themes as ThemesConfig
import settings.wallpaper as wp
from libqtile import hook


@hook.subscribe.startup_once
def autostart() -> None:
    config_path = os.path.join(os.path.expanduser("~"), ".config","qtile", "autostart.sh")
    subprocess.call([config_path])
    

keys = KeyConfig.KEYS_CONFIG #including Keys and Groups
layouts = LayoutsConfig.LAYOUTS
floating_layout = LayoutsConfig.FLOATING
colors = ThemesConfig.colors
mouse = MouseConfig.MOUSE_CONFIG # Drag floating layouts.



widget_defaults = dict(
    font="Nerd 5 free Solid",
    fontsize=12,
    padding=3,
    background=colors[0]
)


extension_defaults = widget_defaults.copy()

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
