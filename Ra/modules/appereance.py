import os 


def set_wallpaper(path:str) -> int:

    try:
        os.system(
            f"hyprctl hyprpaper preload '{path}'"
        )
        os.system(
            f"hyprctl hyprpaper wallpaper ',{path}'"
        )
    except: 
        return -1 


