#!/usr/bin/sh

echo "installing pacman packages"
sudo pacman -Syu network-manager-applet \
	ttf-jetbrains-mono-nerd \
	papirus-icon-theme \
	brightnessctl \
	volumeicon \
	dunst \
	cbatticon \
	blueman \
	pulseaudio-bluetooth \
	light-locker lightdm-webkit2-greeter \
	polkit-gnome
	
	
echo "installing AUR packages"
yay -S picom-ibhagwan-git \
	clipit 


# pulse audio bluetooth this is only for support to bluetooth audio devices
# light-locker only if you use lightdm  please read https://wiki.archlinux.org/title/List_of_applications/Security#Screen_lockers and https://wiki.archlinux.org/title/LightDM for information about TTY access (security hole)

# lightdm-webkit2-greeter  this is only if you use lightdm
