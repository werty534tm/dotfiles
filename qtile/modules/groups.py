import re
from libqtile.config import Group, Match

groups = [
    Group(name, **kwargs)
    for name, kwargs in [
        (" ", {}),
        (" ", {"matches": [Match(wm_class=re.compile(r"^(firefox)$"))]}),
        (" ", {"matches": [Match(wm_class=re.compile(r"^(Apache NetBeans IDE 16)$")), Match(wm_class=re.compile(r"^(jetbrains\-pycharm\-ce)$"))]}),
        (" ", {}),
        (" ", {}),
        (" ", {}),
        (" ", {"matches": [Match(wm_class=re.compile(r"^(steam)$"))]}),
        (" ", {"matches": [Match(wm_class=re.compile(r"^(spotify)$"))]}),
        (" ", {"matches": [Match(wm_class=re.compile(r"^(mpv)$"))]}),
        (" ", {"matches": [Match(wm_class=re.compile(r"^(discord)$"))]}),
    ]
]
