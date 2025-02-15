#Suma
print("Suma")
print(2+2)

#Exponencial
print("\nExponencial")
print(2 ** 3)
print(2 ** 3.) #si son 2 enteros el resultado es entero, si uno es flotnte el resultado tambien
print(2. ** 3)
print(2. ** 3.)

#Multiplicacion
print("\nMultiplicacion")
print(2 * 3)
print(2 * 3.) #si son 2 enteros el resultado es entero, si uno es flotnte el resultado tambien
print(2. * 3)
print(2. * 3.)

#Division
print("\nDivision")
print(6 / 3)
print(6 / 3.) #Siempre es resultado flotante
print(6. / 3)
print(6. / 3.)

#Division entera
print("\nDivision Entera")
print(6 // 3)
print(6 // 3.) #Si es division entre enteros el resultado es entero, en cualquier otro caso es flotante
print(6. // 3)
print(6. // 3.)
print(6 // 4) #Siempre redondea hacia abajo
print(-6 // 4) #Si uno es negativo redondea al valor inferior entero
print(6. / 4) #Si se usa division normal si da decimales
#Nunca hay que dividir entre 0

#Residuo entero
print("\nResiduo Entero")
print(14 % 4) #Te da el residuo de la division para dare un valor entero

#Prioridades
print("\nPrioridades de los operadores")
print(2 ** 2 ** 3) #Siguen la jerarquia de operaciones, ademas tiene un enlazado de izquierda a derecha
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)