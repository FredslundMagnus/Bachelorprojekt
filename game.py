from torch import tensor, Tensor
from helper import device
from layers import Layers, LayerType
from typing import List, Tuple
from levels import Causal5, Levels


class Game:
    def __init__(self, batch: int = None, hours: float = None, width: int = None, height: int = None, level: Levels = None, reset_chance: float = None, layer_Blocks: bool = None, layer_Goal: bool = None, layer_Gold: bool = None, layer_Keys: bool = None, layer_Door: bool = None, layer_Holder: bool = None, layer_Putter: bool = None, layer_Rock: bool = None, layer_Dirt: bool = None, layer_Diamond1: bool = None, layer_Diamond2: bool = None, layer_Diamond3: bool = None, layer_Diamond4: bool = None, layer_Reddoors: bool = None, layer_Redkeys: bool = None, layer_Bluedoors: bool = None, layer_Bluekeys: bool = None, layer_Pink1: bool = None, layer_Pink2: bool = None, layer_Pink3: bool = None, layer_Brown1: bool = None, layer_Brown2: bool = None, layer_Brown3: bool = None, **kwargs) -> None:
        super().__init__()
        self.batch: int = batch
        self.hours: float = hours
        self.level: Levels = level
        self.uses = {
            Levels.Causal1: {LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Keys, LayerType.Door},
            Levels.Causal2: {LayerType.Blocks, LayerType.Goal, LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4},
            Levels.Causal3: {LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys},
            Levels.Causal4: {LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys, LayerType.Rock, LayerType.Dirt},
            Levels.Rocks: {LayerType.Blocks, LayerType.Goal, LayerType.Rock, LayerType.Dirt},
            Levels.Maze: {LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Door, LayerType.Keys, LayerType.Holder, LayerType.Putter},
            Levels.Causal5: {LayerType.Blocks, LayerType.Goal, LayerType.Brown1, LayerType.Brown2, LayerType.Brown3, LayerType.Pink1, LayerType.Pink2, LayerType.Pink3},
        }
        temp1 = [layer_Blocks, layer_Goal, layer_Gold, layer_Keys, layer_Door, layer_Holder, layer_Putter, layer_Dirt, layer_Rock, layer_Diamond1, layer_Diamond2, layer_Diamond3, layer_Diamond4, layer_Reddoors, layer_Redkeys, layer_Bluedoors, layer_Bluekeys, layer_Brown1, layer_Brown2, layer_Brown3, layer_Pink1, layer_Pink2, layer_Pink3]
        temp2 = [LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Keys, LayerType.Door, LayerType.Holder, LayerType.Putter, LayerType.Dirt, LayerType.Rock, LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4, LayerType.Reddoor, LayerType.Redkeys, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Brown1, LayerType.Brown2, LayerType.Brown3, LayerType.Pink1, LayerType.Pink2, LayerType.Pink3]
        self.layers: Layers = Layers(batch, width, height, level, reset_chance, *[layer for use, layer in zip(temp1, temp2) if use and (layer in self.uses[level])])
        for i in range(width):
            for j in range(height):
                for k in range(batch):
                    self.layers.all_items[k][(i, j)] = 0
        self.layers.update()

    @property
    def board(self) -> Tensor:
        return tensor(self.layers.board, device=device)

    def step(self, action: Tensor) -> Tuple[Tensor, Tensor, Tensor, List[dict]]:
        rewards, dones, info = self.layers.step(action.tolist())
        return self.board, tensor(rewards, device=device), tensor(dones, device=device), info
