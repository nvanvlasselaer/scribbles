import pyvista as pv
from pyvistaqt import BackgroundPlotter
import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as R

def quaternion_to_rotation_matrix(quaternion):
    quat = np.roll(quaternion, -1)  # Rearrange quaternion components as x, y, z, w for scipy
    r = R.from_quat(quat)
    rotation_matrix = r.as_matrix()
    return rotation_matrix

def build_homogeneous_matrix(R, locx, locy, locz):
    T = np.matrix([[R[0, 0], R[0, 1], R[0, 2], locx],
                   [R[1, 0], R[1, 1], R[1, 2], locy],
                   [R[2, 0], R[2, 1], R[2, 2], locz],
                   [0, 0, 0, 1]])
    return T

def change_mesh_origin(mesh, new_origin):
    """
    Translate the mesh so that its new origin aligns with the specified coordinates.

    Args:
        mesh (pyvista.PolyData): The input mesh.
        new_origin (tuple): The desired origin as (x, y, z).
    """
    # Compute the current origin (e.g., center of the bounding box)
    current_origin = mesh.center

    # Compute the translation vector
    translation_vector = np.array(new_origin) - np.array(current_origin)

    # Translate the mesh
    mesh.translate(translation_vector, inplace=True)

def update_scene(p, mesh1, mesh2, T1, T2, frame_idx):
    # Reset meshes to original state before applying transformations
    mesh1_copy = mesh1.copy()
    mesh2_copy = mesh2.copy()

    # Apply the current frame's transformations
    mesh1_copy.transform(T1[frame_idx])
    mesh2_copy.transform(T2[frame_idx])

    # Clear and re-add the transformed meshes
    p.clear()
    p.add_mesh(mesh1_copy, color="red", name='femur', opacity=0.5)
    p.add_mesh(mesh2_copy, color="blue", name='tibia', opacity=0.5)

if __name__ == '__main__':
    # Load the meshes
    mesh_1 = "Pyvista/femur.stl"
    mesh1 = pv.read(mesh_1)
    mesh_2 = "Pyvista/tibia.stl"
    mesh2 = pv.read(mesh_2)

    # Change the origins of the meshes
    change_mesh_origin(mesh1, (0, 0, 0))  # Example new origin for femur
    change_mesh_origin(mesh2, (-7, 0, 0))  # Example new origin for tibia

    # Create the plotter
    p = BackgroundPlotter(window_size=(800, 600))

    # Load the motion data
    csv_file = "Pyvista/1_90deg_ydata_oneway.csv"
    motion_data = pd.read_csv(csv_file)

    # Extract quaternions and translations
    quaternions1 = motion_data[["w1", "x1", "y1", "z1"]].values
    translations1 = motion_data[["loc1_x", "loc1_y", "loc1_z"]].values
    quaternions2 = motion_data[["w2", "x2", "y2", "z2"]].values
    translations2 = motion_data[["loc2_x", "loc2_y", "loc2_z"]].values

    # Compute rotation matrices and homogeneous transformations
    T1 = [build_homogeneous_matrix(quaternion_to_rotation_matrix(q), *t) for q, t in zip(quaternions1, translations1)]
    T2 = [build_homogeneous_matrix(quaternion_to_rotation_matrix(q), *t) for q, t in zip(quaternions2, translations2)]

    # Add initial meshes
    p.add_mesh(mesh1, color="red", name='femur')
    p.add_mesh(mesh2, color="blue", name='tibia')

    # Animation variables
    frame_idx = [0]  # Use a mutable container

    def animate():
        frame_idx[0] = (frame_idx[0] + 1) % len(T1)  # Update the frame index
        update_scene(p, mesh1, mesh2, T1, T2, frame_idx[0])

    # Add animation callback
    p.add_callback(animate, interval=1000 // 120)  # 120 Hz animation speed

    # Show the plotter
    p.show()
    p.app.exec_()
