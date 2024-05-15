import os 
import subprocess as sp 


def view_status(*args):
    try:
        return sp.getoutput("pamixer --get-volume-human --set-limit 100")
    except: 
        return -1

def increase_by(percentage = 5):
    try:
        os.system(f"pamixer -i {percentage} --set-limit 100")
    except: 
        return -1

def decrease_by(percentage = 5):
    try:
        os.system(f"pamixer -d {percentage} --set-limit 100")
    except: 
        return -1

def set_at(data:dict = None):
    try:
        os.system(f"pamixer --set-volume {data.get('args',50)} --set-limit 100")
    except: 
        return -1

def deafen(*args):
    try:
        os.system(f"pamixer -t")
    except: 
        return -1

def mute(*args):
    try:
        os.system(f"pamixer --default-source -t ")
    except: 
        return -1