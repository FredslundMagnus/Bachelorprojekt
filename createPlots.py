from plotter import Colors, Loc, Plot


Plot(
    title="Test Causal 2 and 5 Config",
    data=[
        ('causal2_demo', "Causal 2", Colors.blue),
        ('causal5_demo', "Causal 5", Colors.red),
    ],
)

Plot(
    title="Test Causal",
    loc=Loc.lowerRight,
    data=[
        ('causal2_demo', "Causal 2", Colors.blue),
        ('causal5_demo', "Causal 5", Colors.red),
        ('causal6_demo', "Causal 6", Colors.green),
        ('causal7_demo', "Causal 7", Colors.brown),
    ],
)
