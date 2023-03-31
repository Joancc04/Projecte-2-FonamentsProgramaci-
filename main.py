from part1 import *
from part2 import * 
from part3 import *

def main():
    fitxer_barris = "barris.csv"
    fitxer_districtes = "districtes.csv"
    fitxer_hotels = "hotels.csv"
    IFS = ";"
    try:
        hotels = importar_hotels(fitxer_hotels, IFS, True)
        barris = importar_barris(fitxer_barris, IFS, True)
        districtes = importar_districtes(fitxer_districtes, IFS, True)
        omplir_llista_barris(barris,districtes)
    except FileNotFoundError as e:
        print("Error llegint fitxers:", e)
    except Exception as a:
        print("Error processant els fitxers:", a)
    else:
        op = "a"
        while op not in "Ss": 
            hotels = importar_hotels(fitxer_hotels, IFS, False)
            barris = importar_barris(fitxer_barris, IFS, False)
            districtes = importar_districtes(fitxer_districtes, IFS, False)
            mostrar_menu()
            op = input("Introdueix una de les opcions del menú: ")
            if op == "1":
                mostrar_hotels(hotels)
                continuar()
            elif op == "2":
                mostrar_hotels(ordenar_per_estrelles(hotels))
                continuar()
            elif op == "3":
                buscar_hotels(hotels)
                continuar()
            elif op == "4":
                try:
                    latitud = float(input("Intorudeix el valor de la latitud: "))
                    longitud = float(input("Introdueix el valor de la longitud: "))
                    closest_hotel,distancia = hotel_mes_proper(hotels, latitud, longitud)
                except ValueError:
                    print("Error: latitud i longitud han de ser valors reals")
                else:
                    print(f"L'hotel  més  proper  és  el  {closest_hotel}  a  {distancia} kms")
                    continuar()
            elif op == "5":
                mostrar_hotels(ordenar_per_nom(hotels))
                continuar()
            elif op == "6":
                print(f"Hi ha {len(carrers_amb_hotels(hotels))} carrers amb algún hotel.")
                continuar()
                for hotel in carrers_amb_hotels(hotels):
                    print(f"- {hotel}")
                continuar()
            elif op == "7":
                diccionari_b = estrelles_per_barri(hotels, barris)
                for nom_b, l_estrelles in diccionari_b.items():
                    print(f"El barri: {nom_b} té:\n- {l_estrelles[0]} hotels d'1 estrella\n- {l_estrelles[1]} hotels de 2 estrelles\n- {l_estrelles[2]} hotels de 3 estrelles\n- {l_estrelles[3]} hotels de 4 estrelles\n- {l_estrelles[4]} hotels de 5 estrelles\n")
                continuar()
            elif op == "8":
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
    finally:
        print("© Bernat Vidal i Joan Colillas")
    return 0

if __name__ == '__main__':
    main()
    print("a")
    print("b")