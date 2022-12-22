# === PART 2 ===
from part1 import * 
from part3 import * 


# == Exercici 1 ==
def ordenar_per_estrelles(l_hotels):
    return sorted(l_hotels, key=lambda x: x.estrelles)


# == Exercici 2 ==
def mostrar_noms_hotels(llista_hotels):
    for i in llista_hotels:
        print(i.nom,"(",i.codi_hotel,")")
        

# == Exercici 3 ==
def buscar_per_nom(l_hotels,nom_hotel):
    return list(filter(lambda x:nom_hotel.upper() in x.nom.upper(), l_hotels))


# == Exercici 4 ==
def buscar_per_estrelles(l_hotels,n_estrelles):
    return list(filter(lambda x:x.estrelles==n_estrelles, l_hotels))


# == Exercici 5 ==
def buscar_hotels(llista_hotels):
    op = input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ")
    if op == "1":
        nom_hotel = input("Introdueix el nom de l'hotel: ")
        l_hotels = buscar_per_nom(llista_hotels, nom_hotel)
        if l_hotels:
            print(f"S'han trobat {len(l_hotels)} hotels amb aquest nom")
            continuar()
            mostrar_noms_hotels(l_hotels)
        else:
            print("No s'han trobat hotels")
    elif op == "2":
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
                l_hotels = buscar_per_estrelles(llista_hotels, num_estrelles)
                if l_hotels:
                    print(f"S'han trobat {len(l_hotels)} hotels de {num_estrelles} estrelles")
                    continuar()
                    mostrar_noms_hotels(l_hotels)
                else:
                    print("No s'han trobat hotels")
                break
    else:
        print("Error: criteri de cerca no vàlid")


# == Exercici 6 == *****
def hotel_mes_proper(l_hotels, latitud, longitud):
    distancies = []
    noms = []
    for hotels in l_hotels:
        if type(hotels) is Hotel:
            distancies.append(hotels.distancia(latitud, longitud))
            noms.append(hotels.nom)
        else:
            return None, None
    return noms[distancies.index(min(distancies))], min(distancies)