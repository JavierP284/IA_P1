my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("La lista con elementos únicos:")
print(unique_list)