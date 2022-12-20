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
### EXERCICI 1 ###
def ordenar_per_estrelles(llista_hotels):
    ll_hotels=llista_hotels.copy()
    ll_hotels.sort(key=lambda x: x[9])
    return ll_hotels

### EXERCICI 2 ###
def mostrar_noms_hotels(llista_hotels):
    for i in llista_hotels:
        print(i.nom,"(",i.codi_hotel,")")
        
### EXERCICI 3 ###
def buscar_per_nom(llista_hotels,nom_hotel):
    # ll_buscar_hotels=[]
    # [ll_buscar_hotels.append(Hotel()) for x in llista_hotels if nom_hotel.upper() in Hotel(nom).upper()]
    # return ll_buscar_hotels
    pass

## EXERCICI 4 ###
def buscar_per_estrelles(llista_hotels,n_estrelles):
    #ll_buscar_estrelles=[]
    #[ll_buscar_estrelles.append(Hotel()) for x in llista_hotels if n_estrelles==Hotel(estrelles)]
    #return ll_buscar_estrelles

    ll_buscar_estrelles=list(filter(lambda x: x[9]==n_estrelles,llista_hotels))
    return ll_buscar_estrelles

# == Exercici 5 ==
def buscar_hotels(llista_hotels):
    op = int(input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): "))
    if op == 1:
        nom_hotel = input("Introdueix el nom de l'hotel: ")
        l_hotels = buscar_per_nom(nom_hotel)
        if l_hotels:
            print(f"S'han trobat {len(l_hotels)} hotels amb aquest nom")
            time.sleep(1)
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

# == Exercici 6 == *****
def hotel_mes_proper(l_hotels, latitud, longitud):
    if type(Hotel) in l_hotels:
        closest_hotel = ""
        for hotels in l_hotels:
            if hotels.distancia() < Hotel.distancia(latitud, longitud):
                closest_hotel = hotels
        return closest_hotel.latitud, closest_hotel.longitud
    else:
        return None, None


def main():
    fitxer_barris = "barris.csv"
    fitxer_districtes = "districtes.csv"
    fitxer_hotels = "hotels.csv"
    IFS = ";"
    try:
        barris = importar_barris(fitxer_barris, IFS)
        districtes = importar_districtes(fitxer_districtes, IFS)
        hotels = importar_hotels(fitxer_hotels, IFS)
    except FileNotFoundError as e:
        print("Error llegint fitxers:", e)
    except Exception as e:
        print("Error processant els fitxers:", e)
    else:
        omplir_llista_barris(barris, districtes)
        op = "a"
        
        while op not in "Ss":
            mostrar_menu()
            op = input("Introdueix una de les opcions del menú: ")
            if op == "1":
                mostrar_hotels(hotels)
            elif op in "Ss":
                print("Sortint del programa")
            else:
                print("Opció no permesa")
                time.sleep(0.5)
    finally:
        print("© Bernat Vidal i Joan Colillas")
    
    return 0

main()