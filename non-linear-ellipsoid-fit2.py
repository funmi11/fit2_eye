import numpy as np

from stl import mesh

fff = "Segmentation_right_eye.stl"

print("Reading from " , fff )

stl_data = mesh.Mesh.from_file(fff)

##  https://programming-surgeon.com/en/numpy-stl-2/

print(stl_data.points)


pts  = stl_data.points

print(pts.shape)

points = stl_data.points.reshape([-2, 4])

print(points.shape)

outfile = "eye_point_cloud"
np.save(outfile, points)

print('Point cloud saved to ', outfile + ".png")

