c0 = int(input("Ingresa un número natural: "))

if c0 <= 0:
    print("El número debe ser un entero positivo.")
else:
    steps = 0  # Contador de pasos

    while c0 != 1:
        print(c0)  # Imprimir el valor actual de c0
        if c0 % 2 == 0:
            c0 //= 2  # Si es par, se divide por 2
        else:
            c0 = 3 * c0 + 1  # Si es impar, se aplica 3*c0 + 1
        steps += 1  # Incrementar el contador de pasos

    print(c0)  # Imprimir el último valor (1)
    print("Pasos totales:", steps)