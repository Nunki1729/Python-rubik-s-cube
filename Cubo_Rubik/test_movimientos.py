"""
    Program: Python rubik's cube
    Copyright (C) 2026 Javier Santiago (Nunki1729)
 
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

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
