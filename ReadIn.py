import cv2
import numpy as np
import matplotlib.pyplot as plt


# file = '.PuzzleSolver\maze_puzzle3.jpg'
file = "PuzzleSolver/maze_puzzle3.jpg"
img = cv2.imread(file)
plt_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cols = plt_img.shape[1]
row = 0
col = 0

row_values = []
rows_delete = []

width, height, channels = plt_img.shape

#this for loop is identifying the actual layout of the maze, it changes the colors to make sure it is getting
#it right
def find_lines():
    maze_pxls = []
    for i in range(width):
        for j in range(height):
            if (plt_img[i][j][0] == 255):
                plt_img[i][j] = [0,0,225]
                maze_pxls.append((i,j))
            else:
                plt_img[i][j] = [0,225,0]

plt.imshow(plt_img)
plt.show()


