class Barri():
    def __init__(self, nom, codi_districte):
        try:
            self.nom = nom
            self.codi_districte = codi_districte
            if not isinstance(self.codi_districte, int) or self.codi_districte < 0:
                raise TypeError ("codi_districte ha de ser un valor enter positiu")
        except TypeError as e:
            print(e)

    def __str__(self):
        return f"{self.nom} (districte: {self.codi_districte})" 

dictionary = {}
fitxer = "barris.csv"
IFS = ";"
try:
    with open(fitxer, "r") as file:
        count=0
        for line in file:
            if count != 0:
                # print(line)
                # print(linia)
                linia = line[:-1].split(IFS)
                dictionary[linia[0]]=Barri(linia[2], int(linia[1]))
            else:
                count+=1
except FileNotFoundError:
    print("Fitxer no trobat")

# print("diccionari:",dictionary)

# print(Barri("La marina del port", 1))

def print_dict(dictionary):
    for i,j in dictionary.items():
        print(f"{i}: {j}")


