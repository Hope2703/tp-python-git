nombre_input = input("Entrez un nombre entier : ")
nombre = int(nombre_input)

if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair.")
else:
    print(f"Le nombre {nombre} est impair.")