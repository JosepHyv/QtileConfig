from libqtile.config import Group

NAMES = [
    'Web',
    'Term',
    'Dev',
    'Auronix',
    'DBas',
    'Esc',
    'Spotify'
]

GROUPS = [Group(current) for current in NAMES]

def position(name : str ) -> str:
    global NAMES
    lower_names = [x.lower() for x in NAMES]
    position_ans = "" 
    if name.lower() in lower_names:
        position_ans = str(lower_names.index(name.lower()) + 1 )
    return position_ans


 