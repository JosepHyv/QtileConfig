import os
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
    Key([MOD], "i", lazy.layout.grow()),
    Key([MOD], "m", lazy.layout.shrink()),
    Key([MOD], "n", lazy.layout.normalize()),
    Key([MOD], "o", lazy.layout.maximize()),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([MOD, "shift"], "space", lazy.layout.flip()),

    # control de columnas y filas 
    Key([MOD, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([MOD, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MOD, Alt], "j", lazy.layout.flip_down()),
    Key([MOD, Alt], "k", lazy.layout.flip_up()),
    Key([MOD, Alt], "h", lazy.layout.flip_left()),
    Key([MOD, Alt], "l", lazy.layout.flip_right()),
    Key([MOD, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([MOD, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    

    #redimencionar las ventanas 
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="abre instancia de kitty terminal"),
    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="alterna las ventanas (maximizadas)"),
    Key([MOD], "w", lazy.window.kill(), desc="Mata ventana actual"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD], "q", lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))),
    Key([MOD, "control", Alt], "l", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([Alt], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),


    # Configuracion de rofi 

    Key([Alt], "space", lazy.spawn(os.path.expanduser('~/.config/rofi/rofi-run.sh'))),
    Key([Alt], "Tab", lazy.spawn("rofi -show window")),
    Key([MOD, Alt], "space", lazy.spawncmd()),

    #Control de volumne 
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    ## capturar pantalla 
     Key([], "Print", lazy.spawn("spectacle -s -b --fullscreen --copy-image")),
     Key([MOD], "Print", lazy.spawn("spectacle -s -b --fullscreen")),
     Key([Alt], "Print", lazy.spawn("spectacle -s -b -w --region --copy-image")),
     Key([MOD, Alt], "Print", lazy.spawn("spectacle -s -b --region")),      
     Key(['control'], "Print", lazy.spawn("spectacle -s -b --activewindow --copy-image")),       
     Key([MOD, 'control'], "Print", lazy.spawn("spectacle -s -b --activewindow")),       
     Key([MOD, Alt], "l", lazy.spawn("light-locker-command --lock")),

     ## ventanas flotantes 
     Key([MOD, "shift"], 'f', lazy.window.toggle_floating()),
     Key([MOD, "shift"], "s",lazy.layout.toggle_split()),
     Key([MOD], "p", lazy.widget["keyboardlayout"].next_keyboard()),

     ## My main apps workflow
     Key([MOD], "m", lazy.spawn('min --force-device-scale-factor=0.89')),
     Key([MOD], 'e', lazy.spawn('thunar')),
     Key([MOD], 't', lazy.spawn('com.todoist.Todoist')), 
     Key([MOD], 's', lazy.spawn('slack')),  
     Key([MOD], 'g', lazy.spawn('google-chrome-stable --force-device-scale-factor=0.89')),  
     Key([MOD], "x", lazy.spawn('chromium --force-device-scale-factor=0.89')),
     Key([MOD], 'c', lazy.spawn('code --new-window')),
]



