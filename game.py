from torch import tensor, Tensor
from helper import device
from layers import Layers, LayerType
from typing import List, Tuple


class Game:
    def __init__(self, batch: int = None, hours: float = None, width: int = None, height: int = None, reset_chance: float = None, layer_Blocks: bool = None, layer_Goal: bool = None, layer_Gold: bool = None, layer_Keys: bool = None, layer_Door: bool = None, layer_Holder: bool = None, layer_Putter: bool = None, layer_Rock: bool = None, layer_Dirt: bool = None, **kwargs) -> None:
        super().__init__()
        self.batch: int = batch
        self.hours: float = hours
        temp1 = [layer_Blocks, layer_Goal, layer_Gold, layer_Keys, layer_Door, layer_Holder, layer_Putter, layer_Dirt, layer_Rock]
        temp2 = [LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Keys, LayerType.Door, LayerType.Holder, LayerType.Putter, LayerType.Dirt, LayerType.Rock]
        self.layers: Layers = Layers(batch, width, height, reset_chance, *[layer for use, layer in zip(temp1, temp2) if use])
        self.layers.update()

    @property
    def board(self) -> Tensor:
        return tensor(self.layers.board, device=device)

    def step(self, action: Tensor) -> Tuple[Tensor, Tensor, Tensor, List[dict]]:
        rewards, dones, info = self.layers.step(action.tolist())
        return self.board, tensor(rewards, device=device), tensor(dones, device=device), info
