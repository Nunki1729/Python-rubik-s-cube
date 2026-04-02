# Rubik's Cube Python Library

This Python library provides a representation of the **3x3 Rubik's Cube** and tools to manipulate it programmatically.  
It includes:

- Cube representation (edges, corners, orientation)  
- Cube moves (`U`, `D`, `F`, `B`, `R`, `L` and their variants)  
- Algorithm execution  
- White cross solving helper (in development)  
- Cube testing utilities  

This project is aimed at learning, experimentation, and building more advanced Rubik's Cube algorithms.


## Features

- Full internal representation of edges and corners  
- Orientation tracking  
- Apply arbitrary algorithms or predefined sequences (`ALGORITHMS`)  
- Copying and resetting cubes  
- Convert between letter-based and numeric-based cube representations  
- White cross solving method (`_solve_white_cross`)  (in development)
- Test scripts to verify correctness and performance


## Installation

Simply copy the `CuboRubik.py` file into your project directory.  
No external dependencies are required.


## Usage Example

```python
from CuboRubik import Cube

# Create a new cube
cube = Cube()

# Apply a sequence of moves
cube.algorithm(["U", "R", "F2", "L'", "D"])

# Reset the cube
cube.set_cube()  # Sets it to the solved state

# Display the cube colors
colors = cube.set_colors()
print(colors)
```
## Test Scripts

Several test scripts are included:

  - test_cube.py – tests performance and correctness with random algorithms

  - test_movimientos.py – verifies the correctness of move sequences

  - test_cruz_blanca.py – checks the _solve_white_cross method

To run the tests:
```python
python3 test_cube.py
python3 test_movimientos.py
python3 test_cruz_blanca.py
```


## Cube Representation

  - Edges: letters a-l with orientation 0 or 1

  - Corners: letters A-H with orientation 0-2

  - Orientation: tuple (center_color, rotation)

The library uses an absolute base orientation (alpha, 0) to define positions consistently.


## Notes

- This is a learning and experimental library.

- Currently, the library only provides basic move manipulation and white cross solving.

-  Future improvements may include:

      · Adding memory to store cube states and move history

      · More solving methods

      · A set_cube_friendly() function for easier cube setup

      · A better representation of the cube

## License

This project is licensed under the **GNU General Public License v3.0** (GPL-3.0).  
See the [LICENSE](./LICENSE) file for details.

## Author

© 2026 Javier Santiago (Nunki1729)  
Contact: cocousnusu@gmail.com or GitHub: [Nunki1729](https://github.com/Nunki1729)
