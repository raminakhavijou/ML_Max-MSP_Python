from pythonosc import udp_client

def send_osc_data(values, server_ip, server_port):
    # Create a UDP client
    client = udp_client.SimpleUDPClient(server_ip, server_port)

    # Send an OSC message with the list of values
    client.send_message("/data", values)  # Use a default address like "/data"
    print(f"Sent OSC data: {values} to {server_ip}:{server_port}")

def read_data_from_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Assuming each line contains a value to send
                value = float(line.strip())
                data.append(value)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except ValueError:
        print(f"Error converting a line to a number in '{file_path}'. Make sure all lines contain valid numbers.")
    return data

# Example usage
file_path = '/Users/raminakhavijou/Documents/Python/ML/SOUNDSTALLATION2_ML.txt'  # Replace with the actual path to your text file
server_ip = "192.168.12.128"  # Replace with the actual server IP address
server_port = 7500  # Replace with the actual server port number

data_to_send = read_data_from_file(file_path)

# Send all data as a single OSC message without a specific message address
send_osc_data(data_to_send, server_ip, server_port)
