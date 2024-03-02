import subprocess 

# Command to list Wi-Fi networks on Linux using nmcli.
list_networks_command = "nmcli device wifi list"
# Execute the command and capture the output.
output = subprocess.check_output(list_networks_command, shell=True, text=True)
# Print the output, all networks in range.
print(output)