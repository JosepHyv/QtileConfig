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
from settings.layouts import layouts, floating_layout
from settings.groups import groups
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
import settings.wallpaper as wp


@hook.subscribe.startup_once
def autostart() -> None:
    config_path = os.path.join(os.path.expanduser("~"), ".config","qtile", "autostart.sh")
    subprocess.call([config_path])
    

# Hacer que las ventanas flotantes vengan automáticamente al frente
@hook.subscribe.client_focus
def bring_floating_to_front(c):
    if c.floating:
        c.cmd_bring_to_front()

# Hacer que las ventanas no flotantes se envíen automáticamente al fondo o al frente
@hook.subscribe.focus_change
def focus_change_callback(c):
    group = c.group
    if not c.floating:
        for w in group.windows:
            if w != c and w.floating:
                if (
                    w.x <= c.x <= w.x + w.width and
                    w.y <= c.y <= w.y + w.height
                ):
                    c.cmd_lower()
                    break
                else:
                    c.cmd_bring_to_front()
                    break
            elif (
                group.current_window != c and not group.current_window.floating and
                c != w and not w.floating
            ):
                c.cmd_bring_to_front()
    elif c.floating:
        for w in group.windows:
            if w != c and not w.floating:
                w.cmd_lower()




dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"


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
