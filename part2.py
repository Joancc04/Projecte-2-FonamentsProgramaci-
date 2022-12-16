from part1 import * 

'''
TO DO LIST:
- Ex1
- Ex2 
- Ex3
- Ex4
- Ex5 fet
- Ex6
- Ex7
- Ex8 (main)
'''
# == Exercici 1 == 
def ordenar_per_estrelles(l_hotels):
    pass


# == Exercici 2 ==
def mostrar_noms_hotels(l_hotels):
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
        while True:
            try:
                num_estrelles = int(input("Escriu el nombre d'estrelles: "))
                if num_estrelles > 5 or num_estrelles < 1:
                        raise Exception("Error: el nombre d'estrelles ha de ser entre 1 i 5")
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor enter")
            except Exception as missatge:
                print(missatge)
            else:
                l_hotels = buscar_per_estrelles(llista_hotels)
                if l_hotels:
                    print(f"S'han trobat {len(l_hotels)} hotels de {num_estrelles} estrelles")
                else:
                    print("No s'han trobat hotels")
                break
    else:
        print("Error: criteri de cerca no vàlid")

# == Exercici 6 == 
def hotel_mes_proper(l_hotels, latitud, longitud):
    pass


def mein():
    l = ["hola", "que", "tal"]
    buscar_hotels(l)
    return 0


mein()