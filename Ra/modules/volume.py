import os 

def view_status():
    print(sp.getoutput("pamixer --get-volume-human"))

def increase_by(percentage = 5):
    os.system(f"pamixer -i {percentage}")

def deccrease_by(percentage = 5):
    os.system(f"pamixer -d {percentage}")

def set_at(percentage = 5):
    os.system(f"pamixer --set-volume {percentage}")

def deafen():
    os.system(f"pamixer -t")

def mute():
    os.system(f"pamixer --default-source -t ")

increase_by()