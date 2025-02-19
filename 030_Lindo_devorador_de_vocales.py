# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Inicializar una variable para almacenar la palabra sin vocales
word_without_vowels = ""

# Bucle for para recorrer cada letra de la palabra
for letter in user_word:
    if letter in "AEIOU":  # Si la letra es una vocal, se omite con continue
        continue
    word_without_vowels += letter  # Agregar la consonante a la nueva palabra

# Imprimir la palabra sin vocales
print("Palabra sin vocales:", word_without_vowels)