import os
from libqtile.lazy import lazy
from libqtile.config import Key


MOD = "mod4"
Alt = "mod1"
TERMINAL = "kitty"

keys = [
    # cambio entre ventanas (solo el foco de ventanas)
    Key([MOD], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "k", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "i", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [MOD],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Full Screen in Window",
    ),
    Key(
        [MOD],
        "b",
        lazy.hide_show_bar(),
        desc="Full Screen in Window",
    ),
    Key(
        [MOD, "shift"],
        "j",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [MOD, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD, Alt], "k", lazy.layout.flip_down()),
    Key([MOD, Alt], "i", lazy.layout.flip_up()),
    Key([MOD, Alt], "j", lazy.layout.flip_left()),
    Key([MOD, Alt], "l", lazy.layout.flip_right()),
    Key(
        [MOD, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key(
        [MOD, "control"],
        "j",
        lazy.layout.grow_left(),
        desc="Grow window to the right",
    ),
    Key([MOD, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([MOD], "w", lazy.window.kill(), desc="Mata ventana actual"),
    Key([MOD], "Tab", lazy.next_layout(), desc="alterna las ventanas (maximizadas)"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key(
        [MOD, "shift"],
        "q",
        lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu.sh")),
    ),
    Key([MOD, "control", Alt], "l", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([Alt], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ## capturar pantalla
    Key([], "Print", lazy.spawn("flameshot gui -c")),
    Key([MOD], "Print", lazy.spawn("flameshot screen -c")),
    Key([Alt], "Print", lazy.spawn("flameshot screen")),
    Key([MOD, "control"], "Print", lazy.spawn("spectacle -s -b --activewindow")),
    Key([MOD, "shift"], "f", lazy.window.toggle_floating()),
    Key([MOD, "shift"], "s", lazy.layout.toggle_split()),
    Key([MOD], "p", lazy.widget["keyboardlayout"].next_keyboard()),
    Key([MOD, Alt], "p", lazy.spawn("arandr")),
    Key([Alt], "space", lazy.spawn(os.path.expanduser("~/.config/rofi/rofi-run.sh"))),
    Key([Alt], "Tab", lazy.spawn("rofi -show window")),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="abre instancia de kitty terminal"),
    Key([MOD], "e", lazy.spawn("thunar")),
    Key([MOD], "t", lazy.spawn("com.todoist.Todoist")),
    Key([MOD], "s", lazy.spawn("slack")),
    Key(
        [MOD], "g", lazy.spawn("google-chrome-stable --force-device-scale-factor=0.89")
    ),
    Key([MOD], "x", lazy.spawn("chromium --force-device-scale-factor=0.89")),
    Key([MOD], "c", lazy.spawn("code --new-window")),
]
