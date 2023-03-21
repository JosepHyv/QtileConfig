from libqtile.config import Key 
from libqtile.lazy import lazy 

# Mi config 


MOD = "mod4"
Alt = "mod1"
TERMINAL = "kitty"

keys = [
    #cambio entre ventanas (solo el foco de ventanas)
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # control de columnas y filas 
    Key([MOD, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([MOD, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    #redimencionar las ventanas 
    Key([MOD, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([MOD, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [MOD, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="abre instancia de kitty terminal"),
    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="alterna las ventanas (maximizadas)"),
    Key([MOD], "w", lazy.window.kill(), desc="Mata ventana actual"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, "control", Alt], "l", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([Alt], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),


    # Configuracion de rofi 

    Key([Alt], "space", lazy.spawn("rofi -show run")),
    Key([MOD, Alt], "space", lazy.spawncmd()),

    #Control de volumne 
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    ## capturar pantalla 
     Key([], "Print", lazy.spawn("scrot -s -e 'xclip -selection clipboard -t image/png $f && mv $f ~/screenshots/'")),
     Key([MOD, Alt], "l", lazy.spawn("xfce4-screensaver-command -l")),

     ## ventanas flotantes 
     Key([MOD, "shift"], 'f', lazy.window.toggle_floating()),

     ## Mover ventanas (rotando)
     Key([MOD, "shift"], "space", lazy.layout.rotate()),

    Key([MOD, "shift"], "s",lazy.layout.toggle_split()),
    
]

