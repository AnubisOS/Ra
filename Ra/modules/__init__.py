from .battery import *
from .brightness import * 
from .volume import *  
from .appereance import * 

func = {
    # Battery
    'battery_percentage' : view_battery_percantage,
    'battery_status' : view_battery_status,
    
    # Display
    'set_brightness': set_brightness,
    'get_brightness': view_brightness,
    'night_mode': toggle_night_mode,

    # Volume
    'get_status': view_status,
    'set_volume': set_at,
    'mute': mute,
    'deafen':deafen,

    # appereance 
    'set_wallpaper': set_wallpaper
}

