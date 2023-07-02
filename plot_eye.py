# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:03:56 2022

@author: peron
"""

import numpy as np
import pyvista as pv
#%%
grid = pv.PolyData('Segmentation_right_eye.stl')

plotter = pv.Plotter()

actor = plotter.add_mesh(grid)

actor = plotter.show_bounds(
    grid='front',
    location='outer',
    all_edges=True,
)

plotter.show()
