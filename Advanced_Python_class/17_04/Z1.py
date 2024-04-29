import numpy as np
import pylab

def draw_linear_function():
    x = np.arange(0,11)
    title = input("Please enter the title for the chart.")
    if_grid = input("Do you want to display the grid? Please enter 'y' for yes or 'n' for no.")

    a = float(input("Please enter the 'a' parameter."))
    b = float(input("Please enter the 'b' parameter."))

    list_of_y_values = []
    for x_element in x:
        y_element = a * x_element + b
        list_of_y_values.append(y_element)
    y = np.array(list_of_y_values)

    pylab.plot(x,y, color="red", linestyle="dashed")
    pylab.title(title)
    pylab.grid(if_grid)
    pylab.show()

draw_linear_function()