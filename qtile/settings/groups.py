from .keys import keys, MOD
from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy


# unicode for nerd unifonts https://www.nerdfonts.com/cheat-sheet
NAMES = [
    "",  # 'Web', nf-fa-chrome
    "",  # 'Dev', nf-dev-code
    "",  # 'Term', nf-oct-terminal
    "",  # 'Auronix', nf-linux-archlinux
    "",  # 'DBas', nf-fa-database
    '󰑴', # 'Esc', nf-md-school
    "",  # 'Spotify', nf-fa-spotify
]

browsers = ["Chromium", "google-chrome", "firefox"]

groups = (
    [Group(NAMES[0], matches=[Match(wm_class=name) for name in browsers])]
    + [Group(NAMES[1], matches=[Match(wm_class="code")])]
    + [Group(current) for current in NAMES[2::]]
)


def group_position(name: str) -> str:
    global NAMES
    lower_names = [x.lower() for x in NAMES]
    position_ans = ""
    if name.lower() in lower_names:
        position_ans = str(lower_names.index(name.lower()) + 1)
    return position_ans


for current in groups:
    keys.extend(
        [
            Key(
                [MOD],
                group_position(current.name),
                lazy.group[current.name].toscreen(),
                desc="hack para cambiar al grupo dado por posiciones entre 1 y len(grupos)",
            ),
            Key(
                [MOD, "shift"],
                group_position(current.name),
                lazy.window.togroup(current.name, switch_group=True),
                desc="hack para mover una ventana al grupo en el rango de 1 y len(grupos)",
            ),
        ]
    )

keys.extend(
    [
        Key(
            [MOD],
            "Right",
            lazy.screen.next_group(),
            desc="cambiando al siguiente grupo a la derecha",
        ),
        Key(
            [MOD],
            "Left",
            lazy.screen.prev_group(),
            desc="cambiando al  grupo anterior a la izquierda",
        ),
    ]
)

