#!/usr/bin/sh



# TODO

# make instalation rutine 

CONFIG_DIR="${HOME}/.config"


cp -rv  config.py autostart.sh fondos settings "$CONFIG_DIR/qtile/."

echo "Copying picom config"
if [ -d "$CONFIG_DIR/picom" ]; then 
	cp -rv picom/* "$CONFIG_DIR/picom/."
else 
	cp -rv picom $CONFIG_DIR
fi 


echo "Coppyng kitty config"
if [ -d "$CONFIG_DIR/kitty" ]; then 
	cp -rv kitty/* "$CONFIG_DIR/kitty/."	
else 
	cp -rv kitty $CONFIG_DIR
fi 

echo "Coppyng dunst config"
if [ -d "$CONFIG_DIR/dunst" ]; then 
	cp -rv dunst/* "$CONFIG_DIR/dunst/."	
else 
	cp -rv dunst $CONFIG_DIR
fi 

echo "Coppyng rofi config"
if [ -d "$CONFIG_DIR/rofi" ]; then 
	cp -rv rofi/* "$CONFIG_DIR/rofi/."	
else 
	cp -rv rofi $CONFIG_DIR
fi 


echo ""
echo ""

echo "run qtile test"
qtile check

