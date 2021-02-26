
from torch import device as devicer, cuda

device = devicer('cuda' if cuda.is_available() else 'cpu')
