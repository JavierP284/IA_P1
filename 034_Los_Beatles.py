# paso 1
beatles = [] #Crear la lista vacia
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon") #Insertar a los 3 primeros a la lista
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for member in ["Stu Sutcliffe", "Pete Best"]: #Solicitar que el usuario agregue a los siguientes 2
    beatles.append(input(f"Agrega a {member}: "))
print("Paso 3:", beatles)

# paso 4
del beatles[-2:] #Eliminar a los ultimos 2 de la lista
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr") #Agregar a Ringo Starr al inicio de la lista
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
