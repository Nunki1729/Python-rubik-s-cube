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

    @staticmethod
    def _rotate_90(face):
        return [face[6], face[3], face[0],
                face[7], face[4], face[1],
                face[8], face[5], face[2]]

    def _rotate(self, face, k):  # k = 0,1,2,3
        for _ in range(k % 4):
            face = self._rotate_90(face)
        return face

    def set_colors(self):
        # Save real cube state (avoid mutating the cube)
        old_state = ([e[:] for e in self.edge],
                     [c[:] for c in self.corner],
                     self.orientation[:])

        # Face-mapping tables for the original orientation
        #    face_color0: which face is "up" for a given orientation[0]
        #    face_color1_*: lateral faces based on orientation[1] and dominant color
        face_color0 = {
            0: "up",
            1: "back",
            2: "right",
            3: "front",
            4: "left",
            5: "down"
        }
        inverse_face_color0 = {
            0: "down",
            1: "front",
            2: "left",
            3: "back",
            4: "right",
            5: "up"
        }
        face_color1_red = {
            0: "front",
            1: "left",
            2: "back",
            3: "right"
        }
        inverse_face_color1_red = {
            0: "back",
            1: "right",
            2: "front",
            3: "left"
        }
        face_color1_white = {
            0: "up",
            1: "left",
            2: "down",
            3: "right"
        }
        inverse_face_color1_white = {
            0: "down",
            1: "right",
            2: "up",
            3: "left"
        }

        # Normalize, compute colors, and snapshot the normalized colors
        self._virtual_count_moves()
        old_orientation = self.normalize_orientation()
        self._reset_colors()
        self._set_colors_edges()
        self._set_colors_corners()
        self._set_colors_centers()
        preoriented_colors = {k: v[:] for k, v in self.colors.items()}

        # Remap colors back to the original orientation
        self.colors["up"] = preoriented_colors[face_color0[old_orientation[0]]]
        self.colors["down"] = preoriented_colors[inverse_face_color0[old_orientation[0]]]

        if old_orientation[0] in (0, 5):
            self.colors["front"] = preoriented_colors[face_color1_red[old_orientation[1]]]
            self.colors["back"] = preoriented_colors[inverse_face_color1_red[old_orientation[1]]]
            self.colors["left"] = preoriented_colors[inverse_face_color1_red[(old_orientation[1] + 1) % 4]]
            self.colors["right"] = preoriented_colors[face_color1_red[(old_orientation[1] + 1) % 4]]

        else:
            self.colors["front"] = preoriented_colors[face_color1_white[old_orientation[1]]]
            self.colors["back"] = preoriented_colors[inverse_face_color1_white[old_orientation[1]]]
            self.colors["left"] = preoriented_colors[inverse_face_color1_white[(old_orientation[1] + 1) % 4]]
            self.colors["right"] = preoriented_colors[face_color1_white[(old_orientation[1] + 1) % 4]]

        # Rotate the faces
        rotations_y = {
            "up": 1,
            "down": 3,
            "front": 1,
            "back": 1,
            "right": 1,
            "left": 1
        }
        rotations_x = {
            "up": 0,
            "down": 2,
            "front": 2,
            "back": 0,
            "right": 1,
            "left": 3
        }
        self._virtual_set_invert_moves()
        for move in self.virtual_invert_moves:
            if move == "y":
                for j in list(self.colors.keys()):
                    self.colors[j] = self._rotate(self.colors[j], rotations_y[j])
            elif move == "x":
                for j in list(self.colors.keys()):
                    self.colors[j] = self._rotate(self.colors[j], rotations_x[j])

        self._virtual_count_moves()

        # Restore the real cube state
        self.edge, self.corner, self.orientation = old_state

    def count_moves(self):
        if self.start_counter == 0:
            self.moves = []
        self.start_counter = (self.start_counter + 1) % 2

    def set_invert_moves(self):
        self.invert_moves = []
        for i in reversed(self.moves):
            self.invert_moves.extend([i]*3)

    def _virtual_count_moves(self):
        # The virtual counter won't affect the real one
        """self.start_counter = (self.start_counter + 1) % 2"""

        if self.virtual_start_counter == 0:
            self.virtual_moves = []
        self.virtual_start_counter = (self.virtual_start_counter + 1) % 2

    def _virtual_set_invert_moves(self):
        self.virtual_invert_moves = []
        for i in reversed(self.virtual_moves):
            self.virtual_invert_moves.extend([i]*3)

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

        if self.virtual_start_counter == 1:
            self.virtual_moves.append("y")

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

        if self.virtual_start_counter == 1:
            self.virtual_moves.append("x")

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
            corners[6][1] = (corners[6][1] + 2) % 3
            corners[7][1] = (corners[7][1] + 1) % 3
            corners[3][1] = (corners[3][1] + 2) % 3
            corners[2][1] = (corners[2][1] + 1) % 3

        self.corner = [c[:] for c in corners]

    def apply_algorithm(self, alg):
        if not isinstance(alg, list):
            alg = list(alg)

        moves_a = []
        moves_b = []

        for i in range(len(alg)):
            match alg[i]:
                case "2":
                    moves_a.extend(alg[i - 1])
                case "'":
                    moves_a.extend(alg[i - 1] * 2)
                case "x":
                    moves_a.extend("x")
                case "y":
                    moves_a.extend("y")
                case "F":
                    moves_a.extend("F")
                case "B":
                    moves_a.extend("B")
                case "L":
                    moves_a.extend("L")
                case "R":
                    moves_a.extend("R'")
                case "U":
                    moves_a.extend("U")
                case "D":
                    moves_a.extend("D")

        for i in range(len(moves_a)):
            match moves_a[i]:
                case "x":
                    moves_b.extend("x")
                case "y":
                    moves_b.extend("y")
                case "F":
                    moves_b.extend("F")
                case "B":
                    moves_b.extend(list("y2Fy2"))
                case "L":
                    moves_b.extend(list("yyyFy"))
                case "R":
                    moves_b.extend(list("yFyyy"))
                case "U":
                    moves_b.extend(list("xxxFx"))
                case "D":
                    moves_b.extend(list("xFxxx"))

        for i in moves_b:
            if i == "x":
                self.x()
            elif i == "y":
                self.y()
            elif i == "F":
                self.F()
