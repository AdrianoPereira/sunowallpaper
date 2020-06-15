import os
import re
import sys
import subprocess as sp
from distutils.version import LooseVersion


def set_background(file_path):
    if 'linux' not in sys.platform:
        print('Platform no supported yet...', type(sys.platform))
        sys.exit(1)

    interface = os.environ.get("DESKTOP_SESSION")

    if interface in ['ubuntu', 'unity']:
        sp.call(["gsettings", "set", "org.gnome.desktop.background",
                 "draw-background", "false"])
        sp.call(["gsettings", "set", "org.gnome.desktop.background",
                 "picture-uri", "file://" + file_path])
        sp.call(["gsettings", "set", "org.gnome.desktop.background",
                 "picture-options", "scaled"])
        sp.call(["gsettings", "set", "org.gnome.desktop.background",
                 "primary-color", "#000000"])
    else:
        print('Platform no supported yet...', type(sys.platform))
        sys.exit(1)
    return True

if __name__ == "__main__":
    set_background('')
    # print(sys.platform)
