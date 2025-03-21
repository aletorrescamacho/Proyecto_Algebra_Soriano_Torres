import numpy as np
from jacobi import jacobi
from lu import solve_lu
from gauss_jordan import gauss_jordan

def input_seguro(mensaje, tipo=float):
    while True:
        try:
            valor = input(mensaje)
            return tipo(valor)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un valor válido.")

def regresar_al_menu():
    """
    Ofrece la opción de regresar al menú principal o finalizar la simulación.
    """
    print("\nPresione Enter para volver al menú principal o escriba 'salir' para finalizar la simulación...")
    opcion = input().strip().lower()
    if opcion == 'salir':
        print("Finalizando la simulación. ¡Hasta luego!")
        exit()

def ingresar_matriz():
    print("\nSeleccione el tamaño de la matriz:")
    print("0) Finalizar la simulación")
    print("1) 2x2")
    print("2) 3x3")
    print("3) 4x4")
    
    opcion = input_seguro("Opción: ", int)

    if opcion == 0:
        print("Finalizando la simulación. ¡Hasta luego!")
        exit()
    elif opcion == 1:
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
            matriz[i][j] = input_seguro(f"A[{i+1}][{j+1}]: ")
        vector_b[i] = input_seguro(f"b[{i+1}]: ")

    return matriz, vector_b

def seleccionar_metodo():
    while True:
        print("\nSeleccione el método de resolución:")
        print("0) Volver al menú principal")
        print("1) Factorización LU")
        print("2) Método de Jacobi")
        print("3) Solución Directa por Gauss-Jordan")
        print("4) Finalizar la simulación")
        metodo = input_seguro("Opción: ", int)

        if metodo == 0:
            return None
        elif metodo == 4:
            print("Finalizando la simulación. ¡Hasta luego!")
            exit()
        elif metodo in [1, 2, 3]:
            return metodo
        else:
            print("Opción no válida. Intente nuevamente.")

def main():
    print("¡Hola! Bienvenido al programa de resolución de sistemas de ecuaciones lineales.")
    while True:
        matriz, vector_b = ingresar_matriz()
        
        metodo = seleccionar_metodo()
        if metodo is None:
            continue

        print("\nMatriz A ingresada:")
        print(matriz)
        print("\nVector b ingresado:")
        print(vector_b)
        print(f"\nMétodo seleccionado: {metodo}")

        if metodo == 1:
            try:
                solucion = solve_lu(matriz, vector_b)
                print("\nSolución encontrada por LU:")
                print(solucion)
            except ValueError as e:
                print(f"Error: {e}")

        elif metodo == 2:
            print("\nSeleccione la condición inicial:")
            print("0) Volver al menú principal")
            print("1) Condición clásica (0, 0, ..., 0)")
            print("2) Condición personalizada")
            condicion = input_seguro("Opción: ", int)

            if condicion == 0:
                continue

            if condicion == 1:
                x0 = None
            elif condicion == 2:
                x0 = []
                for i in range(len(vector_b)):
                    x0.append(input_seguro(f"x[{i+1}]: "))
                x0 = np.array(x0)
            else:
                print("Opción no válida. Usando condición clásica.")
                x0 = None

            try:
                solucion = jacobi(matriz, vector_b, x0)
                print("\nSolución encontrada por Jacobi:")
                print(solucion)
            except ValueError as e:
                print(f"Error: {e}")

        elif metodo == 3:
            try:
                solucion = gauss_jordan(matriz, vector_b)
                print("\nSolución encontrada por Gauss-Jordan:")
                print(solucion)
            except ValueError as e:
                print(f"Error: {e}")

        regresar_al_menu()

if __name__ == "__main__":
    main()
