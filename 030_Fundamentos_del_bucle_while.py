blocks = int(input("Ingresa el número de bloques: "))

height = 0  # Altura de la pirámide
used_blocks = 0  # Bloques utilizados hasta el momento

while used_blocks + (height + 1) <= blocks:  
    height += 1  # Aumentamos la altura
    used_blocks += height  # Sumamos los bloques usados en esta capa

print("La altura de la pirámide:", height) #Muestra la altura de la piramide