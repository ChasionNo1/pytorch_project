"""
中文版教程
http://www.pytorch123.com/SecondSection/what_is_pytorch/
"""
from __future__ import print_function
import torch
from src import main
import os

x = torch.empty(5, 3)
y = torch.rand(5, 3)
z = torch.zeros(5, 3, dtype=torch.long)

# 路径问题，同一个文件下通过‘./’的形式访问
# 如果是需要向外一级通过‘../’的形式
path = './src/1.webp'
print(x)
print(y)
print(z)