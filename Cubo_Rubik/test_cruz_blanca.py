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
