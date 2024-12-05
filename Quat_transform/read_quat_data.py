import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt

# Read the CSV file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df


sequence = 'xyz'
# sequence = 'zyx'
# sequence = 'yxz'
# sequence = 'zxy'
# sequence = 'xzy'
# sequence = 'yzx'


# Convert quaternions to Euler angles from iphone data
def quaternions_to_euler_from_iphone(df):
    quaternions = df[['x', 'y', 'z', 'w']].values
    rotations = R.from_quat(quaternions)
    euler_angles = rotations.as_euler(sequence, degrees=True) # iphone uses 'yxz' sequence
    print(euler_angles)
    return euler_angles

# Convert quaternions to Euler angles from Polhemus data
def quaternions_to_euler_from_polhemus(df):
    # quaternions = df[['w2', 'x2', 'y2', 'z2']].values # incorrect for scipy
    quaternions = df[['x2', 'y2', 'z2', 'w2']].values
    # quaternions = df[['x1', 'y1', 'z1', 'w1']].values

    rotations = R.from_quat(quaternions)
    euler_angles = rotations.as_euler(sequence, degrees=True)
    return euler_angles

# Plot the Euler angles
def plot_euler_angles(euler_angles):
    time = np.arange(euler_angles.shape[0])  # Assuming each row is a time step
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    
    axs[0].plot(time, euler_angles[:, 0], label=sequence[0].upper())
    axs[0].legend()

    axs[1].plot(time, euler_angles[:, 1], label=sequence[1].upper())
    axs[1].legend()

    axs[2].plot(time, euler_angles[:, 2], label=sequence[2].upper())
    axs[2].legend()

    plt.tight_layout()
    plt.show()

# Main function to execute the steps
def main(file_path):
    df = read_csv(file_path)
    # euler_angles = quaternions_to_euler_from_iphone(df)
    euler_angles = quaternions_to_euler_from_polhemus(df)
    plot_euler_angles(euler_angles)

# Replace 'quaternions.csv' with the path to your CSV file
file_path = 'Quat_transform/testdata.csv'
main(file_path)
