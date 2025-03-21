import numpy as np
from scipy.linalg import lu

def lu_decomposition(A):
    """
    Realiza la factorización LU o PALU de la matriz A.
    Utiliza la biblioteca scipy para manejar la permutación.
    Retorna las matrices P, L, U.
    """
    try:
        # Verificar si la matriz es singular
        if np.linalg.det(A) == 0:
            raise ValueError("La matriz es singular y no admite factorización LU.")

        # Realizar la factorización LU
        P, L, U = lu(A)
        print("\nMatriz P (Permutación):")
        print(P)
        print("\nMatriz L (Triangular Inferior):")
        print(L)
        print("\nMatriz U (Triangular Superior):")
        print(U)
        return P, L, U
    except Exception as e:
        print(f"Error al realizar la factorización LU: {e}")
        return None, None, None

def forward_substitution(L, b):
    """
    Resolución de Ly = b (sustitución hacia adelante).
    """
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        try:
            y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
        except ZeroDivisionError:
            raise ValueError("División por cero en la sustitución hacia adelante.")
    return y

def backward_substitution(U, y):
    """
    Resolución de Ux = y (sustitución hacia atrás).
    """
    n = len(y)
    x = np.zeros(n)
    for i in reversed(range(n)):
        try:
            x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
        except ZeroDivisionError:
            raise ValueError("División por cero en la sustitución hacia atrás.")
    return x

def solve_lu(A, b):
    """
    Resuelve el sistema de ecuaciones Ax = b usando factorización LU.
    """
    P, L, U = lu_decomposition(A)
    if P is None:
        raise ValueError("No se pudo realizar la factorización LU.")

    # Resolver el sistema Ly = Pb (sustitución hacia adelante)
    Pb = np.dot(P, b)
    y = forward_substitution(L, Pb)

    # Resolver el sistema Ux = y (sustitución hacia atrás)
    x = backward_substitution(U, y)

    return x
