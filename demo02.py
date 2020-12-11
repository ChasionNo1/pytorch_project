import torch

x = torch.tensor([4, 5])
print(x)
a = torch.rand(5, 3)
print(a.size())
b = torch.rand(5, 3)
print(a + b)

print(torch.add(a, b))
