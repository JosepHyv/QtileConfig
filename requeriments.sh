#!/usr/bin/sh

echo "installing pacman packages"
sudo pacman -S network-manager-applet \
	ttf-jetbrains-mono-nerd \
	papirus-icon-theme \
	brightnessctl \
	volumeicon \
	dunst \
	cbatticon \
	blueman \
	pulseaudio-bluetooth #this is only for support to bluetooth audio devices
	
	

echo "installing AUR packages"
yay -S picom-ibhagwan-git \
	clipit
