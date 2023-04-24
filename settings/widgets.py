#takings inspiration from here 
from libqtile import bar, widget
from .themes import colors

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
    background=colors[0]
)


def separator() : 
    return widget.Sep(linewidth = 0, padding = 4)

def workspaces():
    return [
        separator(), 
        widget.GroupBox(
            borderwidth=1,
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            this_current_screen_border=colors[4],
            disable_drag=True
        ),
        separator(),
        widget.WindowName()
    ]


PRIMARY_WIDGETS = [
    *workspaces(), 
    widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
    widget.Net(format="{down} ↓↑ {up}"),
    widget.TextBox(" | "),
    widget.CPU(),
    widget.TextBox(" | "),
    widget.KeyboardLayout(configured_keyboards=['us','es']),
    widget.TextBox(" | "),
    widget.Systray(),
    widget.TextBox(" | "),
    widget.Clock(format="%H:%M  %a-%d"),
    widget.TextBox(" | "),
    widget.CurrentLayout(),
    separator()
]

SECONDARY_WIDGETS = [
    *workspaces(), 
    separator(), 
    widget.Clock(format="%H:%M  %a-%d"),
    separator(),
    widget.CurrentLayoutIcon(scale=0.60),
    widget.CurrentLayout(padding=5),
]


extension_defaults = widget_defaults.copy()