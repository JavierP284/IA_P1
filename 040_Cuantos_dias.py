def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #Funcion para determinar si es bisiesto
        return True
    return False

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:  # Verifica si los valores son válidos
        return None

    # Días por mes (sin contar febrero)
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Si es febrero, revisamos si el año es bisiesto
    if month == 2 and is_year_leap(year):
        return 29
    return dias_por_mes[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [29, 29, 28, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")