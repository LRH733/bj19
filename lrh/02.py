import torch
import matplotlib.pyplot as plt

#生成数据
feature = torch.rand(1000, 2)
true_w = torch.tensor([1, 2],dtype=torch.float).view(-1,1)
true_b = 4.1
labels = torch.mm(feature, true_w) + true_b + torch.normal(0,0.01,size=(1000,1))


print(labels)
