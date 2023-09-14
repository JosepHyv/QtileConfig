#!/usr/bin/sh



# TODO

# make instalation rutine 

CONFIG_DIR="${HOME}/.config"

LOCAL_DIR=`pwd`

UNDESEBALE_DIRS=("$LOCAL_DIR/settings/.mypy_cache", "$LOCAL_DIR/settings/__pycache__")

if ! [[ -d $UNDESEABLE_DIRS[0] ]]; then 
	rm -rvf $UNDESEABLE_DIRS[0]
fi 
if [ -d $UNDESEBALE_DIRS[1] ]; then
	echo Eliminando el el directorio $UNDESEBALE_DIRS[1] 
	rm -rvf $UNDESEBALE_DIRS[1]
fi 

cp -rv  battery.py config.py autostart.sh fondos settings "$CONFIG_DIR/qtile/."



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

