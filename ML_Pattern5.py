import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Specify the file path where the data is stored
FILE_PATH = "SOUNDSTALLATION_ML.txt"  # Replace with your file path
OUTPUT_FILE_PATH = "SOUNDSTALLATION2_ML.txt"  # New file path

# Define a simple recurrent neural network (RNN) model
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        _, h_n = self.rnn(x)
        output = self.fc(h_n[-1, :, :])
        return output

def read_sequence_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        sequence = [float(line.strip()) for line in lines]
        return sequence
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except ValueError:
        print("Error converting data to numbers.")
        return None

def predict_next_numbers(sequence, predict_length=3):
    # Convert the sequence to a PyTorch tensor
    sequence_tensor = torch.FloatTensor(sequence).view(1, -1, 1)

    # Initialize the RNN model
    input_size = 1
    hidden_size = 32
    output_size = 1
    model = RNN(input_size, hidden_size, output_size)

    # Set up the loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # Training the RNN on the given sequence
    for epoch in range(1000):
        optimizer.zero_grad()
        output = model(sequence_tensor)
        loss = criterion(output, sequence_tensor)
        loss.backward()
        optimizer.step()

    # Predict the next numbers in the sequence
    with torch.no_grad():
        future_sequence = sequence_tensor[:, -1:, :].clone()
        for _ in range(predict_length):
            future_output = model(future_sequence)
            future_sequence = torch.cat((future_sequence, future_output.unsqueeze(1)), dim=1)

    predicted_numbers = future_sequence[0, -predict_length:, 0].tolist()
    return predicted_numbers

def save_to_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            for value in data:
                file.write(str(value) + "\n")
        print(f"Data saved to {file_path}")
    except IOError:
        print(f"Error saving data to {file_path}")

def main():
    # Read the sequence from the file
    sequence = read_sequence_from_file(FILE_PATH)

    if sequence:
        print("Extracted Sequence:", sequence)

        # Predict the next numbers in the sequence #combining with the original list
        predicted_numbers = predict_next_numbers(sequence, predict_length=3)
        combined_sequence = sequence + predicted_numbers
        print("Predicted Next Numbers:", combined_sequence)

        # Save the combined sequence to a new file
        save_to_file(OUTPUT_FILE_PATH, combined_sequence)

    else:
        print("Unable to read the sequence from the file.")

if __name__ == "__main__":
    main()
