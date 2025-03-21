import numpy as np

def ingresar_matriz():
    print("Seleccione el tamaño de la matriz:")
    print("1) 2x2")
    print("2) 3x3")
    print("3) 4x4")
    opcion = int(input("Opción: "))

    if opcion == 1:
        n = 2
    elif opcion == 2:
        n = 3
    elif opcion == 3:
        n = 4
    else:
        print("Opción no válida. Intente nuevamente.")
        return ingresar_matriz()

    matriz = np.zeros((n, n))
    vector_b = np.zeros(n)

    print(f"\nIngrese los coeficientes de la matriz {n}x{n}:")
    for i in range(n):
        for j in range(n):
            matriz[i][j] = float(input(f"A[{i+1}][{j+1}]: "))
        vector_b[i] = float(input(f"b[{i+1}]: "))

    return matriz, vector_b

def seleccionar_metodo():
    print("\nSeleccione el método de resolución:")
    print("1) Factorización LU")
    print("2) Método de Jacobi")
    print("3) Solución Directa por Gauss-Jordan")
    metodo = int(input("Opción: "))
    return metodo

def main():
    matriz, vector_b = ingresar_matriz()
    metodo = seleccionar_metodo()

    print("\nMatriz A ingresada:")
    print(matriz)
    print("\nVector b ingresado:")
    print(vector_b)
    print(f"\nMétodo seleccionado: {metodo}")

if __name__ == "__main__":
    main()
