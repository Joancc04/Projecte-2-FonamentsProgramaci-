from part1 import *
from part2 import * 
from part3 import *

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
        # === PROVES ===
        # for object in hotels:
        #     print("Hotel:", object.nom, object.estrelles)
        # for i,j in barris.items():
        #     print(i,j)
        # llista_hola = sorted(hotels, key=lambda x: x.nom)
        # for i in llista_hola:
        #     print(i.nom)        
        # omplir_llista_barris(barris, districtes)
        # op = "a"
        # print(estrelles_per_barri(hotels, barris))
        # hola = estrelles_per_barri(hotels, barris)
        # for i,j in hola.items():
        #     print(i,"-->", j)
        # print('''
        
        # ''')
        # for i in hotels:
        #     if i.codi_barri in range(28,33):
        #         print("Hotel:", i.nom, "amb codi:",i.codi_barri)
    
        # dictionary = densitat_per_districte(hotels, barris, districtes)
        # for i,j in dictionary.items():
        #     print("Codi:", i, ". Num de hotels:",j)

        # print(hotels[1].telefon)
        # afegir_prefixe_int(hotels[1].telefon)
        # print(hotels[1].telefon)

        # print(hotels[5].telefon)
        # afegir_prefixe_int(hotels[5])
        # print(hotels[5].telefon)
        modificar_telefon(hotels)
        for i in hotels:
            print(i.telefon)
        # ordenats = ordenar_per_estrelles(hotels)
        # for i in ordenats:
        #     print(i.estrelles)
        # hotels_estrelles = buscar_per_estrelles(hotels, 2)
        # for i in hotels_estrelles:
        #     print(i.estrelles)

        # nom_hotels = buscar_per_nom(hotels, "Hotel")
        # for i in nom_hotels:
        #     print(i.nom)





        # === MAIN ===
        # while op not in "Ss":
        #     mostrar_menu()
        #     op = input("Introdueix una de les opcions del menú: ")
        #     if op == "1":
        #         mostrar_hotels(hotels)
        #     elif op == "2":
        #         mostrar_hotels(ordenar_per_estrelles(hotels))
        #     elif op == "3":
        #         buscar_hotels(hotels)
        #     elif op == "4":
        #         try:
        #             latitud = float(input("Intorudeix el valor de la latitud: "))
        #             longitud = float(input("Introdueix el valor de la longitud: "))
        #         except ValueError:
        #             print("Error: latitud i longitud han de ser valors reals")
        #         else:
        #             closest_hotel = hotel_mes_proper(hotels, latitud, longitud)
        #             print(f"L'hotel  més  proper  és  el  {closest_hotel}  a  {closest_hotel.distancia()} kms")

        #     elif op in "Ss":
        #         print("Sortint del programa")
        #     else:
        #         print("Opció no permesa")
        #         time.sleep(0.5)
    finally:
        print("© Bernat Vidal i Joan Colillas")
    
    return 0

if __name__ == '__main__':
    main()


