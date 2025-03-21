import numpy as np

def es_diagonal_dominante(A):
    """
    Verifica si la matriz A es diagonalmente dominante.
    """
    n = len(A)
    for i in range(n):
        suma = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= suma:
            return False
    return True

def reordenar_diagonal_dominante(A, b):
    """
    Intenta reordenar la matriz A para que sea diagonalmente dominante.
    """
    n = len(A)
    indices = list(range(n))

    for i in range(n):
        for j in range(i, n):
            suma = sum(abs(A[j][k]) for k in range(n) if k != i)
            if abs(A[j][i]) > suma:
                # Intercambiar filas
                A[[i, j]] = A[[j, i]]
                b[i], b[j] = b[j], b[i]
                break
    return A, b

def jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Método de Jacobi para resolver el sistema Ax = b.
    """
    n = len(A)

    # Verificar si la matriz ya es diagonalmente dominante
    if not es_diagonal_dominante(A):
        print("La matriz no es diagonalmente dominante. Intentando reordenar...")
        A, b = reordenar_diagonal_dominante(A, b)
        print("\nMatriz reordenada para ser diagonalmente dominante:")
        print(A)
        print("\nVector b reordenado:")
        print(b)
        if not es_diagonal_dominante(A):
            raise ValueError("No se pudo obtener una matriz diagonalmente dominante.")

    # Condición inicial
    if x0 is None:
        x0 = np.zeros(n)

    x = np.copy(x0)

    print("\nIteraciones del método de Jacobi:")
    for iteracion in range(max_iter):
        x_new = np.copy(x)

        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i][i]

        # Mostrar la iteración actual
        print(f"Iteración {iteracion + 1}: {x_new}")

        # Verificar convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"\nConvergió en {iteracion + 1} iteraciones.")
            return x_new

        x = np.copy(x_new)

    raise ValueError("El método de Jacobi no convergió en el número máximo de iteraciones.")
