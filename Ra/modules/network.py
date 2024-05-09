import subprocess 
import re

# Command to list Wi-Fi networks on Linux using nmcli.
list_networks_command = "nmcli device wifi list"
# Execute the command and capture the output.
output = subprocess.check_output(list_networks_command, shell=True, text=True)

# Print the output, all networks in range.
x = output.splitlines(keepends=False)[1].split()

if x[0] == '*':
    print("active")