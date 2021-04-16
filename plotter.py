from enum import Enum
from load import Load
from collector import Collector
from typing import List, Dict, Tuple
from Utils.debug import enablePrint, disablePrint
import numpy as np
import matplotlib.pyplot as plt
from colors import Colors, MaterialColor


class Loc(Enum):
    upperLeft = 'upper left'
    upperRight = 'upper right'
    lowerLeft = 'lower left'
    lowerRight = 'lower right'


def load(*colectors: List[Tuple[str, str, MaterialColor]], same_x: bool = False) -> List[Tuple[str, List[Collector]]]:
    disablePrint()
    temp: List[Tuple[str, List[Collector]]] = []
    for name, title, color in colectors:
        temp.append((title, [], color))
        for i in range(5):
            try:
                with Load(name, num=i) as load:
                    collector: Collector = load.items(Collector)
                    temp[-1][1].append(*collector)
            except:
                pass
    enablePrint()
    return temp


class Plotter():
    def __init__(self, title: str = 'Placeholder', xlabel: str = 'Games', ylabel: str = "Winrate", loc: Loc = Loc.upperLeft, ylim: Tuple[float, float] = (0, 1), keys: Tuple[int, int] = (0, 0), normalize: int = 100):
        self.plt = plt
        self.loc: str = loc.value
        self.keys: Tuple[float, float] = keys
        self.plt.ylim(ylim)
        self.plt.title(title)
        self.title: str = title
        self.plt.xlabel(xlabel)
        self.plt.ylabel(ylabel)
        self.N: int = normalize

        def varPlot(name: str, collectors: List[Collector], color: MaterialColor, meanVar: bool = False):
            if not collectors:
                raise Exception(f"Der var ingen collectors i den givne position for {name}")
            if collectors:
                data = []
                minL = min(len(collector.data[keys]) for collector in collectors)
                for collector in collectors:
                    data.append(collector.data[keys][:minL])
                data = np.array(data)
                y = np.mean(data, axis=0)
                sd = np.std(data, axis=0)
                y, sd = self.normalize(y, sd)
                x = np.arange(1, len(y) + 1)
                self.plt.plot(x, y, lw=2, label=name, color='#%02x%02x%02x' % color.color, zorder=2)
                if meanVar:
                    sd = sd / np.sqrt(len(collectors))
                self.plt.fill_between(x, y + sd, y - sd, facecolor='#%02x%02x%02x' % color.color, alpha=0.5, zorder=2)
                self.plt.doPrint = True

        self.plt.varPlot = varPlot
        self.plt.doPrint = False

    def __enter__(self):
        return self.plt

    def __exit__(self, types, value, traceback):
        if self.plt.doPrint:
            self.plt.axhline(y=1200, color='#E0E0E0', linestyle='dashed', lw=1, zorder=1)
            self.plt.axhline(y=1400, color='#E0E0E0', linestyle='dashed', lw=1, zorder=1)
            self.plt.axhline(y=1600, color='#E0E0E0', linestyle='dashed', lw=1, zorder=1)
            self.plt.axhline(y=1800, color='#E0E0E0', linestyle='dashed', lw=1, zorder=1)
            self.plt.axhline(y=2000, color='#E0E0E0', linestyle='dashed', lw=1, zorder=1)
            self.plt.axhline(y=2200, color='#E0E0E0', linestyle='dashed', lw=1, zorder=1)
            self.plt.axhline(y=2400, color='#E0E0E0', linestyle='dashed', lw=1, zorder=1)
            self.plt.legend(loc=self.loc)
            self.plt.savefig(f"plots/{self.title.replace(' ', '_')}.png", bbox_inches='tight')
        self.plt.clf()

    def normalize(self, *arrays):
        for array in arrays:
            yield np.convolve(array, np.ones(self.N)/self.N, mode='valid')


class Plot:
    def __init__(self, data: List[Tuple[str, str, MaterialColor]], same_x: bool = False, title: str = 'Placeholder', xlabel: str = 'Games', ylabel: str = "Winrate", loc: Loc = Loc.upperLeft, ylim: Tuple[float, float] = (0, 1), keys: Tuple[int, int] = (0, 0), normalize: int = 100) -> None:
        self.data: List[Tuple[str, str, MaterialColor]] = data
        self.same_x: bool = same_x
        self.title: str = title
        self.xlabel: str = xlabel
        self.ylabel: str = ylabel
        self.loc: Loc = loc
        self.ylim: Tuple[float, float] = ylim
        self.keys: Tuple[float, float] = keys
        self.normalize: int = normalize
        self.createPlot()

    def createPlot(self):
        with Plotter(title=self.title, xlabel=self.xlabel, ylabel=self.ylabel, loc=self.loc, ylim=self.ylim, keys=self.keys, normalize=self.normalize) as plt:
            for name, collectors, color in load(*self.data):
                plt.varPlot(name, collectors, color)


# with Plotter(title="Test Causal 2 and 5") as plt:
#     for name, collectors, color in load(('causal2_demo', "Causal 2", Colors.blue), ('causal5_demo', "Causal 5", Colors.red)):
#         plt.varPlot(name, collectors, color)
