# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Bucle for para recorrer cada letra de la palabra
for letter in user_word:
    if letter in "AEIOU":  # Si la letra es una vocal, se omite con continue
        continue
    print(letter)  # Imprime solo las letras que no son vocales