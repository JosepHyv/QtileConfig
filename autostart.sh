#!/usr/bin/sh

CONFIG_DIR="${HOME}/.config"

# start programs on login x11 session

nm-applet & 
picom -b --config "$CONFIG_DIR/picom/picom.conf" &
volumeicon &
blueman-applet &
clipit &
/usr/bin/gnome-keyring-daemon &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & 
/usr/bin/kdeconnect-indicator & 
light-locker & 
"$CONFIG_DIR/qtile/./battery.py" &
