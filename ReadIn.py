import cv2
import numpy as np
import matplotlib.pyplot as plt


file = './maze_puzzle3.jpg'
img = cv2.imread(file)
plt_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cols = plt_img.shape[1]
row = 0
col = 0

row_values = []
rows_delete = []

for pxl in plt_img:
    if col < plt_img.shape[0]:
        if col > 0:
            if np.array(plt_img[col][row]).all != np.array([row_values[len(row_values) - 1]]).all:
                print(plt_img[col][row])
                rows_delete.append(row)
                row += 1
                col = 0
                row_values = []
        else:
            row_values.append(plt_img[col][row])
            col += 1
    else:
        row += 1
        col = 0


plt.imshow(plt_img)
plt.show()


