#Declarar la lista
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: ")) #Solicitar el numero de elementos que se agregaran a la lista

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: ")) #Solicitar los valores dentro de un bucle para llenar el numero solicitado
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] #Funcion para ordenar los numeros

print("\nOrdenada:") #Mostrar la lista ordenada
print(my_list)
