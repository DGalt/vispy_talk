import numpy as np
from vispy import plot as vp

fig = vp.Fig(size=(600, 500), show=False)

x = np.arange(0.0, 2.0, 0.01)
y1 = np.sin(2*np.pi*x)
y2 = np.cos(2*np.pi*x)

plot1 = fig[0, 0].plot(np.array([x, y1]).T, width=1, color='k', symbol='o')
plot2 = fig[1, 0].plot(np.array([x, y2]).T, width=1, color='k', symbol='o')

fig.plot_widgets[0].camera.link(fig.plot_widgets[1].camera)


if __name__ == '__main__':
    fig.show(run=True)
