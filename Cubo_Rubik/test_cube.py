# test_cube.py
import random
import time
from CuboRubik import Cube  # Importa tu clase Cube desde cube.py

def random_algorithm(length=20):
    """Genera una secuencia aleatoria de movimientos tipo Rubik."""
    moves = ["U", "D", "F", "B", "R", "L"]
    suffixes = ["", "2", "'"]
    return [random.choice(moves) + random.choice(suffixes) for _ in range(length)]

def inverse_algorithm(alg):
    """Devuelve la secuencia inversa para deshacer el algoritmo."""
    inverse_map = {"": "'", "2": "2", "'": ""}
    return [move[0] + inverse_map[move[1:]] for move in reversed(alg)]

def test_cube_performance(cube_class, num_tests=1000, alg_length=20):
    """Mide el tiempo y comprueba la corrección de tu clase Cube."""
    total_time = 0
    errors = 0

    for i in range(num_tests):
        c = cube_class()
        alg = random_algorithm(alg_length)
        inv = inverse_algorithm(alg)

        start_time = time.time()
        c.algorithm(alg)
        c.algorithm(inv)
        end_time = time.time()

        total_time += (end_time - start_time)

        # Verificación: el cubo debería volver a estado resuelto
        if c != cube_class():
            errors += 1

    print(f"Se hicieron {num_tests} pruebas con algoritmos de {alg_length} movimientos.")
    print(f"Tiempo total: {total_time:.4f} s, promedio por prueba: {total_time/num_tests:.6f} s")
    print(f"Errores detectados: {errors}")

if __name__ == "__main__":
    # Ejecuta la prueba con 500 secuencias de 50 movimientos cada una
    test_cube_performance(Cube, num_tests=10000, alg_length=1000)
