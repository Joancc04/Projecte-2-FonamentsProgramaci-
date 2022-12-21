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
        omplir_llista_barris(barris,districtes)
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
        # modificar_telefon(hotels)
        # for i in hotels:
        #     print(i.telefon)
        # ordenats = ordenar_per_estrelles(hotels)
        # for i in ordenats:
        #     print(i.estrelles)
        # hotels_estrelles = buscar_per_estrelles(hotels, 2)
        # for i in hotels_estrelles:
        #     print(i.estrelles)

        # nom_hotels = buscar_per_nom(hotels, "Hotel")
        # for i in nom_hotels:
        #     print(i.nom)
        # omplir_llista_barris(barris, districtes)
        # for key, object in districtes.items():
        #     print(object.llista_barris)
        #     print('''
        
        #     ''')
        # latitud = float(input("Latitud: "))
        # longitud = float(input("Longitud: "))
        # latitud = 41414013/1000000
        # longitud = 2177888/1000000
        # nom, dist = hotel_mes_proper(hotels, latitud, longitud)
        # print(nom, "a ", dist)



        # === MAIN ===
        op = "a"

        while op not in "Ss":
            mostrar_menu()
            op = input("Introdueix una de les opcions del menú: ")
            if op == "1":
                mostrar_hotels(hotels)
            elif op == "2":
                mostrar_hotels(ordenar_per_estrelles(hotels))
            elif op == "3":
                buscar_hotels(hotels)
            elif op == "4":
                try:
                    latitud = float(input("Intorudeix el valor de la latitud: "))
                    longitud = float(input("Introdueix el valor de la longitud: "))
                    closest_hotel,distancia = hotel_mes_proper(hotels, latitud, longitud)
                except ValueError:
                    print("Error: latitud i longitud han de ser valors reals")
                else:
                    print(f"L'hotel  més  proper  és  el  {closest_hotel}  a  {distancia} kms")
                    time.sleep(1)
            elif op == "5":
                mostrar_hotels(ordenar_per_nom(hotels))
            elif op == "6":
                print(f"Hi ha {len(carrers_amb_hotels(hotels))} carrers amb algún hotel: {carrers_amb_hotels(hotels)}")
            elif op == "7":
                diccionari_b = estrelles_per_barri(hotels, barris)
                for nom_b, l_estrelles in diccionari_b.items():
                    print(f"El barri: {nom_b} té:\n- {l_estrelles[0]} hotels d'1 estrella\n- {l_estrelles[1]} hotels d'2 estrelles\n- {l_estrelles[2]} hotels d'3 estrelles\n- {l_estrelles[3]} hotels d'4 estrelles\n- {l_estrelles[4]} hotels d'5 estrelles\n")
            elif op == "8":
                densitat = densitat_per_districte(hotels, barris, districtes)
                for codi_d, densitat in densitat.items():
                    print(f"Districte {codi_d}: {densitat} hotels/km2")
            elif op == "9":
                modificar_telefon(hotels)
                print("S'han modificat els telèfons correctament")
            elif op in "Ss":
                print("Sortint del programa")
            else:
                print("Opció no permesa")
                time.sleep(0.5)
    finally:
        print("© Bernat Vidal i Joan Colillas")
    
    return 0

if __name__ == '__main__':
    main()


