import torch
import torchvision
import torch.optim as optim
import torch.nn.functional as F
from model import MnistNet
from sacred import Experiment

ex = Experiment('MNIST_experiment')

batch_size_train = 64
batch_size_test = 1000

train_loader = torch.utils.data.DataLoader(
  torchvision.datasets.MNIST('./mnist_data/', train=True, download=True,
                             transform=torchvision.transforms.Compose([
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])),
  batch_size=batch_size_train, shuffle=True)

test_loader = torch.utils.data.DataLoader(
  torchvision.datasets.MNIST('./mnist_data/', train=False, download=True,
                             transform=torchvision.transforms.Compose([
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])),
  batch_size=batch_size_test, shuffle=True)



@ex.config
def ex_config():
    n_epochs = 3
    learning_rate = 0.01
    momentum = 0.5
    log_interval = 10
    random_seed = 1


@ex.automain
def ex_main(n_epochs, learning_rate, momentum, log_interval, random_seed):
    torch.backends.cudnn.enabled = False
    torch.manual_seed(random_seed)

    network = MnistNet()
    optimizer = optim.SGD(network.parameters(), lr=learning_rate,
                    momentum=momentum)
    network.train()

    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = network(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()

        if batch_idx % log_interval == 0:
            ex.log_scalar("batch", batch_idx)
            ex.log_scalar("loss", loss.item())



