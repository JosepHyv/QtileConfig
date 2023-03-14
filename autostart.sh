
CONFIG_DIR="${HOME}/.config"

# start programs on login x11 session

nm-applet & picom -b --config "$CONFIG_DIR/picom/picom.conf"
