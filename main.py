#导入所需要的库
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

fig = plt.figure()  #定义新的三维坐标轴
ax3 = plt.axes(projection='3d')

df = pd.read_excel('fualt1.xlsx',sheet_name='Sheet3')
df.columns = ['x','y','z']
for index,row in df.iterrows():
    print([row['x'],row['y'],row['z']])

# #定义三维数据
# xx = np.arange(-5,5,0.5)
# yy = np.arange(-5,5,0.5)
# X, Y = np.meshgrid(xx, yy)
# Z = np.sin(X)+np.cos(Y)
# print(Z)
#
# #作图
# ax3.plot_surface(X,Y,Z,cmap='rainbow')
# #ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
# plt.show()
