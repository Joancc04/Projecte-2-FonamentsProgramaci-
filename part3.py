# === PART 3 ===

def ordenar_per_nom(l_hotels):
    return list(sorted(l_hotels, key=lambda x: x.nom))

def carrers_amb_hotels(l_hotels):
    return list(sorted(set(object.carrer for object in l_hotels)))

def estrelles_per_barri(l_hotels, dict_barris):
    dictionary = {}
    for key, object in dict_barris.items():
        estrelles = [0]*5
        for hotel in l_hotels:
            if hotel.codi_barri == int(key):
                estrelles[hotel.estrelles-1]+=1
        dictionary[object.nom]=estrelles
    return dictionary

def densitat_per_districte(l_hotels, dict_barris, dict_districtes):
    pass