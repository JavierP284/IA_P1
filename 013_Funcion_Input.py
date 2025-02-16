#Utilizar Inputt para solicitar informacion al usuario
print("Dime lo que sea...")
anything = input() #Solicitar texto al usuario paa guardarlo
print("Hmm...", anything, "... ¿en serio?")

#Asignar Valor al Input
print("\n Input con Valor Pre-cargado")
anything = input("Dime lo que sea...")#Se le pude  asignar un valor al input y estte no dara oportunidad de que el usuario guarde algo
print("Hmm...", anything, "...¿en serio?") #No se puede usar un dato guardado en el inpu para operaciones matematicas

#Guardar el valor ingresado como flotante
print("\nGuardar el valor como flotante")
anything = float(input("Ingresa un número: ")) #Para que funcione una operacion tiene que guardarse el valor como flotante
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something) #Dara el resultado numerico sin mosttrar error