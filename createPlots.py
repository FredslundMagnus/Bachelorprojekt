from plotter import Colors, Loc, Plot


# Diamonds plots
for i in range(1, 5):
    Plot(
        title=f"Diamonds Explorer {i}",
        loc=Loc.lowerRight,
        data=[
            (f"Diamonds{i}_0.5_UCB1", "UCB1 (stochastic)", Colors.blue),
            (f"Diamonds{i}_0.5_var", "Uncertainty sampling (stochastic)", Colors.red),
            (f"Diamonds{i}_0.0_UCB1", "UCB1 (deterministic)", Colors.green),
            (f"Diamonds{i}_0.0_var", "Uncertainty sampling (deterministic)", Colors.brown),
        ],
    )

# Plot(
#     title="Template",
#     loc=Loc.lowerRight,
#     data=[
#         ("name1", "Title1", Colors.blue),
#         ("name2", "Title2", Colors.red),
#         ("name3", "Title3", Colors.green),
#         ("name4", "Title4", Colors.brown),
#     ],
# )
