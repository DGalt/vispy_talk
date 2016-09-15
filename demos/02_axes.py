# -*- coding: utf-8 -*-
# vispy: gallery 30
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
"""
Demonstrate ViewBox using various clipping methods.
"""
import sys
import numpy as np

from vispy import app
from vispy import scene


# Create canvas
canvas = scene.SceneCanvas(size=(800, 600), show=True, 
                           keys='interactive', 
                           bgcolor='white')
grid = canvas.central_widget.add_grid()

# Create ViewBoxes
vb = grid.add_view()

# ViewBox uses a 2D pan/zoom camera
vb.camera = 'panzoom'

# Load data
# needs to be shape (..., 2) or (..., 3)
data = np.load('./tseries.npy').astype(np.float32).T

#xaxis = scene.AxisWidget(orientation='bottom',
#                         text_color='black', 
#                         axis_color='gray')
#xaxis.height_max = 50
#grid.add_widget(xaxis, row=1, col=1)
#
#yaxis = scene.AxisWidget(orientation='left',
#                         text_color='black', 
#                         axis_color='gray')
#yaxis.width_max = 50
#grid.add_widget(yaxis, row=0, col=0)

# make a single plot line and display in both viewboxes
line = scene.Line(data, color='blue', parent=vb.scene)

#dots = scene.Markers(pos=data, symbol='disc', 
#                     edge_color='blue', face_color='blue',
#                     parent=vb.scene)

#xaxis.link_view(vb)
#yaxis.link_view(vb)

vb.camera.set_range()



if __name__ == '__main__' and sys.flags.interactive == 0:
    #print(canvas.scene.describe_tree(with_transform=True))
    app.run()