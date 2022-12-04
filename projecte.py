from math import *

class Hotel():
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        self.nom = nom
        self.codi_hotel = codi_hotel
        self.carrer = carrer
        self.numero = numero
        self.codi_barri = codi_barri
        self.codi_postal = codi_postal 
        self.telefon = telefon
        self.latitud = latitud
        self.longitud = longitud
        self.estrelles = estrelles

        # == Comprovant variables tipus int == 
        vars_int = [[self.numero, "numero"], [self.codi_barri, "codi_barri"], [self.estrelles, "estrelles"]]
        for i in vars_int:
            if not isinstance(i[0], int):
                raise TypeError (f"{i[1]} ha de ser un valor enter positiu")
        
        # == Comprovant variables tipus float == 
        vars_float = [[self.latitud, "latitud"], [self.longitud, "longitud"]]
        for i in vars_float:
            if not isinstance(i[0], float):
                raise TypeError (f"{i[1]} ha de ser un valor real")

        # == Comprovant estrelles entre 1 i 5 == 
        if self.estrelles not in range(1,6):
            raise ValueError ("estrelles ha de ser un valor entre 1 i 5")
    
    def __str__(self):
        return f"{self.nom} ({self.codi_hotel}) {self.carrer},{self.numero} {self.codi_postal} (barri: {self.codi_barri}) {self.telefon} ({self.latitud},{self.longitud}) {self.estrelles} estrelles"
        
    def __gt__(self, altre_hotel):
        return self.estrelles > altre_hotel.estrelles

    def distancia(self, latitud, longitud):
        vars_float=[[latitud,"latitud"],[longitud,"longitud"]]
        RADI_TERRA = 6378.137
        latitud *= pi/180
        longitud *= pi/180
        for i in vars_float:
            if not isinstance(i[0], float):
                raise TypeError (f"{i[1]} ha de ser un valor real")
        return acos(sin(self.latitud) * sin(latitud) + cos(self.latitud) * cos(latitud) * cos(longitud - self.longitud)) * RADI_TERRA

def codi_in_llista_hotels(llista_hotels, codi_hotel):
    for i in llista_hotels:
        if codi_hotel == i.codi_hotel:
            return True
    else:
        return False

#IFS = Input Field Separator
def importar_hotels(fitxer,IFS):
    llista_hotels=[]
    try:
        with open(f'{fitxer}', 'r', encoding='utf-8') as file:
            for linia in file[1:]:
                aux, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles = linia[:-2].split(IFS)
                nom, codi_hotel = aux.split(' - ')
                if not codi_in_llista_hotels(llista_hotels, codi_hotel):
                    llista_hotels.append(Hotel(nom, codi_hotel, carrer, int(numero), int(codi_barri), codi_postal, telefon, float(latitud)/1000000, float(longitud)/1000000, int(estrelles)))
    except FileNotFoundError as a:
        print("fitxer no trobat")

class Barri():
    def __init__(self, nom, codi_districte):
        self.nom = nom
        self.codi_districte = codi_districte
        if not isinstance(self.codi_districte, int) and self.codi_districte < 0:
            raise TypeError ("codi_districte ha de ser un valor enter positiu")
    
    def __str__(self):
        return f"{self.nom} (districte: {self.codi_districte})"
        



        


#      nom  , codi_hotel, carrer, numero, codi_barri,codi_postal,telf,latitud,longitud,estrelles
# h1 = Hotel("Joan",      1,        "2",    12,        12,     12,     12,   12.5,      12.5,       4)
# h2 = Hotel("Hotel H10 Itaca", "HB-004151", "Roma",    22, 9,     8015,     932265594,   41.381193,      2.145467,       4)
# print(h2)