from netmiko import ConnectHandler
import datetime

# Cisco switch details
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",  # Replace with your switch's IP address
    "username": "admin",  # Replace with your username
    "password": "password",  # Replace with your password
    "secret": "password",  # Replace with your enable password
}


def backup_cisco_config(device):
    try:
        # Connect to the device
        connection = ConnectHandler(**device)
        connection.enable()

        # Get the running configuration
        running_config = connection.send_command("show running-config")

        # Save the config to a file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"cisco_config_backup_{device['host']}_{timestamp}.txt"

        with open(filename, "w") as file:
            file.write(running_config)

        print(f"Configuration backup saved to {filename}")

        # Disconnect
        connection.disconnect()

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the backup function
backup_cisco_config(device)
