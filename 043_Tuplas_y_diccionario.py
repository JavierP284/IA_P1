school_class = {} #Crear la clase

while True:
    name = input("Ingresa el nombre del estudiante: ") #Solicitar el nombre del estudiante
    if name == '': #Si el nombre esta vacio se termina el programa
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): ")) #Solicitar una calificacion
    if score not in range(0, 11): #Asiganr una condicion de rango para las calificacion que pueden ser validas
	    break
    
    if name in school_class:
        school_class[name] += (score,) #Si el estudiante ya existe se suma su calificacion
    else:
        school_class[name] = (score,) #Si no existe se crea una nueva entrada
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter) #Se calcula el promedio
