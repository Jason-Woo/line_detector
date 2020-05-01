import numpy as np
from RGC import RGC_onCell
from RGC import RGC_offCell

class LineDetector:
    def __init__(self, input_mat, cell_size, center_size):
        input_height, input_weight = input_mat.shape
        cell_mat = []
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
            cell_mat.append(cell_list)
        print(cell_mat)

        
i = [[0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0]]
i = np.array(i)
LineDetector(i, 3, 1)