from plotter import Colors, Loc, Plot


# Diamonds plots
# for i in range(1, 5):
#     Plot(
#         title=f"Diamonds Explorer {i}",
#         loc=Loc.lowerRight,
#         data=[
#             (f"Diamonds{i}_0.5_UCB1", "UCB1 (stochastic)", Colors.blue),
#             (f"Diamonds{i}_0.5_var", "Uncertainty sampling (stochastic)", Colors.red),
#             (f"Diamonds{i}_0.5_NN", "Neural Network (stochastic)", Colors.purple),
#             (f"Diamonds{i}_0.0_UCB1", "UCB1 (deterministic)", Colors.green),
#             (f"Diamonds{i}_0.0_var", "Uncertainty sampling (deterministic)", Colors.brown),
#             (f"Diamonds{i}_0.0_NN", "Neural Network (deterministic)", Colors.yellow),
#         ],
#     )

# Plot(
#     title="convert1",
#     loc=Loc.lowerRight,
#     data=[
#         ("MonsterLevel_Conver1", "Monsters", Colors.pink),
#         ("Coconuts_Conver1", "Coconuts", Colors.green),
#         ("Maze_Conver1", "Maze", Colors.orange),
#         ("Causal3_Conver1", "Lights1", Colors.black),
#         ("Causal4_Conver1", "Lights2", Colors.purple),
#     ],
# )

# Plot(
#     title="convert2",
#     loc=Loc.lowerRight,
#     data=[
#         ("MonsterLevel_Conver2", "Monsters", Colors.pink),
#         ("Coconuts_Conver2", "Coconuts", Colors.green),
#         ("Maze_Conver2", "Maze", Colors.orange),
#         ("Causal3_Conver2", "Lights1", Colors.black),
#         ("Causal4_Conver2", "Lights2", Colors.purple),
#     ],
# )

# Plot(
#     title="Teleporter",
#     loc=Loc.lowerRight,
#     data=[
#         ("DoorsAndKey_teleport", "DoorsAndKey", Colors.blue),
#         ("Monsters_teleport", "Monsters", Colors.pink),
#         ("Coconuts_teleport", "Coconuts", Colors.green),
#         ("Rocks_teleport", "Rocks", Colors.brown),
#         ("Maze_teleport", "Maze", Colors.orange),
#         ("Lights1_teleport", "Lights1", Colors.black),
#         ("Lights2_teleport", "Lights2", Colors.purple),
#         ("Diamonds1_teleport", "Diamonds1", Colors.yellow),
#         ("Diamonds2_teleport", "Diamonds2", Colors.red),
#         ("Diamonds3_teleport", "Diamonds3", Colors.blueGray),
#         ("Diamonds4_teleport", "Diamonds4", Colors.lightGreen),
#     ],
# )

# Plot(
#     title="Simple",
#     loc=Loc.lowerRight,
#     data=[
#         ("DoorsAndKey_simple", "DoorsAndKey", Colors.blue),
#         ("Monsters_simple", "Monsters", Colors.pink),
#         ("Coconuts_simple", "Coconuts", Colors.green),
#         ("Rocks_simple", "Rocks", Colors.brown),
#         ("Maze_simple", "Maze", Colors.orange),
#         ("Lights1_simple", "Lights1", Colors.black),
#         ("Lights2_simple", "Lights2", Colors.purple),
#         ("Diamonds1_simple", "Diamonds1", Colors.yellow),
#         ("Diamonds2_simple", "Diamonds2", Colors.red),
#         ("Diamonds3_simple", "Diamonds3", Colors.blueGray),
#         ("Diamonds4_simple", "Diamonds4", Colors.lightGreen),
#     ],
# )


# Plot(
#     title="option_critic1",
#     loc=Loc.lowerRight,
#     data=[
#         ("DoorsAndKey_option_critic", "DoorsAndKey", Colors.blue),
#         ("Monsters_option_critic", "Monsters", Colors.pink),
#         ("Coconuts_option_critic", "Coconuts", Colors.green),
#         ("Maze_option_critic", "Maze", Colors.orange),
#         ("Lights1_option_critic", "Lights1", Colors.black),
#         ("Lights2_option_critic", "Lights2", Colors.purple),
#         ("Diamonds1_option_critic", "Diamonds1", Colors.yellow),
#         ("Diamonds2_option_critic", "Diamonds2", Colors.red),
#         ("Diamonds3_option_critic", "Diamonds3", Colors.blueGray),
#         ("Diamonds4_option_critic", "Diamonds4", Colors.lightGreen),
#     ],
# )

Plot(
    title="option_critic2",
    loc=Loc.lowerRight,
    data=[
        ("Attempt2_Coconuts_option_critic", "Coconuts", Colors.orange),
        ("Attempt2_Maze_option_critic", "Maze", Colors.orange),
        ("Attempt2_Lights1_option_critic", "Lights1", Colors.black),
        ("Attempt2_Lights2_option_critic", "Lights2", Colors.purple),
        ("Attempt2_Diamonds1_option_critic", "Diamonds1", Colors.yellow),
        ("Attempt2_Diamonds2_option_critic", "Diamonds2", Colors.red),
        ("Attempt2_Diamonds3_option_critic", "Diamonds3", Colors.blueGray),
        ("Attempt2_Diamonds4_option_critic", "Diamonds4", Colors.blueGray),
        ("Attempt2_DoorsAndKey_option_critic", "DoorsAndKey", Colors.blueGray),
        ("Attempt2_Monsters_option_critic", "Monsters", Colors.blueGray),
        ("Attempt2_SuperLevel1_option_critic", "SuperLevel1", Colors.blueGray),
        ("Attempt2_SuperLevel2_option_critic", "SuperLevel2", Colors.blueGray),
    ],
)

Plot(
    title="option_critic8",
    loc=Loc.lowerRight,
    data=[
        ("Attempt8_Maze_option_critic", "Maze", Colors.orange),
        ("Attempt8_Lights1_option_critic", "Lights1", Colors.black),
        ("Attempt8_Lights2_option_critic", "Lights2", Colors.purple),
        ("Attempt8_Diamonds1_option_critic", "Diamonds1", Colors.yellow),
        ("Attempt8_Diamonds2_option_critic", "Diamonds2", Colors.red),
        ("Attempt8_Diamonds3_option_critic", "Diamonds3", Colors.blueGray),
    ],
)

# Plot(
#     title="option_critic6",
#     loc=Loc.lowerRight,
#     data=[
#         ("Attempt6_Maze_option_critic", "Maze", Colors.orange),
#         ("Attempt6_Lights1_option_critic", "Lights1", Colors.black),
#         ("Attempt6_Lights2_option_critic", "Lights2", Colors.purple),
#         ("Attempt6_Diamonds1_option_critic", "Diamonds1", Colors.yellow),
#         ("Attempt6_Diamonds2_option_critic", "Diamonds2", Colors.red),
#         ("Attempt6_Diamonds3_option_critic", "Diamonds3", Colors.blueGray),
#     ],
# )


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
#         title=name+' Comparison',
#         loc=Loc.lowerRight,
#         data=[
#             (f"{env}_simple", "Q-learn", Colors.blue),
#             (f"{env}_teleport", "Teleport", Colors.pink),
#         ],
#     )
