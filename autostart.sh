#!/usr/bin/sh

CONFIG_DIR="${HOME}/.config"

# start programs on login x11 session

echo "$CONFIG_DIR/picom/picom.conf"
nm-applet  &&
picom -b --config "$CONFIG_DIR/picom/picom.conf"
