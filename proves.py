# # # a = 6
# # # b = "hola"
# # # c = "ñalskjd"

# # # class Hotel():
# # #     def __init__(self, codi_hotel):
# # #         self.codi_hotel = codi_hotel

# # # p1 = Hotel(1234)
# # # p2 = Hotel(2345)
# # # p3 = Hotel(3456)
# # # llista=[Hotel(1234),Hotel(2345),Hotel(3456)]
# # # #llista=[[1234,1235,1236],[2345,456456,2323],[234234,3234,2342]]

# # # def codi_in_llista_hotels(llista_hotels, codi_hotel):
# # #     for i in llista_hotels:
# # #         if codi_hotel == i.codi_hotel:
# # #             return True
# # #     else:
# # #         return False
# # # string = "Amrey Sant Pau - HB-004046"
# # # list1=[0]*2
# # # list1[0], list1[1] = string.split(" - ")
# # # print(list1)

# # #==============================================================
# # # print(codi_in_llista_hotels(llista, 1234))
# # # paraules = "hola que tal"
# # # llista=paraules[:-2].split(" ")
# # # print(llista)
# # # def hola():
# # #     return f"hola que tal"
# # # print(hola())
# # #==============================================================

# # def Lyrics2list(string):
# #     sor = []
# #     for i in string:
# #         if i>='A' and i <= 'Z':
# #             sor.append(chr(ord(i)+32))
# #         else:
# #             if  (i>= 'a' and i>= 'z' or i == ' '):
# #                 sor.append(i)
# #     new= "".join(sor)
# #     return new

# # def Lyrics2list(lletra):
# #     aux=[]
# #     for c in lletra:
# #         if (c >= 'A' and c<='Z'):
# #             aux.append(chr(ord(c)+32))
# #         else:
# #             if (c>= 'a' and c<='z' or c == ' '):
# #                 aux.append(c)
# #     new_lletra = "".join(aux)
# #     return (new_lletra)

# def print_names(llista, estat):
#     print(f"\t== [{estat}] ==")
#     for i in llista:
#         print(f"\t     {i}")
#     print(f"\t  [Total: {len(llista)}]\n")
    
# def add_name(venen, no_venen, tard):
#     print("=== SOPING ===")
#     print("   ")
#     op = ""
#     while op!=4:
#         op = int(input("Escriu opció: [1: El pibe vindrà] [2: El pibe vindrà tard] [3: El pibe no ve] [4: Sortir] --> "))
#         if op!=4:
#             nom = input("Escriu el seu nom:")
#         print(" ")
#         if op == 1:
#             if nom not in venen:
#                 venen.append(nom)
#         elif op == 2:
#             if nom not in no_venen:
#                 no_venen.append(nom)
#         elif op == 3:
#             if nom not in tard:
#                 tard.append(nom)
#         elif op == 4:
#             break
#         else:
#             print("Opció inexistent")
#     venen.sort()
#     no_venen.sort()
#     tard.sort()
#     return venen, no_venen, tard
# venen = []
# no_venen = []
# tard = []
# add_name(venen, no_venen, tard)
# print_names(venen, "venen")
# print_names(no_venen, "no venen")
# print_names(tard, "venen tard")
paraula = ""
llista=[]
while paraula != " ":
    paraula = input()
    llista.append(paraula)
llista.sort()
print(llista)
