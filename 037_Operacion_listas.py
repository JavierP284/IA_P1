my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] #Declaracion de la lista
unique_list = []

for num in my_list:
    if num not in unique_list: #Funcion para eliminar elementos repetidos
        unique_list.append(num)

print("La lista con elementos únicos:") #Imprimir la lista sin numeros repetidos
print(unique_list)