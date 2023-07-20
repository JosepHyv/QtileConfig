#!/usr/bin/sh

echo "installing pacman packages"
sudo pacman -Syu \
  network-manager-applet \
  ttf-jetbrains-mono-nerd \
  papirus-icon-theme \
  brightnessctl \
  volumeicon \
  dunst \
  cbatticon \
  blueman \
  pulseaudio-bluetooth \
  light-locker \
  lightdm-webkit2-greeter \
  polkit-gnome \
  pavucontrol \
  noto-fonts 


sudo pacman -Syu $(pacman -Ssq nerd-fonts)


echo "installing AUR packages"
yay -S \
    picom-ibhagwan-git \
	clipit 


# pulse audio bluetooth this is only for support to bluetooth audio devices
# light-locker only if you use lightdm  please read https://wiki.archlinux.org/title/List_of_applications/Security#Screen_lockers and https://wiki.archlinux.org/title/LightDM for information about TTY access (security hole)

# lightdm-webkit2-greeter  this is only if you use lightdm


# xfce packages that i have installed using only qtile 

# extra/thunar-volman 4.18.0-1 (131.5 KiB 672.7 KiB) [xfce4] (Instalado)
# extra/exo 4.18.0-1 (319.9 KiB 2.2 MiB) [xfce4] (Instalado)
# extra/ristretto 0.13.1-1 (250.5 KiB 1.0 MiB) [xfce4-goodies] (Instalado)
# extra/libxfce4util 4.18.1-1 (135.1 KiB 974.7 KiB) (Instalado)
# extra/thunar-archive-plugin 0.5.1-1 (43.0 KiB 174.3 KiB) [xfce4-goodies] (Instalado)
# extra/thunar-media-tags-plugin 0.4.0-1 (67.8 KiB 311.7 KiB) [xfce4-goodies] (Instalado)
# extra/libxfce4ui 4.18.3-1 (383.4 KiB 2.2 MiB) (Instalado)
# extra/tumbler 4.18.1-1 (166.3 KiB 882.6 KiB) [xfce4] (Instalado)
# extra/thunar 4.18.6-1 (1.5 MiB 8.6 MiB) [xfce4] (Instalado)
# extra/garcon 4.18.1-1 (166.7 KiB 1.2 MiB) [xfce4] (Instalado)
# extra/xfce4-battery-plugin 1.1.5-1 (101.8 KiB 476.3 KiB) [xfce4-goodies] (Instalado)
# extra/xfce4-settings 4.18.2-1 (891.2 KiB 4.6 MiB) [xfce4] (Instalado)
# extra/xfce4-panel 4.18.3-1 (786.5 KiB 4.1 MiB) [xfce4] (Instalado)
# extra/xfconf 4.18.1-1 (184.1 KiB 1.1 MiB) [xfce4] (Instalado)
