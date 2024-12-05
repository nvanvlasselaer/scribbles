import numpy as np
from scipy.spatial.transform import Rotation as R

def rotate_quaternion(global_quaternion, rotation_quaternion):
    """
    Rotates a quaternion from the global reference frame to a local reference frame.
    
    Parameters:
        global_quaternion (list or np.array): The input quaternion in [w, x, y, z] format.
        rotation_quaternion (list or np.array): The rotation quaternion in [w, x, y, z] format.
    
    Returns:
        np.array: The transformed quaternion in [w, x, y, z] format.
    """
    # Ensure inputs are numpy arrays
    global_quaternion = np.array(global_quaternion)
    rotation_quaternion = np.array(rotation_quaternion)
    
    # Convert to [x, y, z, w] format for multiplication
    global_xyzw = np.roll(global_quaternion, -1)
    rotation_xyzw = np.roll(rotation_quaternion, -1)
    
    # Create rotation objects
    rot_q = R.from_quat(rotation_xyzw)  # Rotation quaternion
    print('Rotation quaternion:', rot_q.as_euler('xyz', degrees=True))

    global_q = R.from_quat(global_xyzw)  # Global quaternion
    print('Global quaternion:', global_q.as_euler('xyz', degrees=True))
    
    # Apply rotation: q_local = q_rotate * q_global * q_rotate^-1
    rotated_q = rot_q * global_q * rot_q.inv()
    print('Rotated quaternion:', rotated_q.as_euler('xyz', degrees=True))

    # multiply_q = rot_q * global_q
    multiply_q = global_q * rot_q
    print('Multiplied quaternion:', multiply_q.as_euler('xyz', degrees=True))

    rotated_multiply_q = rot_q * multiply_q * rot_q.inv()
    print('Rotated multiplied quaternion:', rotated_multiply_q.as_euler('xyz', degrees=True))
    
    # Convert back to [w, x, y, z] format
    local_quaternion = np.roll(rotated_q.as_quat(), 1)
    return local_quaternion

# Example Usage:
if __name__ == "__main__":
    # Example input: quaternion in [w, x, y, z] format
    global_quaternion = [0.2, 0.5, 0.3, 1] 

    rotation_quaternion = [0, 0, 0, 1] 
    
    # Transform the quaternion
    local_quaternion = rotate_quaternion(global_quaternion, rotation_quaternion)
 
    
    # print("Global Quaternion:", global_quaternion)
    # print("Rotation Quaternion:", rotation_quaternion)
    # print("Local Quaternion:", local_quaternion)
