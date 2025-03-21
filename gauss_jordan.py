import numpy as np

def gauss_jordan(A, b):
    """
    Método de Gauss-Jordan para resolver el sistema Ax = b.
    Elimina las variables escalonando la matriz aumentada.
    """
    n = len(b)
    # Crear la matriz aumentada [A|b]
    Ab = np.hstack((A, b.reshape(-1, 1)))
    print("\nMatriz aumentada inicial:")
    print(Ab)

    # Eliminación Gauss-Jordan
    for i in range(n):
        # Verificar si el pivote es cero
        if Ab[i, i] == 0:
            for j in range(i + 1, n):
                if Ab[j, i] != 0:
                    # Intercambiar filas
                    Ab[[i, j]] = Ab[[j, i]]
                    break

        # Hacer que el pivote sea 1 dividiendo toda la fila
        pivot = Ab[i, i]
        Ab[i] = Ab[i] / pivot
        print(f"\nFila {i+1} escalonada (pivote = {pivot}):")
        print(Ab)

        # Hacer ceros en la columna actual para las demás filas
        for j in range(n):
            if j != i:
                factor = Ab[j, i]
                Ab[j] = Ab[j] - factor * Ab[i]
                print(f"\nEliminando elemento en la fila {j+1}, columna {i+1} (factor = {factor}):")
                print(Ab)

    # La solución está en la última columna de la matriz aumentada
    x = Ab[:, -1]
    print("\nSolución del sistema:")
    print(x)
    return x
