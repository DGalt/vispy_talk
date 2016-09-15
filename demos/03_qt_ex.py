import sys
from PyQt4 import QtGui
from vispy import scene
import numpy as np

class ExPlot(QtGui.QWidget):
    def __init__(self):
        super(ExPlot, self).__init__()
        layout = QtGui.QVBoxLayout(self)
        self.resize(600, 600)
        
        canvas = scene.SceneCanvas(size=(600, 600), show=True, 
                           keys='interactive', bgcolor='white')
                                         
        grid = canvas.central_widget.add_grid(margin=10)
        grid.spacing = 0
        
        grid_upper = grid.add_grid()
        grid_lower = grid.add_grid()
        
        yaxis1 = scene.AxisWidget(orientation='left',
                                  axis_color='gray',
                                  text_color='black')
        yaxis1.width_max = 40
        grid_upper.add_widget(yaxis1, row=0, col=0)
        
        xaxis1 = scene.AxisWidget(orientation='bottom',
                                  axis_color='gray',
                                  text_color='black')
        xaxis1.height_max = 40
        grid_upper.add_widget(xaxis1, row=1, col=1)
        
        yaxis2 = scene.AxisWidget(orientation='left',
                                  axis_color='gray',
                                  text_color='black')
        yaxis2.width_max = 40
        grid_lower.add_widget(yaxis2, row=0, col=0)
        
        xaxis2 = scene.AxisWidget(orientation='bottom',
                                  axis_color='gray',
                                  text_color='black')
        xaxis2.height_max = 40
        grid_lower.add_widget(xaxis2, row=1, col=1)
        
        grid.add_widget(grid_upper, row=0, col=0, row_span=1, col_span=2)
        grid.add_widget(grid_lower, row=1, col=0, row_span=1, col_span=2)
        
        x = np.arange(0.0, 2.0, 0.01)
        y1 = np.sin(2*np.pi*x)
        y2 = np.cos(2*np.pi*x)
        
        vb1 = grid_upper.add_view(row=0, col=1)
        plot1 = scene.LinePlot(np.array([x, y1]).T, parent=vb1.scene,
                               symbol='disc', face_color='blue', edge_color='blue')
        vb1.camera = 'panzoom'
        xaxis1.link_view(vb1)
        yaxis1.link_view(vb1)
        
        vb2 = grid_lower.add_view(row=0, col=1)
        plot2 = scene.LinePlot(np.array([x, y2]).T, parent=vb2.scene,
                               symbol='disc', face_color='red', edge_color='red')
        vb2.camera = 'panzoom'
        xaxis2.link_view(vb2)
        yaxis2.link_view(vb2)
        
        vb2.camera.link(vb1.camera)
        vb1.camera.set_range()
        
        button = QtGui.QPushButton('Auto Scale')
        button.clicked.connect(lambda: self.auto_scale(vb1))
        
        layout.addWidget(canvas.native)
        layout.addWidget(button)
        
    def auto_scale(self, vb):
        vb.camera.set_range()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ExPlot()
    ex.show()
    sys.exit(app.exec_())
        
