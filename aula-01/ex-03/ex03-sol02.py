"""
Dada uma lista de n strings, order a lista de forma CRESCENTE pelo comprimento das strings
Entrada: ["pato", "", "pipoca", "maravilhoso", "pizza"]
Saída Esperada: ["", "pato", "pizza", "pipoca", "maravilhoso"]
"""

entrada = ["pato", "", "pipoca", "maravilhoso", "pizza"]
ordenada = []

while len(entrada) > 0:
    menor = min(entrada, key=lambda x: len(x))
    ordenada.append(menor)
    entrada.remove(menor)

print(ordenada)