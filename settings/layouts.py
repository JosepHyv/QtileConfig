from libqtile import layout
from libqtile.config import Match

LAYOUT_CONFIG = {
    'border_focus': "#a524e2",
    'border_normal' : "#5a565b",
    'border_ratio' : 1.2,
    'border_width': 2,
    "border_rounding" : 10,
    'margin': 4
}


layouts = [
    layout.Bsp(**LAYOUT_CONFIG),
    layout.Max(),
    ### if i neeed i can unmark this amazing layouts

    # layout.MonadWide(**LAYOUT_CONFIG),
    # layout.RatioTile(**LAYOUT_CONFIG),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
]

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