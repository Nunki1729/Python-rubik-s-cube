"""
    SISTEMA DE REPRESENTACIÓN DEL CUBO

    1) ORIENTACIÓN GLOBAL

    La orientación del cubo se representa como (letra_griega, número).

    - La letra griega indica qué color está en la cara Up:
        blanco   -> alpha
        naranja  -> beta
        azul     -> gamma
        rojo     -> delta
        verde    -> epsilon
        amarillo -> zeta

    - El número (0–3) indica cuántos giros de 90° en sentido horario mirando a Up de frente
    alrededor del eje vertical se han aplicado desde la orientación base de mayor prioridad hasta
    la orientación actual.

    Ejemplo: (beta, 3)

    Significa que la cara naranja está en Up y que la cara verde está en Front.


    2) SISTEMA BASE ABSOLUTO

    Para leer y codificar las piezas, el cubo se coloca virtualmente en la
    orientación base (alpha, 0):

        - Blanco en Up.
        - Rojo en Front.

    Todas las posiciones (UB, UR, UF, etc.) están definidas respecto a
    esta orientación base. Es el sistema de referencia absoluto del modelo.


    3) REPRESENTACIÓN DE ARISTAS

    Cada arista se representa como: letra + orientación

    Ejemplo: f0

    - La letra (a–l) identifica la pieza concreta según un orden alfabético
    asignado recorriendo el cubo capa por capa en sentido horario.

    Ejemplos:
        a -> blanco-naranja
        e -> verde-naranja
        k -> rojo-amarillo

    - La orientación es 0 o 1:
        0 -> el color de mayor prioridad está en la cara de mayor prioridad
        1 -> no lo está (arista volteada)

    Las aristas se almacenan en una lista ordenada. La posición en la lista
    indica la posición física en el cubo (según la orientación alpha, 0).

    Ejemplo: f0 en la posición 0
    Significa que la arista azul-naranja está en la posición UB (en alpha, 0),
    con naranja en Up y azul en Back.


    4) REPRESENTACIÓN DE ESQUINAS

    Cada esquina se representa como: letra + orientación

    Ejemplo: D2

    - La letra (A–H) identifica la pieza concreta.
    - La orientación puede ser 0, 1 o 2.

    El número de orientación indica cuántas rotaciones de 120° en sentido horario
    ha sufrido la pieza desde la orientación en la que su color de mayor prioridad
    coincide con la cara de mayor prioridad.

    Las esquinas se almacenan en una lista ordenada. La posición en la lista
    indica su posición física en el cubo (según alpha, 0).

    Ejemplo: D2 en la posición 4

    Significa que la esquina amarillo-naranja-verde está en la posición DBL
    (en alpha, 0), con:
        amarillo en Left,
        verde en Back,
        naranja en Down.
"""


