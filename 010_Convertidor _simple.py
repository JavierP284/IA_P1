#Convertidor de Kilometros a Millas
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61 #Se colocan las formulas para pasar de una sistema a otro en su respectiva variable
kilometers_to_miles = kilometers/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros") #Se coloca el numero de decimales que queremos que nos muestre con la funcion round
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")