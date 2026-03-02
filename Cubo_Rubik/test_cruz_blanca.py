from CuboRubik import Cube
import random

MOVES = ("U", "D", "F", "B", "R", "L",
         "U2", "D2", "F2", "B2", "R2", "L2",
         "U'", "D'", "F'", "B'", "R'", "L'")

for n in range(100):
    a = Cube()
    alg = [random.choice(MOVES) for _ in range(50)]

    a.algorithm(alg)
    a.set_colors()
    a._solve_white_cross()

    for edge_pos in range(4):
        if a._edge[edge_pos][0] != edge_pos:
            print("Problema en la repetición ", n)
