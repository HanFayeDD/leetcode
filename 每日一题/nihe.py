import numpy as np
from sklearn.linear_model import LinearRegression

# 给定数据（请替换为你的实际数据）
x_values = [2, 3, 4, 5, 6]  # 示例x值
y_values = [2.2, 3.8, 5.5, 6.5, 7.0]  # 示例y值

# 将数据转换为二维数组格式（sklearn要求）
X = np.array(x_values).reshape(-1, 1)
y = np.array(y_values)

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(X, y)

# 获取回归系数
slope = model.coef_[0]  # 斜率
intercept = model.intercept_  # 截距

# 输出回归方程
print(f"线性回归方程: y = {slope:.4f}x + {intercept:.4f}")

# 打印R²得分（拟合优度）
r_squared = model.score(X, y)
print(f"R²得分: {r_squared:.4f}")
