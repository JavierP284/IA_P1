def liters_100km_to_miles_gallon(liters): #Funcion para convertir litros/100km a millas/galon
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles/gallons

def miles_gallon_to_liters_100km(miles): #Convertir millas por galon a litros 
    km = (miles * 1609.344) / 1000
    liters_per_100km = 100 / km * 3.785411784
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9)) #Diferentes pruebas para demostrar el funcionamiento
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))