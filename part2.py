from projecte import * 

'''
TO DO LIST:
- Ex1
- Ex2 
- Ex3
- Ex4
- Ex5
- Ex6
- Ex7
- Ex8 (main)
'''
# == Exercici 2 ==
def mostrar_noms_hotels(llista_hotels):
    pass


# == Exercici 3 ==
def buscar_per_nom(l_hotels, nom_hotel):
    pass


# == Exercici 4 == 
def buscar_per_estrelles():
    pass

# == Exercici 5 ==
def buscar_hotels(llista_hotels):
    op = int(input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): "))
    if op == 1:
        nom_hotel = input("Introdueix el nom de l'hotel: ")
        l_hotels = buscar_per_nom(nom_hotel)
        if l_hotels:
            print(f"S'han trobat {len(l_hotels)} hotels amb aquest nom")
            mostrar_noms_hotels(l_hotels)
        else:
            print("No s'han trobat hotels")
    elif op == 2:
        try:
            num_estrelles = int(input("Escriu el nombre d'estrelles: "))
            while not isinstance(num_estrelles, int) and 1 > num_estrelles > 5:
                num_estrelles = int(input("Escriu el nombre d'estrelles: "))
        except ValueError:
            print("Error: el número d'estrelles ha de ser un valor enter")
        else:
            l_hotels = buscar_per_estrelles(llista_hotels)
            if l_hotels:
                print(f"S'han trobat {len(l_hotels)} hotels de {num_estrelles} estrelles")
            else:
                print("No s'han trobat hotels")
    else:
        print("Error: criteri de cerca no vàlid")