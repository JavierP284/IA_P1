#Utilizar operadores con una funcion no matematica
print("Concatenar cadenas")
nom = input("¿Me puedes dar tu nombre por favor? ") #Solicitar los datos para guardarlos
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + nom + " " + ape + ".") #Utilizar + para concatenar cadenas

#Utilizar *
print("Replicacion")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="") #Utilizar * para que se reproduzca la cadena el numero de veces indicado
print("+" + 10 * "-" + "+")