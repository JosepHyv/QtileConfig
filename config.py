from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.widget import battery

# my personalization
import os 
import subprocess
import keys as KeyConfig
import groups as GroupConfig
import mouse as MouseConfig
import wallpaper as wp
from libqtile import hook


@hook.subscribe.startup_once
def autostart() -> None:
    config_path = os.path.join(os.path.expanduser("~"), ".config","qtile", "autostart.sh")
    subprocess.call([config_path])
    

mod = KeyConfig.MOD
keys = KeyConfig.KEYS_CONFIG #including Keys and Groups


groups = GroupConfig.GROUPS

for current in groups:
    keys.extend(
        [
            Key(
                [mod], 
                GroupConfig.position(current.name), 
                lazy.group[current.name].toscreen(),
                desc="hack para cambiar al grupo dado por posiciones entre 1 y len(grupos)"
            ),
            Key(
                [mod, "shift"], 
                GroupConfig.position(current.name), 
                lazy.window.togroup(current.name, switch_group=True),
                desc="hack para mover una ventana al grupo en el rango de 1 y len(grupos)"
            )
        ]
    )

layout_conf = {
    'border_focus': "#5c1b6c",
    'border_normal' : "#5a565b",
    'border_ratio' : 1.2,
    'border_width': 2,
    'margin': 4
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [
    '#1d1f21',  # 0 - Fondo
    '#282a2e',  # 1 - Barra
    '#c5c8c6',  # 2 - Texto
    '#cc6666',  # 3 - Resaltado
]


widget_defaults = dict(
    font="Font JetBrains 5 free Solid",
    fontsize=12,
    padding=3,
    background=colors[0]
)


extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper=wp.today_wall(),#'/home/josephy/.config/qtile/fondos/arch-liinux-4k-t0.jpg',
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.TextBox(" "),
                widget.GroupBox(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Net(format="{down} ↓↑ {up}"),
                widget.TextBox("||"),
                widget.CPU(),
                widget.TextBox("||"),
               # widget.TextBox("default config", name="default"),
               # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.TextBox("||"),
                widget.Clock(format="%H:%M  %a-%d"),
                widget.TextBox("||"),
                widget.CurrentLayout(),
                widget.TextBox("  "),
            ],
            32,
            background=["#111111", "#222222"],
            opacity=0.7,
        ),
    ),
]

# Drag floating layouts.
mouse = MouseConfig.MOUSE_CONFIG

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "urgent"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
