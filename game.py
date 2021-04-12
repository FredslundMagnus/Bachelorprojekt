from torch import tensor, Tensor
from helper import device
from layers import Layers, LayerType
from typing import List, Tuple
from levels import Levels, MonsterLevel


class Game:
    def __init__(self, batch: int = None, hours: float = None, width: int = None, height: int = None, level: Levels = None, reset_chance: float = None, failed_actions_chance: float = None, **kwargs) -> None:
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
            Levels.Coconuts: {LayerType.Blocks, LayerType.Goal, LayerType.Rock, LayerType.Dirt, LayerType.Gold, LayerType.Coconut},
            Levels.Causal6: {LayerType.Blocks, LayerType.Goal, LayerType.Greendown, LayerType.Greenup, LayerType.Greenstar, LayerType.Yellowstar, LayerType.Bluestar},
            Levels.SuperLevel: {LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys, LayerType.Rock, LayerType.Dirt, LayerType.Coconut, LayerType.Door, LayerType.Keys},
            Levels.SuperLevel2: {LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys, LayerType.Rock, LayerType.Dirt, LayerType.Coconut},
            Levels.MonsterLevel: {LayerType.Blocks, LayerType.Goal, LayerType.Gold, LayerType.Monster, LayerType.Rock},
            Levels.Causal7: {LayerType.Blocks, LayerType.Goal, LayerType.Greencross, LayerType.Bluecross, LayerType.Redcross, LayerType.Purplecross}
        }
        convert = {(use, [layer for layer in LayerType if layer.name == name.split('_')[1]][0]) for name, use in kwargs.items() if name.split('_')[0] == "layer"}
        self.layers: Layers = Layers(batch, width, height, level, reset_chance, failed_actions_chance, *[layer for use, layer in convert if use and (layer in self.uses[level])])
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
