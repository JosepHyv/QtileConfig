# QtileConfig
My Qtile configuration for Linux.

My configuration uses the minimal packages of xfce, gnome, and kde possible. This config was designed for my primary workflow as a Junior Developer, Competitive Programmer, and Software Engineering Student. However, in my normal life, I love this config and use it too.

> layouts in config 
- bsp 
- max
- floating

I chose to use bsp because it is the fastest and most customizable layout available in qtile. Max and floating are used to optimize my workflow.
## Floating Windows
![floating](/images/floating.png)

## Bsp Window
![bsp](/images/bsp.png)



# Instalation

I created the config using Arch Linux, the scripts for dependencies use `pacman` and `yay`. If you use another Linux distro or package manager, you can find the equivalent package names for your package manager.

1. Clone this repo:
```zsh

git clone https://github.com/JosepHyv/QtileConfig.git

```

2. Change directory and run the requeriments:

```zsh
cd QtileConfig
./requeriments.sh

```

3. Run the installation script:
```zsh
./install.sh
```
**Note:** This script will copy all config files to your `${HOME}/.config` path and then check the integrity of the qtile config. **DO NOT RELOAD** the config if the script returns exit 1 with errors.

**Note 2:**  If the script says that mypy is missing, please install it by running `sudo pacman -S mypy` and then run the script again.

4. Reload the config by either rebooting or pressing `Super+Ctrl+r`
```zsh
# or if you want reboot 
reboot
```



## Systray 
The systray of the config was build with:
| package | use | start with |
| ------- | --- | ---------- |
| nm-applet | iis the GNOME network manager for WiFi and Ethernet connections | `nm-applet`  |
| volumeicon | is a lightweight volume control for system tray | `volumeicon` |
| blueman | is a GTK+ Bluetooth Manager | `blueman-applet` |
| clipit | is a lightweight GTK+ clipboard manager | `clipit` |
|kdeconnect | the KDE Connect utility in the systray | `/usr/bin/kdeconnect-indicator`  |


## proccess autostart
All processes in autostart run on start-up by qtile, executing the `autostart.sh` script. In this file, I launch the systray icons that I use and run some processes for my workflow. They are:

| process | description | 
| ------- | ----------- |
| `picom -b --config "$CONFIG_DIR/picom/picom.conf" &` | Run the picom compositor with my picom config. |
| `/usr/lib/pam_kwallet_init &` | Start the kwallet process and service for authentication, for example, for automatic WiFi connection with saved networks. |
|`/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & ` | Start polkit gnome auth agent. This is a utility for some apps that require you to enter a password (i.e., the input password dialog). |
|`light-locker &`| This is the service for LightDM. This service allows me to lock my screen. It is unnecessary if you are not using LightDM. |