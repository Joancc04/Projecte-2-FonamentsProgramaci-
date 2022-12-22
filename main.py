from part1 import *
from part2 import * 
from part3 import *

def main():
    fitxer_barris = "barris.csv"
    fitxer_districtes = "districtes.csv"
    fitxer_hotels = "hotels.csv"
    delay_time = 0.2
    IFS = ";"
    DELAY = True
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
        # === MAIN ===
        op = "a"
        DELAY = 0.3
        while op not in "Ss":
            mostrar_menu()
            op = input("Introdueix una de les opcions del menú: ")
            if op == "1":
                mostrar_hotels(hotels)
                continuar()
            elif op == "2":
                # delay(DELAY, delay_time)
                mostrar_hotels(ordenar_per_estrelles(hotels))
                continuar()
            elif op == "3":
                buscar_hotels(hotels)
                continuar()
            elif op == "4":
                try:
                    latitud = float(input("Intorudeix el valor de la latitud: "))
                    longitud = float(input("Introdueix el valor de la longitud: "))
                    # print(latitud, longitud)
                    closest_hotel,distancia = hotel_mes_proper(hotels, latitud, longitud)
                    # print(closest_hotel, distancia)
                except ValueError:
                    print("Error: latitud i longitud han de ser valors reals")
                else:
                    print(f"L'hotel  més  proper  és  el  {closest_hotel}  a  {distancia} kms")
                    continuar()
            elif op == "5":
                # delay(DELAY, delay_time)
                mostrar_hotels(ordenar_per_nom(hotels))
                continuar()
            elif op == "6":
                # delay(DELAY, delay_time)
                print(f"Hi ha {len(carrers_amb_hotels(hotels))} carrers amb algún hotel: {carrers_amb_hotels(hotels)}")
                continuar()
            elif op == "7":
                # delay(DELAY, delay_time)
                diccionari_b = estrelles_per_barri(hotels, barris)
                for nom_b, l_estrelles in diccionari_b.items():
                    print(f"El barri: {nom_b} té:\n- {l_estrelles[0]} hotels d'1 estrella\n- {l_estrelles[1]} hotels d'2 estrelles\n- {l_estrelles[2]} hotels d'3 estrelles\n- {l_estrelles[3]} hotels d'4 estrelles\n- {l_estrelles[4]} hotels DELAY estrelles\nzz")
                continuar()
            elif op == "8":
                # delay(DELAY, delay_time)
                densitat = densitat_per_districte(hotels, barris, districtes)
                for codi_d, densitat in densitat.items():
                    print(f"Districte {codi_d}: {densitat} hotels/km2")
                continuar()
            elif op == "9":
                modificar_telefon(hotels)
                print("S'han modificat els telèfons correctament")
                continuar()
            elif op in "Ss":
                print("Sortint del programa")
            else:
                print("Opció no permesa")
                # delay(DELAY, delay_time)
    finally:
        print("© Bernat Vidal i Joan Colillas")
    return 0

if __name__ == '__main__':
    main()


