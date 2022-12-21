# === PART 3 ===


# == Exercici 1 ==
def ordenar_per_nom(l_hotels):
    return list(sorted(l_hotels, key=lambda x: x.nom))

# == Exercici 2 ==
def carrers_amb_hotels(l_hotels):
    return list(sorted(set(object.carrer for object in l_hotels)))

# == Exercici 3 ==
def estrelles_per_barri(l_hotels, dict_barris):
    dictionary = {}
    for key, object in dict_barris.items():
        estrelles = [0]*5
        for hotel in l_hotels:
            if hotel.codi_barri == int(key):
                estrelles[hotel.estrelles-1]+=1
        dictionary[object.nom]=estrelles
    return dictionary

# == Exercici 4 ==
def densitat_per_districte(l_hotels, dict_barris, dict_districtes):
    dictionary = {}
    for codi_d, object_d in dict_districtes.items():
        num_hotels = 0
        for codi_b, object_b in dict_barris.items():
            if int(codi_d) == int(object_b.codi_districte):
                for hotel in l_hotels:
                    if hotel.codi_barri == int(codi_b):
                        num_hotels+=1
        dictionary[codi_d]=num_hotels/object_d.extensio

    return dictionary


# == Exercici 5 ==
def afegir_prefixe_int(object_hotel):
    if object_hotel.telefon[0] != "+":
        object_hotel.telefon = "+34" + object_hotel.telefon

# == Exercici 6 ==
def modificar_telefon(l_hotels):
    # La funció map no retorna els números amb +34 davant, per tant, fem servir el loop for tradicinal.
    # return map(afegir_prefixe_int, l_hotels)
    for hotels in l_hotels:
        afegir_prefixe_int(hotels)



