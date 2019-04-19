#coding=utf-8

'''
在训练神经网络之前，我们需要有一个标准定义它到底好不好，以便我们进行改进，这就是损失（loss）。

比如用均方误差（MSE）来定义损失

n是样本的数量，在上面的数据集中是4；y代表人的性别，男性是1，女性是0；ytrue是变量的真实值，ypred是变量的预测值。顾名思义，均方误差就是所有数据方差的平均值，我们不妨就把它定义为损失函数。预测结果越好，损失就越低，训练神经网络就是将损失最小化。
'''
import numpy as np

def mse_loss(y_true, y_pred):
  # y_true and y_pred are numpy arrays of the same length.
  return ((y_true - y_pred) ** 2).mean()

y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])

print(mse_loss(y_true, y_pred)) # 0.5
