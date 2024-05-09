import os 

path = "/sys/class/power_supply"

batteries = [ os.path.join(path, bat) for bat in os.listdir(path) if bat.startswith("BAT")]

def view_battery_percantage():
    with open(os.path.join(batteries[0], "capacity") ,'r') as bat : 
        value = int(bat.readline()) 
        print(f"{value}%")

def view_battery_status():
    with open(os.path.join(batteries[0], "status") ,'r') as bat : 
        print(bat.readline())

view_battery_percantage()
view_battery_status()