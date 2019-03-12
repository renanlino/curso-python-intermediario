"""
Dada uma lista de n números, determinar o MAIOR elemento da lista. Exemplo:
Entrada: [21, 15, 30, 18, -10, 0.333333]
Saída Esperada: 30
"""

entrada = [21, 15, 30, 18, -10, 0.333333]

maior_ate_agora = entrada[0]

for num in entrada:
    if num > maior_ate_agora:
        maior_ate_agora = num

print(maior_ate_agora)