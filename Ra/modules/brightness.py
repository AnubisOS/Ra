import os 
import subprocess as sp
import shlex
from math import ceil

MAX = 255

path = "/sys/class/backlight" 

vega = [ os.path.join(path,card) for card in os.listdir(path) ]


def view_brightness():
    with open(os.path.join(vega[0], "brightness"), 'r') as f :
        value = ceil((int(f.read()) / MAX) * 100)
    return value    

def set_brightness(value=100):
    with open(os.path.join(vega[0], "brightness"), 'w') as f :
        f.write(str(value))
    return value    

def increase_brightness(increment = 5):
    pre_value = view_brightness()
    value = (pre_value + increment) * 2.55
    set_brightness(ceil(value))

def decrease_brightness(decrement = 5):
    pre_value = view_brightness()
    value = (pre_value - decrement ) * 2.55
    set_brightness(ceil(value))

def toggle_night_mode():
    cmd = "wlsunset"
    if sp.getoutput(f"pidof {cmd}") != ""  :
        os.system(f"kill $(pgrep {cmd})")
        return "OFF"
    cmds = shlex.split(cmd)
    p = sp.Popen(cmds, start_new_session=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)
    return "ON"


toggle_night_mode()