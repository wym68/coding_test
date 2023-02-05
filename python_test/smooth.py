import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# 创建数据
x = np.linspace(0, 10, 10)
y = np.sin(x)

# 定义光滑曲线函数
spl = UnivariateSpline(x, y)

# 指定光滑曲线的平滑程度
spl.set_smoothing_factor(0.5)

# 计算光滑曲线上的点
x_smooth = np.linspace(0, 10, 1000)
y_smooth = spl(x_smooth)

# 绘制原始数据与光滑曲线
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_smooth, y_smooth, label='Smoothed Curve')
plt.legend()
plt.show()

