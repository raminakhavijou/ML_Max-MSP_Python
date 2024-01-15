import socket
import struct

# UDP configuration
UDP_IP = "192.168.12.128"
UDP_PORT = 7400

# Specify the file path where you want to store the data
FILE_PATH = "SOUNDSTALLATION_ML.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

with open(FILE_PATH, "w") as file:
    while True:
        try:
            data, addr = sock.recvfrom(1024)

            # Remove null bytes from the received data
            cleaned_data = data.replace(b'\x00', b'').decode('utf-8').strip()

            # Print the cleaned data
            print(f"Received cleaned data: {cleaned_data}")

            # Remove commas from the cleaned data
            cleaned_data_without_commas = cleaned_data.replace(',', '')

            # Write the cleaned data without commas to the file
            file.write(f"{cleaned_data_without_commas}\n")

            # Flush the file to ensure data is written immediately
            file.flush()

            try:
                string_value = cleaned_data_without_commas
                print(f"Received string value: {string_value}")

            except UnicodeDecodeError:
                # If decoding fails, treat the data as an integer
                try:
                    # Unpack the received data as a 32-bit integer in little-endian format
                    integer_value = struct.unpack('<I', data[:4])[0]
                    print(f"Received integer value: {integer_value}")

                except struct.error as se:
                    print(f"Error decoding data: {se}")

        except Exception as e:
            print(f"Unexpected error: {e}")
