"""
Dada uma lista de n strings, order a lista de forma CRESCENTE pelo comprimento das strings
Entrada: ["pato", "", "pipoca", "maravilhoso", "pizza"]
Saída Esperada: ["", "pato", "pizza", "pipoca", "maravilhoso"]
"""

def pega_menor(lista):
    menor_ate_agora = lista[0]
    for palavra in lista:
        if len(palavra) < len(menor_ate_agora):
            menor_ate_agora = palavra
    return menor_ate_agora

entrada = ["pato", "", "pipoca", "maravilhoso", "pizza"]
ordenada = []

while len(entrada) > 0:
    menor = pega_menor(entrada)
    ordenada.append(menor)
    entrada.remove(menor)

print(ordenada)