# takings inspiration from here
from libqtile import bar, widget
from .themes import colors
from qtile_extras import widget as widex

widget_defaults = dict(
    font="JetBrainsMono Nerd Font", fontsize=13, padding=3, background=colors[0]
)


def separator():
    icons = ["", "󰇝", "󱋱"]
    # nf-cod-chevron_left, nf-md-drag_vertical, nf-md-drag_vertical_variant
    return widget.TextBox(
        text=icons[1], fontsize=24, padding=5, opacity=0.3, foreground=colors[5]
    )


def workspaces(_fontsize=widget_defaults["fontsize"], _font=widget_defaults["font"]):
    return [
        widget.GroupBox(
            rounded=True,
            highlight_method="block",
            urgent_alert_method="block",
            this_current_screen_border=colors[4],
            disable_drag=True,
            font=_font,
            fontsize=_fontsize,
            foreground=colors[6],
            inactive=colors[5],
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            center_aligned=True,
        ),
    ]


PRIMARY_WIDGETS = [
    *workspaces(15, "Symbols Nerd Font Mono"),
    widget.TextBox(" "),
    widget.WindowName(padding=3, markup=False, format="{name}"),
    # widex.GlobalMenu(),
    widget.Memory(format="󰓅 {MemUsed: .0f}{mm}"),
    separator(),
    widget.CPU(format=" {load_percent}%"),
    separator(),
    widget.KeyboardLayout(configured_keyboards=["us", "latam"]),
    separator(),
    widget.Volume(fmt="󰕾 {} ", volume_app="pavucontrol"),
    widget.Battery(
        update_interval=0.3,
        unknow_char="",
        empty_char="",
        charge_char="",
        full_char="",
        show_short_text=False,
        low_percentage=0.20,
        notify_below=0.21,
        discharge_char="",
        format="{char} {percent:1.0%}",
    ),
    widget.Systray(),
    # widget.StatusNotifier(),
    separator(),
    widget.Clock(format=" %H:%M %a-%d"),
    separator(),
    widget.CurrentLayoutIcon(scale=0.50),
    widget.CurrentLayout(),
]

SECONDARY_WIDGETS = [
    *workspaces(15, "Symbols Nerd Font Mono"),
    widget.TextBox(" ", width=bar.STRETCH),
    widget.Clock(format=" %H:%M %a-%d"),
    widget.TextBox(" ", width=bar.STRETCH),
    widget.CurrentLayoutIcon(scale=0.50),
    widget.CurrentLayout(),
]


extension_defaults = widget_defaults.copy()
