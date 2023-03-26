#!/usr/bin/sh

CONFIG_DIR="${HOME}/.config"

# start programs on login x11 session

nm-applet & 
picom -b --config "$CONFIG_DIR/picom/picom.conf" &
volumeicon &
cbatticon -u 5 &
blueman-applet &
# start kwallet for auth
/usr/lib/pam_kwallet_init &
clipit &
ksmserver  &
