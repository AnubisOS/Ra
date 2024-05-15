import os 

path = "/sys/class/power_supply"

batteries = [ os.path.join(path, bat) for bat in os.listdir(path) if bat.startswith("BAT")]

def view_battery_percantage(*args):
    try:
        with open(os.path.join(batteries[0], "capacity") ,'r') as bat : 
            value = int(bat.readline()) 
            return f"{value}%"
    except : 
        return -1 

def view_battery_status(*args):
    try: 
        with open(os.path.join(batteries[0], "status") ,'r') as bat : 
            return bat.readline()
    except : 
        return -1 