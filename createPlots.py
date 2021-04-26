from plotter import Colors, Loc, Plot


# # Diamonds plots
# for i in range(1, 5):
#     Plot(
#         title=f"Diamonds Explorer {i}",
#         loc=Loc.lowerRight,
#         data=[
#             (f"Diamonds{i}_0.5_UCB1", "UCB1 (stochastic)", Colors.blue),
#             (f"Diamonds{i}_0.5_var", "Uncertainty sampling (stochastic)", Colors.red),
#             (f"Diamonds{i}_0.0_UCB1", "UCB1 (deterministic)", Colors.green),
#             (f"Diamonds{i}_0.0_var", "Uncertainty sampling (deterministic)", Colors.brown),
#         ],
#     )

Plot(
    title="causal42",
    loc=Loc.lowerRight,
    data=[
        ("Causal4_Cf_convert1_TopN6", "convert1_Top3", Colors.blue),
        ("Causal4_Cf_convert2_TopN6", "convert2_Top3", Colors.pink),
        ("Causal4_Cf_convert3_TopN6", "convert3_Top3", Colors.green),
        ("Causal4_Cf_convert4_TopN6", "convert4_Top3", Colors.brown),
        ("Causal4_Cf_convert5_TopN6", "convert5_Top3", Colors.orange),
    ],
)

envs = [
    ('Lights1', 'Magical Lights 1'),
    ('Lights2', 'Magical Lights 2'),
    ('Diamonds1', 'Diamonds Explorer 1'),
    ('Diamonds2', 'Diamonds Explorer 2'),
    ('Diamonds3', 'Diamonds Explorer 3'),
    ('Diamonds4', 'Diamonds Explorer 4'),
    ('SuperLevel1', 'Super Level 1'),
    ('SuperLevel2', 'Super Level 2'),
    ('Maze', 'Maze'),
    ('Rocks', 'Rocks & Dirt'),
    ('Coconuts', 'Coconuts'),
    ('Monsters', 'Monsters'),
    ('DoorsAndKey', 'Doors and Key'),
]

# for env, name in envs:
#     Plot(
#         title=name,
#         loc=Loc.lowerRight,
#         data=[
#             (f"{env}_simple", "Q-learn", Colors.blue),
#             (f"{env}_teleport", "Teleport", Colors.pink),
#         ],
#     )
