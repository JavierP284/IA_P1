#Calcular la hora a la que finaliza un eveno
hour = int(input("Hora de inicio (horas): ")) #Solicitar hora inicial
mins = int(input("Minuto de inicio (minutos): ")) #Solicitar minutos iniciales
dura = int(input("Duración del evento (minutos): ")) #Solicitar duracion del evento en minuos

mins = mins+dura #Obtener el numero total de minutos contando el evento
hour = hour + (mins//60) #Sumar los minutos a la hora convirtiendo el toal de minutos a horas usando division entera para evittar los decimales
mins = mins % 60 #Limitar los minuos a el rango de 0 a 59
hour = hour % 24 #Limitar las horas de 0 a 23

print("Hora en que finaliza el evento: " ,hour, ":" ,mins, sep="") #Mostrar resulado