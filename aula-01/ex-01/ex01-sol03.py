"""
Dada uma lista de n números, determinar o MAIOR elemento da lista. Exemplo:
Entrada: [21, 15, 30, 18, -10, 0.333333]
Saída Esperada: 30
"""

entrada = [21, 15, 30, 18, -10, 0.333333]
ordenado = sorted(entrada, reverse=True)

print(ordenado[0])