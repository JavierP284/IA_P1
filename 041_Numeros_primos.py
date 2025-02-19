def is_prime(num):
    if num <2: #Ya que 0 y 1 no son primos
            return False
    for i in range(2, int(num ** 0.5) + 1):  # Solo verificamos hasta la raíz cuadrada
        if num % i == 0:  # Si es divisible por algún número, no es primo
            return False
    return True

print("Numeros primos: ") #Imprimir los numeros primos solamente
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
