from datetime import date

nom = input("Quel est votre nom : ")
annee_naissance = int(input("Quelle est votre année de naissance ? "))

#calcul age actuel
age = date.today().year - annee_naissance
print(f"Bonjour {nom}, vous avez {age} ans.")
