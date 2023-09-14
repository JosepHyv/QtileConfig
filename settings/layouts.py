from .groups import NAMES
from libqtile import layout
from libqtile.config import Match, Rule

LAYOUT_CONFIG = {
    'border_focus': "#a524e2",
    'border_normal' : "#5a565b",
}

MARGINS_AND_BORDERS = {
    'border_width': 2,
    'single_border_width'  : 2, 
    'single_margin' : 5, 
    'margin' : 5
}

LAYOUT_FLOATING = {
    'border_focus': "#a524e2",
    'border_normal' : "#5a565b",
    'border_width': 2,
}

layouts = [
    # layout.MonadTall(**LAYOUT_CONFIG,
    # border_width = 2,
    # single_border_width  = 2,
    # single_margin = 5,
    # margin = 7),
    layout.Bsp(**LAYOUT_CONFIG, **MARGINS_AND_BORDERS, ratio=1.8),
    layout.Max(),
    
]

floating_layout = layout.Floating(
    **LAYOUT_FLOATING,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='kdenlive'),
    ],
) 

# match xprop | grep -i WM_CLASS
floating_apps = ['min', 'kitty', 'flipper', 'code', 'thunar', 'slack', 'pavucontrol', 'blueman-applet']

dgroups_app_rules = [ 
    Rule(
        match=[Match(wm_class=current) for current in floating_apps],
        float=True,
        intrusive=False

    )
]
#     Rule(
#         match=[Match(wm_class='min')],
#         float=True,
#         intrusive=True
#     ),
#     Rule(
#         match=[Match(wm_class='kitty')],
#         float=True,
#         intrusive=True
#     )        
# ]
