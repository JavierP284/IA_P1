def is_year_leap(year): #Declarar la funcion y el argumento que permitira tomar de fuera
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #Funcion para determinar si es bisiesto
        return True
    return False

test_data = [1600, 2000, 2023, 1900] #Años para hacer la prueba
test_results = [True, True, False, False] #Test de funcionamiento

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido") #Comprobacion

yr = int(input("Ingresa un año: "))
result = is_year_leap(yr)
if result == True:
    print("Año bisiesto")
else:
    print("Año común")
 
