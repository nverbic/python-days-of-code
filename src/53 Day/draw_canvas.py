'''
    Day 53
    Create a program that allows users to draw on a canvas using a GUI
'''

import tkinter as tk

# Define function when mouse left click + dragging is enabled
def paint(e=""):
    ''' Free style drawing on the canvas '''
    prev_x, prev_y, x, y = (e.x), (e.y), (e.x+1), (e.y+1)

    # Specify type of display
    canvas.create_line(prev_x, prev_y, x, y, width=LINE_WIDTH, fill=COLOR,\
                            capstyle='round')

root = tk.Tk()

# Create Tttle
root.title( "Paint App")

# Specify size
root.minsize(650, 450)

# Create canvas widget
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="white")
canvas.pack(expand=True)

COLOR = "black" # Color of the shape
LINE_WIDTH = 6 # Width of the line shape

# Bind events to Canvas
# Capture Mouse left click + move (dragging)
canvas.bind("<B1-Motion>", paint)

# Create label.
l = tk.Label(root, text = "Left Click and Drag to draw.")
l.pack()
l.place(relx = 0.5, rely = 1.0, anchor = 's')

root.mainloop()
