year = int(input("Introduce un año: ")) #Solicitar año

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano") #Si el año es menor a 1582
else:
    if year % 4 != 0: #Año no divisible entre 4
        print("Año Común") 
    elif year % 100 != 0: #Año no divisible entre 100
        print("Año Bisiesto") 
    elif year % 400 != 0: #Año no divisible entre 400
        print("Año Común")
    else:
        print("Año Bisiesto") #Cualquier situacion diferente a las anteriores