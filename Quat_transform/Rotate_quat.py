import numpy as np
import pandas as pd
import math
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt

def sandwich_quaternion(quaternion, q_rotate):

    r1 = R.from_quat(quaternion)
    r2 = R.from_quat(q_rotate)
    r = r2 * r1 * r2.inv()
    return r.as_quat()

def rotate_quaternion_other_quat(quaternion1, quaternion2):

    r1 = R.from_quat(quaternion1)
    r2 = R.from_quat(quaternion2)
    r = r1 * r2 
    return r.as_quat()

def rotate_quaternion_with_inv_quat(quaternion, q_rotate):

    r1 = R.from_quat(quaternion)
    r2 = R.from_quat(q_rotate)
    r = r1 * r2.inv() # Rotate from the orientation of r2 to the orientation of r1
    # r = r2.inv() * r1 # Represent r1 relative to the frame of r2
    return r.as_quat()

def quaternions_to_euler(quaternions):
    rotations = R.from_quat(quaternions)
    euler_angles = rotations.as_euler(sequence, degrees=True)
    return euler_angles

# file_path = 'Quat_transform/4_90deg_y_with_xxdeg_z_rotationdata.csv'
# file_path = '/Users/nicolas/Github/nvanvlasselaer/Knee-kinematics/Data/2-Rsnapshot.csv'
file_path = 'Quat_transform/testdata.csv'
# file_path = 'DATA/rotated_quaternions.csv'
# file_path = 'Quat_transform/1_90deg_ydata.csv'

# q_rotate = R.from_euler('XYZ', [0, 0, 180], degrees=True).as_quat()
q_rotate = (0, 0, 1, 0)
# sqrt2_over_2 = math.sqrt(2) / 2
# q_rotate = (0, 0, sqrt2_over_2, sqrt2_over_2)

# sequence = 'ZYX'
# sequence = 'XYZ'
# sequence = 'XZY'
# sequence = 'ZXY'
# sequence = 'YZX'
sequence = 'YXZ'


# Read the CSV file
data = pd.read_csv(file_path)

Time = data['Time'].values
time2 = data['time2'].values

# Extract quaternions for sensor 1 and sensor 2
quaternions_1 = data[['x1', 'y1', 'z1', 'w1']].to_numpy()
quaternions_2 = data[['x2', 'y2', 'z2', 'w2']].to_numpy()

euler_angles_1 = quaternions_to_euler(quaternions_1)
euler_angles_2 = quaternions_to_euler(quaternions_2)

rotated_quaternion_1 = []

for quaternion in quaternions_1:

    rotated_quaternion_1_row = rotate_quaternion_other_quat(quaternion, q_rotate)
    rotated_quaternion_1_row = sandwich_quaternion(rotated_quaternion_1_row, q_rotate)
    rotated_quaternion_1.append(rotated_quaternion_1_row)

# Convert rotated_quaternion_1 to a NumPy array
rotated_quaternion_1 = np.array(rotated_quaternion_1)

rotated_quaternion_2 = []

for quaternion in quaternions_2:

    rotated_quaternion_2_row = rotate_quaternion_other_quat(quaternion, q_rotate)
    rotated_quaternion_2_row = sandwich_quaternion(rotated_quaternion_2_row, q_rotate)
    rotated_quaternion_2.append(rotated_quaternion_2_row)

# Convert rotated_quaternion_2 to a NumPy array
rotated_quaternion_2 = np.array(rotated_quaternion_2)

transformed_euler_angles_1 = quaternions_to_euler(rotated_quaternion_1)
transformed_euler_angles_2 = quaternions_to_euler(rotated_quaternion_2)



# Plot the Euler angles
time = np.arange(euler_angles_1.shape[0])  # Assuming each row is a time step
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axs[0].plot(time, euler_angles_1[:, 0], label=sequence[0].upper())
axs[0].plot(time, transformed_euler_angles_1[:, 0], label='Transformed')
axs[0].legend()

axs[1].plot(time, euler_angles_1[:, 1], label=sequence[1].upper())
axs[1].plot(time, transformed_euler_angles_1[:, 1], label='Transformed')
axs[1].legend()

axs[2].plot(time, euler_angles_1[:, 2], label=sequence[2].upper())
axs[2].plot(time, transformed_euler_angles_1[:, 2], label='Transformed')
axs[2].legend()

axs[0].set_title('Sensor 1 Euler Angles')


# Sensor 2
time = np.arange(euler_angles_2.shape[0])  # Assuming each row is a time step
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axs[0].plot(time, euler_angles_2[:, 0], label=sequence[0].upper())
axs[0].plot(time, transformed_euler_angles_2[:, 0], label='Transformed')
axs[0].legend()

axs[1].plot(time, euler_angles_2[:, 1], label=sequence[1].upper())
axs[1].plot(time, transformed_euler_angles_2[:, 1], label='Transformed')
axs[1].legend()

axs[2].plot(time, euler_angles_2[:, 2], label=sequence[2].upper())
axs[2].plot(time, transformed_euler_angles_2[:, 2], label='Transformed')
axs[2].legend()


plt.tight_layout()
plt.show()


# Create a new DataFrame with transformed quaternions
transformed_data = pd.DataFrame({
    'Time': Time,
    'w1': rotated_quaternion_1[:, 3],
    'x1': rotated_quaternion_1[:, 0],
    'y1': rotated_quaternion_1[:, 1],
    'z1': rotated_quaternion_1[:, 2],
    'time2': time2,
    'w2': rotated_quaternion_1[:, 3],
    'x2': rotated_quaternion_1[:, 0],
    'y2': rotated_quaternion_1[:, 1],
    'z2': rotated_quaternion_1[:, 2]
})

# Save the transformed quaternions back to a CSV file
# output_path = 'DATA/transformed_quaternions.csv'
output_path = 'DATA/rotated_quaternions.csv'

# transformed_data.to_csv(output_path, index=False)
# print(f"Transformed quaternions saved to {output_path}")