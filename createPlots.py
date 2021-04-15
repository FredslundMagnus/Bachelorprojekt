from plotter import Plotter, load, Colors, Loc, PlotConfig

with Plotter(title="Test Causal 2 and 5") as plt:
    for name, collectors, color in load(('causal2_demo', "Causal 2", Colors.blue), ('causal5_demo', "Causal 5", Colors.red)):
        plt.varPlot(name, collectors, color)

PlotConfig(
    title="Test Causal 2 and 5 Config",
    data=[
        ('causal2_demo', "Causal 2", Colors.blue),
        ('causal5_demo', "Causal 5", Colors.red),
    ]
)
