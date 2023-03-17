from .keys import keys, MOD
from libqtile.config import Group, Key
from libqtile.lazy import lazy

NAMES = [
    'Web',
    'Term',
    'Dev',
    'Auronix',
    'DBas',
    'Esc',
    'Spotify', 
    "   ", "   "
]

groups = [Group(current) for current in NAMES]

def position(name : str ) -> str:
    global NAMES
    lower_names = [x.lower() for x in NAMES]
    position_ans = "" 
    if name.lower() in lower_names:
        position_ans = str(lower_names.index(name.lower()) + 1 )
    return position_ans

for current in groups:
    keys.extend(
                [
                    Key(
                        [MOD], 
                        position(current.name), 
                        lazy.group[current.name].toscreen(),
                        desc="hack para cambiar al grupo dado por posiciones entre 1 y len(grupos)"
                    ),
                    Key(
                        [MOD, "shift"], 
                        position(current.name), 
                        lazy.window.togroup(current.name, switch_group=True),
                        desc="hack para mover una ventana al grupo en el rango de 1 y len(grupos)"
                    )
                ]
            )



 