import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

DEAD = 0
LIVE = 1

def initial_setup(grid_size):
    return np.random.choice([DEAD, LIVE], grid_size * grid_size, p = [0.9,  0.1]).reshape(grid_size, grid_size)
 
def set_state(cell, i, j, grid_size, grid_view):
    N = grid_size
    neighbours_state = grid_view[i, (j-1) % N] + grid_view[i, (j+1) % N] + grid_view[(i-1) % N, (j-1) % N] + grid_view[(i-1) % N, j] + grid_view[(i-1) %     N, (j+1) % N] + grid_view[(i+1) % N, (j-1) % N] + grid_view[(i+1) % N, j] + grid_view[(i+1) % N, (j+1) % N]
    if cell == 1:
        if neighbours_state > 3 or neighbours_state <=1:
            cell = 0
    if neighbours_state == 3:
        cell = 1
    return cell
 
def game_handler(frame_num, grid_size, img):
    for row_num, row in enumerate(grid_view):
        for column_num, cell in enumerate(row):
            grid_view[row_num, column_num] = set_state(cell, row_num, column_num, grid_size, grid_view)
    img.set_data(grid_view)
    return img

parser = argparse.ArgumentParser()
parser.add_argument("--N", type= int, action="store", dest="grid_size", default=80)
args = parser.parse_args()
grid_size = args.grid_size

grid_view = initial_setup(grid_size)
  
fig, ax = plt.subplots()
img = ax.imshow(grid_view)
a = FuncAnimation(fig, game_handler, frames = 20, interval = 50, fargs= (grid_size, img), repeat= False)
plt.show()


