import torch
import torch.nn as nn

m = nn.LogSoftmax(dim=0)
loss = nn.NLLLoss()
# input is of size N x C = 3 x 5
input = torch.randn(5, requires_grad=True)
print('input 1______', torch.exp(m(input)))
# each element in target has to have 0 <= value < C
target = torch.tensor(1)
output = loss(m(input), target)
output.backward()


# # 2D loss example (used, for example, with image inputs)
# N, C = 5, 4
# loss = nn.NLLLoss()
# # input is of size N x C x height x width
# data = torch.randn(N, 16, 10, 10)
# print('data______', data)
# conv = nn.Conv2d(16, C, (3, 3))
# m = nn.LogSoftmax(dim=1)
# # each element in target has to have 0 <= value < C
# target = torch.empty(N, 8, 8, dtype=torch.long).random_(0, C)
# output = loss(m(conv(data)), target)
# output.backward()