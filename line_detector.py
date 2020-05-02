import numpy as np
from RGC import RGC_onCell
from RGC import RGC_offCell
from test_case import *
import matplotlib.pyplot as plt


class LineDetector:
    def __init__(self, input_mat, cell_size, center_size):
        input_height, input_weight = input_mat.shape
        self.cell_mat = []
        for i in range(input_height // cell_size):
            cell_list = []
            for j in range(input_weight // cell_size // 2):
                cell = RGC_onCell(center_size, cell_size)
                firingRate = cell.run(input_mat[i*cell_size:i*cell_size+cell_size,j*cell_size:j*cell_size+cell_size])
                cell_list.append(firingRate)
            for j in range(input_weight // cell_size // 2):
                cell = RGC_offCell(center_size, cell_size)
                firingRate = cell.run(input_mat[i*cell_size:i*cell_size+cell_size,j*cell_size:j*cell_size+cell_size])
                cell_list.append(firingRate)
            self.cell_mat.append(cell_list)
        print(self.cell_mat)

    def judge(self):
        active_val_left = []
        active_val_right = []
        active_spot = []
        for i in range(len(self.cell_mat)):
            for j in range(len(self.cell_mat)//2):
                if self.cell_mat[i][j] != 340:
                    active_val_left.append(self.cell_mat[i][j])
                    active_spot.append(i)
            for j in range(len(self.cell_mat)//2, len(self.cell_mat)):
                if self.cell_mat[i][j] != 340:
                    active_val_right.append(self.cell_mat[i][j])
                    active_spot.append(i)
        if len(set(active_val_left)) == 1 and len(set(active_val_right)) == 1 and len(set(active_spot)) == 1:
            return True
        else:
            return False


test_ele = [i0, i20, i40, i60, i80, i100, i120, i140, i160]
for ele, cnt in zip(test_ele, range(1,10)):
    img = np.array(ele)
    detector = LineDetector(img, 3, 1)
    plt.subplot(3, 3, cnt)
    plt.imshow(img,cmap='binary')
    plt.title(detector.judge())
    plt.axis('off')
plt.show()