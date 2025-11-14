notas = [8.5, 4.0, 10.0, 7.5, 6.0, 9.0]
soma_notas = 0
contagem_notas_acima_de_7 = 0

for nota in notas:
  soma_notas += nota
  if nota >= 7.0:
    contagem_notas_acima_de_7 += 1

media = soma_notas / len(notas)

print(f"A média das notas é: {media}")
print(f"A quantidade de notas maiores ou iguais a 7.0 é: {contagem_notas_acima_de_7}")
