import math
# try:
#     a = int(input())
#     if a < 0:
#         raise ValueError("Error: el nombre és més petit que 0")
#     elif a > 15:
#         raise ValueError("Erro: el nombre és més gran que 15")
# except ValueError as a:
#     print(a)
# def biseccio(l, val):
#     nums = list(range(1,round(math.log2(len(l)))))
#     # print(round(math.log2(len(l))))
#     # print(len(nums))
#     bg = False
#     lw = False
#     for i in nums:
#         if val > len(l)/i:
#             bg = True
#             print("El nombre és més gran que", len(l)/i)
#         else:
#             lw = True
#             print("El nombre és més petit que", len(l)/i)
# l = []
# for i in range(1000):
#     l.append(i)
# print(len(l))
# biseccio(l, 400)

# def hola(n, n2):
#     llista = []
#     nom = []
#     for i in range(0,11):
#         llista.append(n)
#         nom.append()
#     return min(llista)

# l = [1,2,3]
# print(l)
# l = []
# print(l)

def majusculues(l):
    out = [x.upper() for x in l]
    return out

l = ["hola", "liuh", "tal"]
print(majusculues(l))