
#导入相关库
import time

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")
#读入数据
data = pd.read_excel(r'./fualt_10hang.xlsx')
x = data['A']  # 特征数据，自变量
y = data['B']  # 标签值，因变量
X, Y = np.meshgrid(x, y)
data_ = []
Z = 0.04159464 * X + (-0.19600337)*Y + 4021666.145932085


ax.plot_surface(X,Y,Z,alpha=0.7, cstride=1, rstride = 1, cmap='rainbow')
plt.show()