class Cube:

    """
    Posición aleatoria:
        aristas -> f0, c0, b1, e1, l1, a1, g1, d1, j1, i0, h1, k0
        esquinas -> A2, B2, G0, D2, E2, F2, C0, H2
        orientación -> alpha, 0
        [["f0", "c0", "b1", "e1", "l1", "a1", "g1", "d1", "j1", "i0", "h1", "k0"],
         ["A2", "B2", "G0", "D2", "E2", "F2", "C0", "H2"], ["alpha", 0]]

    [["f0","c0","b1","e1","l1","a1","g1","d1","j1","i0","h1","k0"],["A2","B2","G0","D2","E2","F2","C0","H2"],["alpha",0]]

    [5,0],[2,0],[1,1],[4,1],[11,1],[0,1],[6,1],[3,1],[9,1],[8,0],[7,1],[10,0]
    [0,2],[1,2],[6,0],[3,2],[4,2],[5,2],[2,0],[7,2]
    [0,0]

    IDEAS PARA MEJORAR EL CÓDIGO:
    Crear la función set_cube() que admita el mismo formato que el que usa view_cube_set()
    Mejorar la función set_cube_friendly()
    Añadir una memoria para guardar los distintos cubos, los movimientos...
    Añadir funciones para añadir movimentos
    Tener en cuenta la orientación del cubo (al introducir el cubo hay que paasarlo a la orientación correcta)
    """

    # Constants
    
    SOLVED_CUBE = (
        ((i, 0) for i in range(12)),
        ((i, 0) for i in range(8)),
        (0, 0)
    )

    EDGE_COLORS = {
        0: ("W", "O"), 1: ("W", "B"), 2: ("W", "R"), 3: ("W", "G"),
        4: ("O", "G"), 5: ("O", "B"), 6: ("R", "B"), 7: ("R", "G"),
        8: ("Y", "O"), 9: ("Y", "B"), 10: ("Y", "R"), 11: ("Y", "G")
    }

    CORNER_COLORS = {
        0: ("W", "O", "G"), 1: ("W", "B", "O"), 2: ("W", "R", "B"), 3: ("W", "G", "R"),
        4: ("Y", "G", "O"), 5: ("Y", "O", "B"), 6: ("Y", "B", "R"), 7: ("Y", "R", "G")
    }

    ALGORITHMS = {
        "T": ("R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"),
        "Ja": ("R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'"),
        "Jb": ("R'", "U2", "R", "U", "R'", "U2", "L", "U'", "R", "U", "L'"),
        "Rb": ("L", "U2", "L'", "U2", "L", "F'", "L'", "U'", "L", "U", "L", "F", "L2", "U")
    }

    WHITE_CROSS = {
        (0, 0): (), (0, 1): ("U'",), (0, 2): ("U2",), (0, 3): ("U",),
        (0, 4): ("B'",), (0, 5): ("B",), (0, 6): ("R", "U'"), (0, 7): ("L'", "U"),
        (0, 8): ("B2",), (0, 9): ("R", "B"), (0, 10): ("F", "L'", "U"), (0, 11): ("L", "B'"),

        (1, 0): (), (1, 1): (), (1, 2): ("F", "R"), (1, 3): ("L'", "F2", "R"),
        (1, 4): ("L'", "D2", "R2"), (1, 5): ("R'",), (1, 6): ("R",), (1, 7): ("F2", "R"),
        (1, 8): ("D'", "R2"), (1, 9): ("R2",), (1, 10): ("D", "R2"), (1, 11): ("D2", "R2"),

        (2, 0): (), (2, 1): (), (2, 2): (), (2, 3): ("L", "F"),
        (2, 4): ("L2", "F"), (2, 5): ("R", "D'", "R'", "F2"), (2, 6): ("F'",), (2, 7): ("F",),
        (2, 8): ("D2", "F2"), (2, 9): ("D'", "F2"), (2, 10): ("F2",), (2, 11): ("D", "F2"),

        (3, 0): (), (3, 1): (), (3, 2): (), (3, 3): (),
        (3, 4): ("L",), (3, 5): ("B2", "L", "B2"), (3, 6): ("F2", "L'", "F2"), (3, 7): ("L'",),
        (3, 8): ("D", "L2"), (3, 9): ("D2", "L2"), (3, 10): ("D'", "L2"), (3, 11): ("L2",)
    }

    # Special methods
    
    def __init__(self):
        self._colors = {
            "up": [None] * 9,
            "down": [None] * 9,
            "front": [None] * 9,
            "back": [None] * 9,
            "right": [None] * 9,
            "left": [None] * 9,
        }

        self._edge = [[i, 0] for i in range(12)]
        self._corner = [[i, 0] for i in range(8)]
        self._orientation = [0, 0]

    def __eq__(self, other):
        if not isinstance(other, Cube):
            return False

        return (
                self._edge == other._edge and
                self._corner == other._corner and
                self._orientation == other._orientation
        )

    def __repr__(self):
        return f"Cube(edges={self._edge}, corners={self._corner}, orientation={self._orientation})"

    def __str__(self):
        self.set_colors()
    
        face = {
            "up": None,
            "down": None,
            "front": None,
            "back": None,
            "left": None,
            "right": None
        }

        for side in face:
            face[side] = [
                [self._colors[side][0], self._colors[side][1], self._colors[side][2]],
                [self._colors[side][3], self._colors[side][4], self._colors[side][5]],
                [self._colors[side][6], self._colors[side][7], self._colors[side][8]]
            ]

        output = "EL CUBO AHORA MISMO:\n\n"

        for side in face:
            output += f"{side.upper()}:\n"
            for row in face[side]:
                output += f"{row[0]} {row[1]} {row[2]}\n"
            output += "-------------------------\n"

        return output
    
    # Methods for encapsulation
    
    def _set_edges(self, edges=SOLVED_CUBE[0]):
        self._edge = [e[:] for e in edges]

    def _set_corners(self, corners=SOLVED_CUBE[1]):
        self._corner = [c[:] for c in corners]

    def _set_orientation(self, orientation=SOLVED_CUBE[2]):
        self._orientation = list(orientation)

    def set_cube(self, cube=SOLVED_CUBE):
        self._set_edges(cube[0])
        self._set_corners(cube[1])
        self._set_orientation(cube[2])

    # Useful methods
    
    def copy(self):
        new = Cube()

        new._edge = [e[:] for e in self._edge]
        new._corner = [c[:] for c in self._corner]
        new._orientation = list(self._orientation)

        return new

    def set_cube_from_letters(self, cube_set=SOLVED_CUBE):
        # Set edges
        letter_to_num_edge = {lett: num for num, lett in enumerate("abcdefghijkl")}
        new_edge = [[i, 0] for i in range(12)]

        for i, edge in enumerate(cube_set[0]):
            new_edge[i] = [letter_to_num_edge[edge[0]], int(edge[1])]

        self._set_edges(new_edge)

        # Set corners
        letter_to_num_corner = {lett: num for num, lett in enumerate("ABCDEFGH")}
        new_corner = [[i, 0] for i in range(8)]

        for i, corner in enumerate(cube_set[1]):
            new_corner[i] = [letter_to_num_corner[corner[0]], int(corner[1])]

        self._set_corners(new_corner)

        # Set orientation
        centers = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]
        letter_to_num_center = {lett: num for num, lett in enumerate(centers)}

        new_orientation = [letter_to_num_center[cube_set[2][0]], int(cube_set[2][1])]

        self._set_orientation(new_orientation)

    # Color
    
    def _reset_colors(self):
        self._colors = {
            "up": [None] * 9,
            "down": [None] * 9,
            "front": [None] * 9,
            "back": [None] * 9,
            "right": [None] * 9,
            "left": [None] * 9,
        }

    def _set_colors_edges(self):
        # Set up face
        for sticker, edge_index in zip((1, 3, 5, 7), (0, 3, 1, 2)):
            edge_num, edge_orient = self._edge[edge_index]
            self._colors["up"][sticker] = self.EDGE_COLORS[edge_num][edge_orient]

        # Set down face
        for sticker, edge_index in zip((1, 3, 5, 7), (8, 9, 11, 10)):
            edge_num, edge_orient = self._edge[edge_index]
            self._colors["down"][sticker] = self.EDGE_COLORS[edge_num][edge_orient]

        # Set front face
        for sticker, edge_index in zip((1, 3, 5, 7), (2, 7, 6, 10)):
            edge_num, edge_orient = self._edge[edge_index]

            if edge_index in (2, 10):
                self._colors["front"][sticker] = self.EDGE_COLORS[edge_num][(edge_orient + 1) % 2]
            elif edge_index in (7, 6):
                self._colors["front"][sticker] = self.EDGE_COLORS[edge_num][edge_orient]

        # Set back face
        for sticker, edge_index in zip((1, 3, 5, 7), (8, 4, 5, 0)):
            edge_num, edge_orient = self._edge[edge_index]

            if edge_index in (8, 0):
                self._colors["back"][sticker] = self.EDGE_COLORS[edge_num][(edge_orient + 1) % 2]
            elif edge_index in (4, 5):
                self._colors["back"][sticker] = self.EDGE_COLORS[edge_num][edge_orient]

        # Set right face
        for sticker, edge_index in zip((1, 3, 5, 7), (5, 1, 9, 6)):
            edge_num, edge_orient = self._edge[edge_index]
            self._colors["right"][sticker] = self.EDGE_COLORS[edge_num][(edge_orient + 1) % 2]

        # Set left face
        for sticker, edge_index in zip((1, 3, 5, 7), (4, 11, 3, 7)):
            edge_num, edge_orient = self._edge[edge_index]
            self._colors["left"][sticker] = self.EDGE_COLORS[edge_num][(edge_orient + 1) % 2]

    def _set_colors_corners(self):
        # Set up face
        for sticker, corner_index in zip((0, 2, 6, 8), (0, 1, 3, 2)):
            corner_num, corner_orientation = self._corner[corner_index]
            self._colors["up"][sticker] = self.CORNER_COLORS[corner_num][corner_orientation]

        # Set down face
        for sticker, corner_index in zip((0, 2, 6, 8), (5, 4, 6, 7)):
            corner_num, corner_orientation = self._corner[corner_index]
            self._colors["down"][sticker] = self.CORNER_COLORS[corner_num][corner_orientation]

        # Set front face
        for sticker, corner_index in zip((0, 2, 6, 8), (3, 2, 7, 6)):
            corner_num, corner_orientation = self._corner[corner_index]

            if corner_index in (3, 6):
                self._colors["front"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 2) % 3]
            elif corner_index in (2, 7):
                self._colors["front"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 1) % 3]

        # Set back face
        for sticker, corner_index in zip((0, 2, 6, 8), (4, 5, 0, 1)):
            corner_num, corner_orientation = self._corner[corner_index]

            if corner_index in (4, 1):
                self._colors["back"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 2) % 3]
            elif corner_index in (5, 0):
                self._colors["back"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 1) % 3]

        # Set right face

        for sticker, corner_index in zip((0, 2, 6, 8), (1, 5, 2, 6)):
            corner_num, corner_orientation = self._corner[corner_index]

            if corner_index in (1, 6):
                self._colors["right"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 1) % 3]
            elif corner_index in (5, 2):
                self._colors["right"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 2) % 3]

        # Set left face
        for sticker, corner_index in zip((0, 2, 6, 8), (4, 0, 7, 3)):
            corner_num, corner_orientation = self._corner[corner_index]

            if corner_index in (4, 3):
                self._colors["left"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 1) % 3]
            elif corner_index in (0, 7):
                self._colors["left"][sticker] = self.CORNER_COLORS[corner_num][(corner_orientation + 2) % 3]

    def set_colors(self):
        self._reset_colors()
        self._set_colors_edges()
        self._set_colors_corners()

        for face, color in zip(self._colors, ("W", "Y", "R", "O", "B", "G")):
            self._colors[face][4] = color

        return self._colors
    
    # Movements

    def U(self):
        # Edges
        edges = [e[:] for e in self._edge]

        edges[0] = self._edge[3][:]
        edges[1] = self._edge[0][:]
        edges[2] = self._edge[1][:]
        edges[3] = self._edge[2][:]

        self._edge = [e[:] for e in edges]

        # Corners

        corners = [c[:] for c in self._corner]

        corners[0] = self._corner[3][:]
        corners[1] = self._corner[0][:]
        corners[2] = self._corner[1][:]
        corners[3] = self._corner[2][:]

        self._corner = [c[:] for c in corners]

    def D(self):
        # Edges
        edges = [e[:] for e in self._edge]

        edges[8] = self._edge[9][:]
        edges[11] = self._edge[8][:]
        edges[10] = self._edge[11][:]
        edges[9] = self._edge[10][:]

        self._edge = [e[:] for e in edges]

        # Corners

        corners = [c[:] for c in self._corner]

        corners[4] = self._corner[5][:]
        corners[7] = self._corner[4][:]
        corners[6] = self._corner[7][:]
        corners[5] = self._corner[6][:]

        self._corner = [c[:] for c in corners]

    def F(self):
        # Edges
        edges = [e[:] for e in self._edge]

        edges[2] = self._edge[7][:]
        edges[6] = self._edge[2][:]
        edges[10] = self._edge[6][:]
        edges[7] = self._edge[10][:]

        for edge_index in (2, 6, 10, 7):
            edges[edge_index][1] = (edges[edge_index][1] + 1) % 2

        self._edge = [e[:] for e in edges]

        # Corners

        corners = [c[:] for c in self._corner]

        corners[3] = self._corner[7][:]
        corners[2] = self._corner[3][:]
        corners[6] = self._corner[2][:]
        corners[7] = self._corner[6][:]

        for corner_index in (6, 3):
            corners[corner_index][1] = (corners[corner_index][1] + 2) % 3

        for corner_index in (7, 2):
            corners[corner_index][1] = (corners[corner_index][1] + 1) % 3

        self._corner = [c[:] for c in corners]

    def B(self):
        # Edges
        edges = [e[:] for e in self._edge]

        edges[0] = self._edge[5][:]
        edges[4] = self._edge[0][:]
        edges[8] = self._edge[4][:]
        edges[5] = self._edge[8][:]

        for edge_index in (0, 4, 8, 5):
            edges[edge_index][1] = (edges[edge_index][1] + 1) % 2

        self._edge = [e[:] for e in edges]

        # Corners

        corners = [c[:] for c in self._corner]

        corners[0] = self._corner[1][:]
        corners[4] = self._corner[0][:]
        corners[5] = self._corner[4][:]
        corners[1] = self._corner[5][:]

        for corner_index in (5, 0):
            corners[corner_index][1] = (corners[corner_index][1] + 1) % 3

        for corner_index in (1, 4):
            corners[corner_index][1] = (corners[corner_index][1] + 2) % 3

        self._corner = [c[:] for c in corners]

    def R(self):
        # Edges
        edges = [e[:] for e in self._edge]

        edges[1] = self._edge[6][:]
        edges[6] = self._edge[9][:]
        edges[9] = self._edge[5][:]
        edges[5] = self._edge[1][:]

        self._edge = [e[:] for e in edges]

        # Corners

        corners = [c[:] for c in self._corner]

        corners[2] = self._corner[6][:]
        corners[1] = self._corner[2][:]
        corners[5] = self._corner[1][:]
        corners[6] = self._corner[5][:]

        for corner_index in (5, 2):
            corners[corner_index][1] = (corners[corner_index][1] + 2) % 3

        for corner_index in (6, 1):
            corners[corner_index][1] = (corners[corner_index][1] + 1) % 3

        self._corner = [c[:] for c in corners]

    def L(self):
        # Edges
        edges = [e[:] for e in self._edge]

        edges[3] = self._edge[4][:]
        edges[7] = self._edge[3][:]
        edges[11] = self._edge[7][:]
        edges[4] = self._edge[11][:]

        self._edge = [e[:] for e in edges]

        # Corners

        corners = [c[:] for c in self._corner]

        corners[0] = self._corner[4][:]
        corners[3] = self._corner[0][:]
        corners[7] = self._corner[3][:]
        corners[4] = self._corner[7][:]

        for corner_index in (7, 0):
            corners[corner_index][1] = (corners[corner_index][1] + 2) % 3

        for corner_index in (4, 3):
            corners[corner_index][1] = (corners[corner_index][1] + 1) % 3

        self._corner = [c[:] for c in corners]

    # En desarrollo
    @staticmethod
    def _verify_algorithm(alg):
        return alg

    def _apply_algorithm(self, alg):
        # alg must be something like ["U", "F2", "L'"]
        basic_moves = {
            "U": self.U,
            "D": self.D,
            "F": self.F,
            "B": self.B,
            "R": self.R,
            "L": self.L,
        }

        for move in alg:
            if move in self.ALGORITHMS:
                self._apply_algorithm(self.ALGORITHMS[move])
            elif move[1:] == "":
                basic_moves[move[0]]()
            elif move[1:] == "2":
                basic_moves[move[0]]()
                basic_moves[move[0]]()
            elif move[1:] == "'":
                basic_moves[move[0]]()
                basic_moves[move[0]]()
                basic_moves[move[0]]()

    def algorithm(self, alg):
        self._apply_algorithm(self._verify_algorithm(alg))


class Solver:
    # En desarrollo
    def _solve_white_cross(self):
        for white_e in range(4):
            pos = next(i for i, e in enumerate(self._edge) if e[0] == white_e)
            self.algorithm(self.WHITE_CROSS[(white_e, pos)])
