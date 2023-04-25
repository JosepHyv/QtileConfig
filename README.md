# QtileConfig
My Qtile config for linux

My configuration uses xfce, gnome and kde packages (the minimal packages possible), this config was designed for my primary workflow as JR developer, competitive Programmer and Software Engineer Student, however in my normal life, i love this config and i use too

> layouts in config 
- bsp 
- max
- floating

i decide for use bsp, because is the layout most faster and customizable available in qtile, and max and floating for uptimice my workflow
## Floating Windows
![floating](/images/floating.png)

## Bsp Window
![bsp](/images/bsp.png)



# Instalation

i make the config using arch linux, the scripts for dependencies are using `pacman` and `yay`, if you use another linux distro or package manager you can find the equivalents package names for you package manager.

1. Clone this repo
```zsh

git clone https://github.com/JosepHyv/QtileConfig.git

```

2. change directory and run the requeriments 

```zsh
cd QtileConfig
./requeriments.sh

```

3. run the installation script
```zsh
./install.sh
```
**Note:** this script will copy all config in yout `${HOME}/.config` path and then check the integrity of qtile config **DONT RELOAD** the config if the script return exit 1 with errors

**Note 2:** if the script say that mypy is missing please install it, you can doit with `sudo pacman -S mypy` and run it again

4. Reload the config, you can reboot or press `Super+Ctrl+r`
```zsh
# or if you want reboot 
reboot
```



## Systray 
The systray of the config was build with:
| package | use | start with |
| ------- | --- | ---------- |
| nm-applet | is the gnome network manager for wifi and ethernet connections | nm-applet  |
| volumeicon | is a lightweight volume control for system tray | volumeicon |
| blueman | is a GTK+ Bluetooth Manager | blueman-applet |
| clipit | is a lightweight GTK+ clipboard manager | clipit |
|kdeconnect | the kdeconnect utlitie in systray | /usr/bin/kdeconnect-indicator  |
