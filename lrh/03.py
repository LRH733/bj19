import torch


x = torch.arange(16).view(4, 4)
y = torch.ones((4, 4)).type_as(x)
z = x * y
p = torch.mul(x, y)
l = torch.mm(x, y)
q = torch.matmul(x, y)

print(" * 结果：", z)
print(" mul 结果：", p)
print(" mm 结果：", l)
print(" matmul 结果：", q)


