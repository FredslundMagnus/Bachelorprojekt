from plotter import Plotter, load, Colors, Loc, PlotConfig

with Plotter(title="Test Causal 2 and 5") as plt:
    for name, collectors, color in load(('causal2_demo', "Causal 2", Colors.blue), ('causal5_demo', "Causal 5", Colors.red)):
        plt.varPlot(name, collectors, color)

PlotConfig(
    title="Test Causal 2 and 5 Config",
    normalize=1000,
    data=[
        ('causal2_demo', "Causal 2", Colors.blue),
        ('causal5_demo', "Causal 5", Colors.red),
    ]
)

PlotConfig(
    title="Test Causal",
    normalize=50,
    loc=Loc.lowerRight,
    data=[
        ('causal2_demo', "Causal 2", Colors.blue),
        ('causal5_demo', "Causal 5", Colors.red),
        ('causal6_demo', "Causal 6", Colors.green),
        ('causal7_demo', "Causal 7", Colors.brown),
    ],
)
