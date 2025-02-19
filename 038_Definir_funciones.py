def message(): #Declarar la función
    valor=int(input("Ingresar valor: ")) #Colocar el funconamiento
    print("Tu valor es:" ,valor)

print("Inicia aqui.")
message() #Llamar a la función
print("Termina aqui.")

#Funcion con argumentos
def introduction(first_name, last_name): #Asignar los parametros
    print("Hola, mi nombre es", first_name, last_name) #Solicitar los datos

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

