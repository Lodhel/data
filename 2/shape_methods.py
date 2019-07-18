# import torch
import torchvision.datasets
MNIST_train = torchvision.datasets.MNIST('./', download=True, train=True)
x = MNIST_train.train_data
x = x.float()

x.shape
# x=torch.zeros([6000, 28, 28], dtype=torch.int32)

print(x.reshape(-1, 1, 1).shape)