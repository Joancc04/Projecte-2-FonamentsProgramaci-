try:
    a = int(input())
    if a < 0:
        raise ValueError("Error: el nombre és més petit que 0")
    elif a > 15:
        raise ValueError("Erro: el nombre és més gran que 15")
except ValueError as a:
    print(a)