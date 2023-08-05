import torch
import numpy as np

# creates empty tensor
x = torch.empty(3,3) 
print(f'{x}\n')

# creates random tensors
x = torch.rand(3,3) 
print(f'{x}\n')

# creates 1s tensors
x = torch.ones(3,3) 
print(f'{x}\n')

# see datatype of tensor
x = torch.empty(1)
print(f'{x.dtype}\n')

# set datatype of tensor
x = torch.empty(1, dtype=torch.int)
print(f'{x.dtype}\n')

# see size of tensor
x = torch.empty(1)
print(f'{x.size()}\n')

# create premade tensor
x = torch.tensor([21, 34, 53])
print(f'{x}\n')

# tensor arithmatic (all other arithmatic is possible in the same way)
x = torch.rand(2,2)
y = torch.rand(2,2)
print(f'{x}\n')
print(f'{y}\n')
z = x + y
print(f'{z}\n')

# tensor slicing
x = torch.rand(5,3)
print(f'{x}\n')
print(f'{x[:, 1]}\n')
print(f'{x[1, :]}\n')
print(f'{x[1, 1].item()}\n')

# tensor reshaping
x = torch.rand(4,4)
print(f'{x}\n')
y = x.view(16)
print(f'{y}\n')
y = x.view(-1, 8)
print(f'{y}\n')

# convert from numpy to tensor
a = torch.ones(5)
b = a.numpy() # converts tensor to numpy array
