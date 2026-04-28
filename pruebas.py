while True:
    numero = int(input("Ingrese número: "))
    
    if numero < 0:
        print("No válido")
        continue

    print("Número válido")
    break

for numero in [1, 2, 3, 4, 5]:
    if numero == 3:
        continue
    print(numero)