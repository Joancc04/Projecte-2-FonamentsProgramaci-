from math import *
'''
TO DO LIST:
- Ex1 fet
- Ex2 fet
- Ex3 fet 
- Ex4 fet
- Ex5 a mitjes
- Ex6 fet
- Ex7
- Ex8 
- Ex9 fet
- Ex10 fet
- Ex11
- Ex11 (main)
hola
que tal
lskdnfkskmd
branca Joan
prova branca Bernat
'''


#== EXERCICI 1 ==
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


#== EXERCICI 2 ==
def codi_in_llista_hotels(llista_hotels, codi_hotel):
    for i in llista_hotels:
        if codi_hotel == i.codi_hotel:
            return True
    else:
        return False


#== EXERCICI 3 ==
#IFS = Input Field Separator
def importar_hotels(fitxer,IFS):
    llista_hotels=[]
    try:
        with open(fitxer, 'r') as file:
            count = 0
            for linia in file:
                if count != 0:
                    linia = file.readline()
                    aux, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles = linia.split(IFS)
                    llista= aux.split(" - ")
                    nom = llista[0]
                    codi_hotel = llista[-1]
                    if not codi_in_llista_hotels(llista_hotels, codi_hotel):
                        llista_hotels.append(Hotel(nom, codi_hotel, carrer, int(numero), int(codi_barri), codi_postal, telefon, float(latitud)/1000000, float(longitud)/1000000, int(estrelles)))
                count+=1
        return llista_hotels
    except FileNotFoundError:
        print("fitxer no trobat")


#== EXERCICI 4 ==
class Barri():
    def __init__(self, nom, codi_districte):
        self.nom = nom
        self.codi_districte = codi_districte
        if not isinstance(self.codi_districte, int) and self.codi_districte < 0:
            raise TypeError ("codi_districte ha de ser un valor enter positiu")

    def __str__(self):
        return f"{self.nom} (districte: {self.codi_districte})"

#== EXERCICI 5 ==
def importar_barris(fitxer, IFS):
    dictionary = {}
    try:
        with open(fitxer, "r") as file:
            count = 0
            if count != 0:
                for line in file:
                    line = file.readline()
                    dictionary['']
            count+=1
    except FileNotFoundError:
        print("Fitxer no trobat")



#== EXERCICI 6 ==
class Districte():
    def __init__(self, nom, extensio, poblacio, llista_barris):
        self.nom = nom
        self.extensio = extensio
        self.poblacio = poblacio
        self.llista_barris = llista_barris
        if not isinstance(poblacio, int) and poblacio < 0:
            raise TypeError ("poblacio ha de ser un valor enter positiu")
        if not isinstance(extensio, float) and extensio < 0:
            raise TypeError ("extensio ha de ser un valor real positiu")
        
    def __str__(self):
        barris = ""
        if self.llista_barris:
            for x in self.llista_barris:
                barris += x + ", "
        else:
            barris = "N/D"
        print (barris)
        return f"{self.nom} ({self.extensio} kms2, {self.poblacio} habitants) barris: {barris}"
        

#== EXERCICI 9 ==
def mostrar_hotels(llista_hotels):
    existence = False
    for i in llista_hotels:
        if isinstance(i, Hotel):
            print(i)
            existence = True
    if not existence:
        print("No hi ha hotels")


#== EXERCICI 10 ==
def mostrar_menu():
    print('''

--- MENÚ PRINCIPAL ---
1 - Veure hotels
S - Sortir del programa    
    ''')


def main():
    llista = importar_hotels("hotels.csv", ";")
    for i in llista:
        print(i.nom, i.codi_hotel,i.estrelles)
    
    # llista=["hola","que","tal","com","va"]
    # print(Districte("Collsuspina", 500, 300, llista))

main()
# print(vars(Hotel))

#      nom  , codi_hotel, carrer, numero, codi_barri,codi_postal,telf,latitud,longitud,estrelles
# h1 = Hotel("Joan",      1,        "2",    12,        12,     12,     12,   12.5,      12.5,       4)
# h2 = Hotel("Hotel H10 Itaca", "HB-004151", "Roma",    22, 9,     8015,     932265594,   41.381193,      2.145467,       4)
# h3 = "holaquetal"
# asdf = [h1,h2,h3]
# mostrar_hotels(asdf)

