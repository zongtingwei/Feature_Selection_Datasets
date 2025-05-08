import pandas as pd
from scipy.io import loadmat
import numpy as np

mat_data = loadmat('datasets/dataset_name.mat')
X = mat_data['X']
Y = mat_data['Y']

# 合并数据
combined_data = np.hstack((Y, X))

# 保存为 .npy 文件
np.save('dataset_name.npy', combined_data)
