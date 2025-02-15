#Ejercicio para evaluar expresion 3x^3 - 2x^2 + 3x - 1 con diferentes valores de x
x =  0 #Se define el valor de x
x = float(x) #Se asegura que x sea de tipo flottante
y = 3*x**3 - 2*x**2 + 3*x -1  #se coloca la expresion
print("y =", y) #Se imprime el resultado de la evaluacion

#Se repite con diferentes valores de x
x =  1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x -1
print("y =", y)

x =  -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x -1
print("y =", y)
