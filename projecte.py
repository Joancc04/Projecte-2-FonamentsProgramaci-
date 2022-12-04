class Hotel():
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitutd, longitud, estrelles):
        self.nom = nom
        self.codi_hotel = codi_hotel
        self.carrer = carrer
        self.numero = numero
        self.codi_barri = codi_barri
        self.codi_postal = codi_postal 
        self.telefon = telefon
        self.latitud = latitutd
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
        
        


#      nom  , codi_hotel, carrer, numero, codi_barri,codi_postal,telf,latitud,longitud,estrelles
Hotel("Joan",      1,        "2",    12,        12,     12,     12,   12.5,      12.5,       12)