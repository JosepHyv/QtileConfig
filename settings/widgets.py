#takings inspiration from here 
from libqtile import bar, widget
from settings.themes import colors

widget_defaults = dict(
    font="Nerd 5 free Solid",
    fontsize=12,
    padding=3,
    background=colors[0]
)


extension_defaults = widget_defaults.copy()