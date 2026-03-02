class Cube:

    """
    Posición aleatoria:
        aristas -> f0, c0, b1, e1, l1, a1, g1, d1, j1, i0, h1, k0
        esquinas -> A1, B1, G0, D1, E1, F1, C0, H1
        orientación -> alpha, 0
        [["f0", "c0", "b1", "e1", "l1", "a1", "g1", "d1", "j1", "i0", "h1", "k0"],
         ["A1", "B1", "G0", "D1", "E1", "F1", "C0", "H1"], ["alpha", 0]]
    [["f0","c0","b1","e1","l1","a1","g1","d1","j1","i0","h1","k0"],["A1","B1","G0","D1","E1","F1","C0","H1"],["alpha",0]]

    IDEAS PARA MEJORAR EL CÓDIGO:
    Crear la función set_cube() que admita el mismo formato que el que usa view_cube_set()
    Mejorar la función set_cube_friendly()
    Añadir una memoria para guardar los distintos cubos, los movimientos...
    Añadir funciones para añadir movimentos
    Tener en cuenta la orientación del cubo (al introducir el cubo hay que paasarlo a la orientación correcta)
    """

    EDGE_COLORS = {
        0: ["W", "O"], 1: ["W", "B"], 2: ["W", "R"], 3: ["W", "G"],
        4: ["O", "G"], 5: ["O", "B"], 6: ["R", "B"], 7: ["R", "G"],
        8: ["Y", "O"], 9: ["Y", "B"], 10: ["Y", "R"], 11: ["Y", "G"],
    }
    CORNER_COLORS = {
        0: ["W", "G", "O"], 1: ["W", "O", "B"], 2: ["W", "B", "R"], 3: ["W", "R", "G"],
        4: ["Y", "O", "G"], 5: ["Y", "B", "O"], 6: ["Y", "R", "B"], 7: ["Y", "G", "R"]
    }
    MOVES = {
        "x": ["x"],
        "x2": ["x", "x"],
        "x'": ["x", "x", "x"],

        "y": ["y"],
        "y2": ["y", "y"],
        "y'": ["y", "y", "y"],

        "F": ["F"],
        "F2": ["F", "F"],
        "F'": ["F", "F", "F"],

        "B": ["y", "y", "F", "y", "y"],
        "B2": ["y", "y", "F", "F", "y", "y"],
        "B'": ["y", "y", "F", "F", "F", "y", "y"],

        "R": ["y", "F", "y", "y", "y"],
        "R2": ["y", "F", "F", "y", "y", "y"],
        "R'": ["y", "F", "F", "F", "y", "y", "y"],

        "L": ["y", "y", "y", "F", "y"],
        "L2": ["y", "y", "y", "F", "F", "y"],
        "L'": ["y", "y", "y", "F", "F", "F", "y"],

        "U": ["x", "x", "x", "F", "x"],
        "U2": ["x", "x", "x", "F", "F", "x"],
        "U'": ["x", "x", "x", "F", "F", "F", "x"],

        "D": ["x", "F", "x", "x", "x"],
        "D2": ["x", "F", "F", "x", "x", "x"],
        "D'": ["x", "F", "F", "F", "x", "x", "x"]
    }

    def __init__(self):
        self.colors = {
            "up": [None] * 9,
            "down": [None] * 9,
            "front": [None] * 9,
            "back": [None] * 9,
            "right": [None] * 9,
            "left": [None] * 9,
        }

        self.orientation = [0, 0]
        self.edge = [[i, 0] for i in range(12)]
        self.corner = [[i, 0] for i in range(8)]

        self.start_counter = 0
        self.moves = []
        self.invert_moves = []

        self.virtual_start_counter = 0
        self.virtual_moves = []
        self.virtual_invert_moves = []

    def copy(self):
        new = Cube()

        new.edge = [e[:] for e in self.edge]
        new.corner = [c[:] for c in self.corner]
        new.orientation = self.orientation[:]

        new.start_counter = self.start_counter
        new.moves = self.moves[:]
        new.invert_moves = self.invert_moves[:]

        new.virtual_start_counter = self.virtual_start_counter
        new.virtual_moves = self.virtual_moves[:]
        new.virtual_invert_moves = self.virtual_invert_moves[:]

        return new

    def set_cube_from_letters(self, cube_set):
        """
        counter = 0
        for i in cube_set[0]:
            match i[0]:
                case "a":
                    self.edge[counter] = [0, int(i[1])]
                case "b":
                    self.edge[counter] = [1, int(i[1])]
                case "c":
                    self.edge[counter] = [2, int(i[1])]
                case "d":
                    self.edge[counter] = [3, int(i[1])]
                case "e":
                    self.edge[counter] = [4, int(i[1])]
                case "f":
                    self.edge[counter] = [5, int(i[1])]
                case "g":
                    self.edge[counter] = [6, int(i[1])]
                case "h":
                    self.edge[counter] = [7, int(i[1])]
                case "i":
                    self.edge[counter] = [8, int(i[1])]
                case "j":
                    self.edge[counter] = [9, int(i[1])]
                case "k":
                    self.edge[counter] = [10, int(i[1])]
                case "l":
                    self.edge[counter] = [11, int(i[1])]
            counter += 1
        """
        letter_to_num_edge = {
            "a": 0, "b": 1, "c": 2, "d": 3,
            "e": 4, "f": 5, "g": 6, "h": 7,
            "i": 8, "j": 9, "k": 10, "l": 11
        }
        counter = 0
        for i in cube_set[0]:
            self.edge[counter] = [letter_to_num_edge[i[0]], int(i[1])]
            counter += 1

        """   
               for i in cube_set[1]:
                   match i[0]:
                       case "A":
                           self.corner[counter] = [0, int(i[1])]
                       case "B":
                           self.corner[counter] = [1, int(i[1])]
                       case "C":
                           self.corner[counter] = [2, int(i[1])]
                       case "D":
                           self.corner[counter] = [3, int(i[1])]
                       case "E":
                           self.corner[counter] = [4, int(i[1])]
                       case "F":
                           self.corner[counter] = [5, int(i[1])]
                       case "G":
                           self.corner[counter] = [6, int(i[1])]
                       case "H":
                           self.corner[counter] = [7, int(i[1])]

                   counter += 1
               """
        letter_to_num_corner = {
            "A": 0, "B": 1, "C": 2, "D": 3,
            "E": 4, "F": 5, "G": 6, "H": 7
        }
        counter = 0
        for i in cube_set[1]:
            self.corner[counter] = [letter_to_num_corner[i[0]], int(i[1])]
            counter += 1

        """
        match cube_set[2][0]:
            case "alpha":
                self.orientation = [0, cube_set[2][1]]
            case "beta":
                self.orientation = [1, cube_set[2][1]]
            case "gamma":
                self.orientation = [2, cube_set[2][1]]
            case "delta":
                self.orientation = [3, cube_set[2][1]]
            case "epsilon":
                self.orientation = [4, cube_set[2][1]]
            case "zeta":
                self.orientation = [5, cube_set[2][1]]
        """
        letter_to_num_center = {
            "alpha": 0, "beta": 1, "gamma": 2,
            "delta": 3, "epsilon": 4, "zeta": 5
        }
        self.orientation = [letter_to_num_center[cube_set[2][0]], int(cube_set[2][1])]

    # ES NECESARIO PODER ELIMINAR ERRORES AL INTRODUCIR DATOS
    def set_cube_friendly(self):
        set_edge = []
        set_corner = []

        for _ in range(12):
            while True:
                a = input("Enter edge:")
                if all(ch in "abcdefghijkl01" for ch in a):
                    break

            set_edge.append(a)

        for _ in range(8):
            while True:
                a = input("Enter corner:")
                if all(ch in "ABCDEFGHl012" for ch in a):
                    break

            set_corner.append(a)

        while True:
            set_orientation_name = input("Enter face of reference:")
            if all(ch in "qwertyuiopasdfghjklñzxcvbnm" for ch in set_orientation_name):
                break

        while True:
            set_orientation_value = input("Enter orientation:")
            if all(ch in "0123" for ch in set_orientation_value):
                break

        set_orientation = [set_orientation_name, set_orientation_value]
        set_cube = [set_edge, set_corner, set_orientation]
        self.set_cube_from_letters(set_cube)

    def view_cube_set(self):
        print(self.edge)
        print(self.corner)
        print(self.orientation)

    def _reset_colors(self):
        self.colors = {
            "up": [None] * 9,
            "down": [None] * 9,
            "front": [None] * 9,
            "back": [None] * 9,
            "right": [None] * 9,
            "left": [None] * 9,
        }

    def _set_colors_edges(self):
        # Set up face

        for i, j in zip([1, 3, 5, 7], [0, 3, 1, 2]):
            if self.edge[j][1] == 0:
                self.colors["up"][i] = self.EDGE_COLORS[self.edge[j][0]][0]
            else:
                self.colors["up"][i] = self.EDGE_COLORS[self.edge[j][0]][1]

        # Set down face

        for i, j in zip([1, 3, 5, 7], [8, 9, 11, 10]):
            if self.edge[j][1] == 0:
                self.colors["down"][i] = self.EDGE_COLORS[self.edge[j][0]][0]
            else:
                self.colors["down"][i] = self.EDGE_COLORS[self.edge[j][0]][1]

        # Set front face

        for i, j in zip([1, 3, 5, 7], [2, 7, 6, 10]):
            if j == 2 or j == 10:
                if self.edge[j][1] == 0:
                    self.colors["front"][i] = self.EDGE_COLORS[self.edge[j][0]][1]
                else:
                    self.colors["front"][i] = self.EDGE_COLORS[self.edge[j][0]][0]
            else:
                if self.edge[j][1] == 0:
                    self.colors["front"][i] = self.EDGE_COLORS[self.edge[j][0]][0]
                else:
                    self.colors["front"][i] = self.EDGE_COLORS[self.edge[j][0]][1]

        # Set back face

        for i, j in zip([1, 3, 5, 7], [8, 4, 5, 0]):
            if j == 8 or j == 0:
                if self.edge[j][1] == 0:
                    self.colors["back"][i] = self.EDGE_COLORS[self.edge[j][0]][1]
                else:
                    self.colors["back"][i] = self.EDGE_COLORS[self.edge[j][0]][0]
            else:
                if self.edge[j][1] == 0:
                    self.colors["back"][i] = self.EDGE_COLORS[self.edge[j][0]][0]
                else:
                    self.colors["back"][i] = self.EDGE_COLORS[self.edge[j][0]][1]

        # Set right face

        for i, j in zip([1, 3, 5, 7], [5, 1, 9, 6]):
            if self.edge[j][1] == 0:
                self.colors["right"][i] = self.EDGE_COLORS[self.edge[j][0]][1]
            else:
                self.colors["right"][i] = self.EDGE_COLORS[self.edge[j][0]][0]

        # Set left face

        for i, j in zip([1, 3, 5, 7], [4, 11, 3, 7]):
            if self.edge[j][1] == 0:
                self.colors["left"][i] = self.EDGE_COLORS[self.edge[j][0]][1]
            else:
                self.colors["left"][i] = self.EDGE_COLORS[self.edge[j][0]][0]

    def _set_colors_corners(self):
        # Set up face

        for i, j in zip([0, 2, 6, 8], [0, 1, 3, 2]):
            if self.corner[j][1] == 0:
                self.colors["up"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

            elif self.corner[j][1] == 1:
                self.colors["up"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

            else:
                self.colors["up"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

        # Set down face

        for i, j in zip([0, 2, 6, 8], [5, 4, 6, 7]):
            if self.corner[j][1] == 0:
                self.colors["down"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

            elif self.corner[j][1] == 1:
                self.colors["down"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

            else:
                self.colors["down"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

        # Set front face

        for i, j in zip([0, 2, 6, 8], [3, 2, 7, 6]):
            if j == 3 or j == 6:
                if self.corner[j][1] == 0:
                    self.colors["front"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

                elif self.corner[j][1] == 1:
                    self.colors["front"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                else:
                    self.colors["front"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

            else:
                if self.corner[j][1] == 0:
                    self.colors["front"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                elif self.corner[j][1] == 1:
                    self.colors["front"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

                else:
                    self.colors["front"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

        # Set back face

        for i, j in zip([0, 2, 6, 8], [4, 5, 0, 1]):
            if j == 4 or j == 1:
                if self.corner[j][1] == 0:
                    self.colors["back"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

                elif self.corner[j][1] == 1:
                    self.colors["back"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                else:
                    self.colors["back"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

            else:
                if self.corner[j][1] == 0:
                    self.colors["back"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                elif self.corner[j][1] == 1:
                    self.colors["back"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

                else:
                    self.colors["back"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

        # Set right face

        for i, j in zip([0, 2, 6, 8], [1, 5, 2, 6]):
            if j == 1 or j == 6:
                if self.corner[j][1] == 0:
                    self.colors["right"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                elif self.corner[j][1] == 1:
                    self.colors["right"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

                else:
                    self.colors["right"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

            else:
                if self.corner[j][1] == 0:
                    self.colors["right"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

                elif self.corner[j][1] == 1:
                    self.colors["right"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                else:
                    self.colors["right"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

        # Set left face

        for i, j in zip([0, 2, 6, 8], [4, 0, 7, 3]):
            if j == 4 or j == 3:
                if self.corner[j][1] == 0:
                    self.colors["left"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                elif self.corner[j][1] == 1:
                    self.colors["left"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

                else:
                    self.colors["left"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

            else:
                if self.corner[j][1] == 0:
                    self.colors["left"][i] = self.CORNER_COLORS[self.corner[j][0]][1]

                elif self.corner[j][1] == 1:
                    self.colors["left"][i] = self.CORNER_COLORS[self.corner[j][0]][2]

                else:
                    self.colors["left"][i] = self.CORNER_COLORS[self.corner[j][0]][0]

    def _set_colors_centers(self):
        for i, j in zip(self.colors, ["W", "Y", "R", "O", "B", "G"]):
            self.colors[i][4] = j

    def set_colors(self):
        self.normalize_orientation()
        self._reset_colors()
        self._set_colors_edges()
        self._set_colors_corners()
        self._set_colors_centers()

    def count_moves(self):
        if self.start_counter == 0:
            self.moves = []
        self.start_counter = (self.start_counter + 1) % 2

    def set_invert_moves(self):
        self.invert_moves = []
        for i in reversed(self.moves):
            self.invert_moves.extend([i]*3)

    def normalize_orientation(self):
        old_orientation = self.orientation[:]

        if self.orientation[0] != 0:
            if self.orientation[1] in (1, 3):
                self.y()

            for _ in range(4):
                if self.orientation[0] == 0:
                    break
                self.x()

        for _ in range(4):
            if self.orientation[1] == 0:
                break
            self.y()

        return old_orientation

    def y(self):
        # Edges
        edge_ring = [None]*3

        for i in range(3):
            chunk = self.edge[i*4: i*4 + 4]
            edge_ring[i] = [chunk[-1]] + chunk[:-1]

        self.edge = []
        for i in edge_ring:
            self.edge += i[:]

        # Cornes
        corner_ring = [None]*2

        for i in range(2):
            chunk = self.corner[i*4: i*4 + 4]
            corner_ring[i] = [chunk[-1]] + chunk[:-1]

        self.corner = []
        for i in corner_ring:
            self.corner += i[:]

        # Centers
        self.orientation[1] = (self.orientation[1] + 3) % 4

        # Add the move to the move counters
        if self.start_counter == 1:
            self.moves.append("y")

    def x(self):
        # Edges

        edges = [None]*12
        edges_perm = [2, 6, 10, 7, 3, 1, 9, 11, 0, 5, 8, 4]

        for j, i in zip(range(len(edges_perm)), edges_perm):
            edges[j] = self.edge[i]

        self.edge[:] = edges[:]

        # Corners

        corners = [None]*8
        corners_perm = [3, 2, 6, 7, 0, 1, 5, 4]

        for j, i in zip(range(len(corners_perm)), corners_perm):
            corners[j] = self.corner[i]

        self.corner[:] = corners[:]

        # Centers
        match self.orientation[0]:
            case 0:
                match self.orientation[1]:
                    case 0:
                        self.orientation = [3, 2]
                    case 1:
                        self.orientation = [4, 2]
                    case 2:
                        self.orientation = [1, 2]
                    case 3:
                        self.orientation = [2, 2]

            case 1:
                match self.orientation[1]:
                    case 0:
                        self.orientation = [0, 0]
                    case 1:
                        self.orientation = [4, 1]
                    case 2:
                        self.orientation = [5, 0]
                    case 3:
                        self.orientation = [2, 3]

            case 2:
                match self.orientation[1]:
                    case 0:
                        self.orientation = [0, 1]
                    case 1:
                        self.orientation = [1, 1]
                    case 2:
                        self.orientation = [5, 3]
                    case 3:
                        self.orientation = [3, 3]

            case 3:
                match self.orientation[1]:
                    case 0:
                        self.orientation = [0, 2]
                    case 1:
                        self.orientation = [2, 1]
                    case 2:
                        self.orientation = [5, 2]
                    case 3:
                        self.orientation = [4, 3]

            case 4:
                match self.orientation[1]:
                    case 0:
                        self.orientation = [0, 3]
                    case 1:
                        self.orientation = [3, 1]
                    case 2:
                        self.orientation = [5, 1]
                    case 3:
                        self.orientation = [1, 3]

            case 5:
                match self.orientation[1]:
                    case 0:
                        self.orientation = [3, 0]
                    case 1:
                        self.orientation = [2, 0]
                    case 2:
                        self.orientation = [1, 0]
                    case 3:
                        self.orientation = [4, 0]

    # Add the move to the move counters
        if self.start_counter == 1:
            self.moves.append("x")

    def F(self):
        # Edges
        edges = [e[:] for e in self.edge]

        edges[2] = self.edge[7][:]
        edges[6] = self.edge[2][:]
        edges[10] = self.edge[6][:]
        edges[7] = self.edge[10][:]

        if self.orientation[0] in (0, 5):
            if self.orientation[1] in (0, 2):
                for i in (2, 6, 10, 7):
                    edges[i][1] = (edges[i][1] + 1) % 2
            else:
                # orientations don`t change because te front face has the lowest priority
                pass
        else:
            if self.orientation[1] in (0, 2):
                # orientations don`t change because te front face has the bigest priority
                pass
            else:
                if self.orientation[0] in (1, 3):
                    # orientations don`t change because te front face has the lowest priority
                    pass
                else:
                    for i in (2, 6, 10, 7):
                        edges[i][1] = (edges[i][1] + 1) % 2

        self.edge = [e[:] for e in edges]

        # Corners

        corners = [c[:] for c in self.corner]

        corners[3] = self.corner[7][:]
        corners[2] = self.corner[3][:]
        corners[6] = self.corner[2][:]
        corners[7] = self.corner[6][:]

        if self.orientation[0] in (0, 5):
            corners[6][1] = (corners[6][1] + 1) % 3
            corners[7][1] = (corners[7][1] + 2) % 3
            corners[3][1] = (corners[3][1] + 1) % 3
            corners[2][1] = (corners[2][1] + 2) % 3
        else:
            if self.orientation[1] in (0, 2):
                pass
            else:
                corners[6][1] = (corners[6][1] + 2) % 3
                corners[7][1] = (corners[7][1] + 1) % 3
                corners[3][1] = (corners[3][1] + 2) % 3
                corners[2][1] = (corners[2][1] + 1) % 3

        self.corner = [c[:] for c in corners]

        # Add the move to the move counters
        if self.start_counter == 1:
            self.moves.append("F")

    # Se considera que alg tiene la forma "F U B L' F2"
    def apply_algorithm(self, alg):
        alg = alg.split()
        simplified_alg = []

        for i in alg:
            simplified_alg += self.MOVES[i]

        for i in simplified_alg:
            if i == "x":
                self.x()
            if i == "y":
                self.y()
            if i == "F":
                self.F()

    """
    def apply_algorithm(self, alg):
        valid_moves = {"x", "y", "F", "B", "L", "R", "U", "D"}
        primitive_expansion = {
            "x": ["x"],
            "y": ["y"],
            "F": ["F"],
            "B": ["y", "y", "F", "y", "y"],
            "L": ["y", "y", "y", "F", "y"],
            "R": ["y", "F", "y", "y", "y"],
            "U": ["x", "x", "x", "F", "x"],
            "D": ["x", "F", "x", "x", "x"],
        }

        def parse_algorithm_string(alg_str):
            s = "".join(alg_str.split())
            tokens = []
            i = 0
            while i < len(s):
                move = s[i]
                if move not in valid_moves:
                    raise ValueError(f"Invalid move '{move}' at position {i}")

                suffix = ""
                if i + 1 < len(s) and s[i + 1] in ("2", "'"):
                    suffix = s[i + 1]
                    i += 1

                tokens.append((move, suffix))
                i += 1
            return tokens

        def parse_algorithm_iterable(alg_items):
            items = list(alg_items)
            compact_items = []
            for item in items:
                if not isinstance(item, str):
                    raise TypeError("Algorithm iterable must contain only strings")
                stripped = "".join(item.split())
                if stripped:
                    compact_items.append(stripped)

            if all(len(item) <= 1 for item in compact_items):
                return parse_algorithm_string("".join(compact_items))

            tokens = []
            for item in compact_items:
                if len(item) == 1 and item in valid_moves:
                    tokens.append((item, ""))
                elif len(item) == 2 and item[0] in valid_moves and item[1] in ("2", "'"):
                    tokens.append((item[0], item[1]))
                else:
                    raise ValueError(f"Invalid token '{item}'")
            return tokens

        if isinstance(alg, str):
            tokens = parse_algorithm_string(alg)
        else:
            tokens = parse_algorithm_iterable(alg)

        moves_to_execute = []
        for move, suffix in tokens:
            turns = 1
            if suffix == "2":
                turns = 2
            elif suffix == "'":
                turns = 3
            moves_to_execute.extend(primitive_expansion[move] * turns)

        dispatcher = {"x": self.x, "y": self.y, "F": self.F}
        for move in moves_to_execute:
            dispatcher[move]()
    """
