import pyvista as pv
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as R
import time

# File paths
stl_file_1 = "Pyvista/femur.stl"
stl_file_2 = "Pyvista/tibia.stl"

# Load STL models
model1 = pv.read(stl_file_1)
model2 = pv.read(stl_file_2)

plotter = pv.Plotter()
plotter.add_mesh(model1, color="red", opacity=0.8)
plotter.add_mesh(model2, color="blue", opacity=0.8)
plotter.show()
