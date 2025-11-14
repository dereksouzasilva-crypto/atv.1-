lista_A = [1, 2, 3, 4, 5]
lista_B = [4, 5, 6, 7, 8]

comuns = []


for elemento in lista_A:
    if elemento in lista_B and elemento not in comuns:
        comuns.append(elemento)

print(f"Lista A: {lista_A}")
print(f"Lista B: {lista_B}")
print(f"Lista de elementos comuns (comuns): {comuns}")
