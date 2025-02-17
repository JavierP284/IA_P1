#Programa que compara numeros
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: ")) #Solicitar los 3 numeros
num3 = int(input("Ingresa el tercer numero: "))

num_grd = num1 #Suponer que el numero mas grande es el numero 1

if num2 > num_grd: #Comparar el numero 2 con el numero mas grande
    num_grd = num2

if num3 > num_grd: #Comparar el numero 3 con el dato guardado en el mas grande
    num_grd = num3

print("El numero mas grande es: " , num_grd) #Mostrar el numero mas grande de los 3