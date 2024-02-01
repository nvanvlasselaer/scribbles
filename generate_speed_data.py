import csv
import matplotlib.pyplot as plt
import numpy as np

# Define parameters
distance = 10000  # meters
initial_speed = 8  # m/s
final_speed = 6  # m/s
plateau_distance = 6000  # meters
plateau_speed = 12  # m/s
noise_amplitude = 1.5  # Maximum amplitude of the random noise

# Generate speed values
speeds = []
distances = []
for i in range(distance // 100):
    distance_m = (i + 1) * 100
    if distance_m < plateau_distance:
        speed = initial_speed + (plateau_speed - initial_speed) * (1 - np.cos(2 * np.pi * distance_m / plateau_distance)) / 2
    else:
        speed = final_speed + (plateau_speed - final_speed) * (1 - np.cos(2 * np.pi * (distance_m - plateau_distance) / (distance - plateau_distance))) / 2
    speed += np.random.uniform(-noise_amplitude, noise_amplitude)  # Add random noise
    speed = max(0, min(speed, plateau_speed))  # Ensure speed is within bounds
    speeds.append(round(speed,2))
    distances.append(distance_m)

# Generate CSV file
with open('DATA/running_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Distance (m)', 'Speed (m/s)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, (distance_m, speed) in enumerate(zip(distances, speeds)):
        writer.writerow({'Distance (m)': distance_m, 'Speed (m/s)': speed})

# Plot the data
plt.plot(distances, speeds)
plt.title('Speed Variation During the Run')
plt.xlabel('Distance (m)')
plt.ylabel('Speed (m/s)')
plt.grid(True)
plt.savefig('DATA/running_speed_variation.png')  # Save the plot as an image
plt.show()