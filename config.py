from libqtile import bar,widget
from libqtile.config import Screen
from libqtile.lazy import lazy

# my personalization
# extra libs for autostart
import os 
import subprocess
from libqtile import hook, qtile

# main keywords config 
from settings.keys import keys
from settings.mouse import mouse
from settings.layouts import layouts, floating_layout, dgroups_app_rules
from settings.groups import groups
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens


@hook.subscribe.startup_once
def autostart() -> None:
    config_path = os.path.join(os.path.expanduser("~"), ".config","qtile", "autostart.sh")
    subprocess.call([config_path])
    
@hook.subscribe.client_focus
def floating_windows(c):
    if c.floating:
        c.cmd_bring_to_front()



dgroups_key_binder = None
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
floats_kepts_above = False

# @hook.subscribe.screen_change
# def unlock_on_resume(qtile, ev):
    # if ev.state == "off":
        # qtile.cmd_spawn("xfce4-screensaver-command -d")

# Configuramos el salvapantallas para que no se inicie automáticamente
screensaver = {
    "idle_activation_enabled": False,
    "lock_on_suspend": True,
    "lock_on_lid": False,
    "lock_on_logout": False,
    "lock_after_blank_screen": True,
    "lock_delay": 0,
    "mode": "blank-only",
}
