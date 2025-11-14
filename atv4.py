estoque = [
    {"nome": "Teclado", "preco": 150.00, "quantidade": 5},
    {"nome": "Mouse", "preco": 80.00, "quantidade": 12},
    {"nome": "Monitor", "preco": 700.00, "quantidade": 3},
    {"nome": "Headset", "preco": 250.00, "quantidade": 8}
]

print("Produtos com estoque menor que 10 unidades:")
print("-----------------------------------------")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])
