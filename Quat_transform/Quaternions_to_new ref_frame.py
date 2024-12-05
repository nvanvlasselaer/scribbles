import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt


def change_reference_frame(quaternions, q_rot):

    # Ensure q_CL is a unit quaternion
    r_rot = R.from_quat(q_rot)
    r_rot_inv = r_rot.inv()

    # Transform each quaternion
    transformed_quaternions = []
    for q in quaternions:
        r_global = R.from_quat(q)
        r_local = r_rot * r_global * r_rot_inv
        transformed_quaternions.append(r_local.as_quat())
    
    return np.array(transformed_quaternions)

def quaternions_to_euler(quaternions):
    rotation = R.from_quat(quaternions)
    euler_angles = rotation.as_euler(sequence, degrees=True)
    return euler_angles

# File path and headers
# file_path = 'Quat_transform/4_90deg_y_with_xxdeg_z_rotationdata.csv'
# file_path = '/Users/nicolas/Github/nvanvlasselaer/Knee-kinematics/Data/2-Rdata.csv'
# file_path = 'DATA/rotated_quaternions.csv'
# file_path = 'Quat_transform/testdata.csv'
file_path = 'Quat_transform/1_90deg_ydata.csv'

# sequence = 'ZYX'
# sequence = 'XYZ'
# sequence = 'XZY'
# sequence = 'ZXY'
# sequence = 'YZX'
sequence = 'YXZ'

# Read the CSV file
data = pd.read_csv(file_path)

# Extract quaternions for sensor 1 and sensor 2
quaternions_1 = data[['x1', 'y1', 'z1', 'w1']].to_numpy()
quaternions_2 = data[['x2', 'y2', 'z2', 'w2']].to_numpy()

euler_angles_1 = quaternions_to_euler(quaternions_1)
euler_angles_2 = quaternions_to_euler(quaternions_2)

Time = data['Time'].values
time2 = data['time2'].values

# Define the transformation quaternion q_CL
# This rotates the reference frame
# q_rot = R.from_euler('XZY', [180, -90, 0], degrees=True).as_quat()
# q_rot = R.from_euler('XYZ', [0, 0, 180], degrees=True).as_quat()
# q_rot = [-1, 1, 0, 0]
q_rot = [0, 0, 1, 0]

# Perform the transformation
transformed_quaternions_1 = change_reference_frame(quaternions_1, q_rot)
transformed_quaternions_2 = change_reference_frame(quaternions_2, q_rot)


transformed_euler_angles_1 = quaternions_to_euler(transformed_quaternions_1)
transformed_euler_angles_2 = quaternions_to_euler(transformed_quaternions_2)

# Create a new DataFrame with transformed quaternions
transformed_data = pd.DataFrame({
    'Time': Time,
    'w1': transformed_quaternions_1[:, 3],
    'x1': transformed_quaternions_1[:, 0],
    'y1': transformed_quaternions_1[:, 1],
    'z1': transformed_quaternions_1[:, 2],
    'time2': time2,
    'w2': transformed_quaternions_2[:, 3],
    'x2': transformed_quaternions_2[:, 0],
    'y2': transformed_quaternions_2[:, 1],
    'z2': transformed_quaternions_2[:, 2]
})

# ******** Save *******

# output_path = 'DATA/transformed_quaternions.csv'
# output_path = 'DATA/transformed_quaternions.csv'

# transformed_data.to_csv(output_path, index=False)
# print(f"Transformed quaternions saved to {output_path}")

# ***************



# ******** Plot ********

# Plot the Euler angles
# time = np.arange(euler_angles_1.shape[0])  # Assuming each row is a time step
# fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# axs[0].plot(time, euler_angles_1[:, 0], label=sequence[0].upper())
# axs[0].plot(time, transformed_euler_angles_1[:, 0], label='Transformed')
# axs[0].legend()

# axs[1].plot(time, euler_angles_1[:, 1], label=sequence[1].upper())
# axs[1].plot(time, transformed_euler_angles_1[:, 1], label='Transformed')
# axs[1].legend()

# axs[2].plot(time, euler_angles_1[:, 2], label=sequence[2].upper())
# axs[2].plot(time, transformed_euler_angles_1[:, 2], label='Transformed')
# axs[2].legend()

# axs[0].set_title('Sensor 1 Euler Angles')


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