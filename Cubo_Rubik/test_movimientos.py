from CuboRubik import Cube
import random

a = Cube()
a.set_cube_from_letters([["f0","c0","b1","e1","l1","a1","g1","d1","j1","i0","h1","k0"],
                         ["A1","B1","G0","D1","E1","F1","C0","H1"],
                         ["alpha",0]])

b = a.copy()

MOVES = ["U", "D", "F", "B", "R", "L"]
move = []
inverse_move = []

for _ in range(10000):
    random_move = random.choice(MOVES)

    move += random_move
    inverse_move += random_move
    inverse_move += random_move
    inverse_move += random_move

inverse_move.reverse()

for i in move:
    match i:
        case "U":
            b.U()
        case "D":
            b.D()
        case "F":
            b.F()
        case "B":
            b.B()
        case "R":
            b.R()
        case "L":
            b.L()

for i in inverse_move:
    match i:
        case "U":
            b.U()
        case "D":
            b.D()
        case "F":
            b.F()
        case "B":
            b.B()
        case "R":
            b.R()
        case "L":
            b.L()

if a == b:
    print("todo correcto")
else:
    print("hay fallos")
