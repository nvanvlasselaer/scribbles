import pandas as pd
import matplotlib.pyplot as plt

# Function to read the CSV file and plot the data
def plot_pitch_roll_yaw(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    
    # Extract pitch, roll, and yaw columns
    pitch = data['pitch']
    roll = data['roll']
    yaw = data['yaw']
    
    # Create a time index if not present
    time = data.index if 'time' not in data.columns else data['time']
    
    # Plotting
    plt.figure(figsize=(12, 6))

    plt.subplot(3, 1, 1)
    plt.plot(time, pitch, label='Pitch')
    plt.xlabel('Time')
    plt.ylabel('Pitch')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(time, roll, label='Roll', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Roll')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(time, yaw, label='Yaw', color='green')
    plt.xlabel('Time')
    plt.ylabel('Yaw')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Replace 'your_file.csv' with the path to your CSV file
csv_file = '/Users/nicolas/Github/nvanvlasselaer/scribbles/DATA/quaternion_data-random.csv'
plot_pitch_roll_yaw(csv_file)
