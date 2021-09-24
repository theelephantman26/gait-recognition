import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

def scrollable_plotter(x, y):
    Plot, Axis = plt.subplots()
    
    # Adjust the bottom size according to the
    # requirement of the user
    plt.subplots_adjust(bottom=0.25)

    l = plt.plot(x, y)
    slider_color = 'White'
    axis_position = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor = slider_color)
    slider_position = Slider(axis_position, "Pos", 0.1, 90.0)

    def update(val):
        pos = slider_position.val
        Axis.axis([pos, pos+10, -1, 1])
        Plot.canvas.draw_idle()
    
    # update function called using on_changed() function
    slider_position.on_changed(update)
    
    # Display the plot
    plt.show()