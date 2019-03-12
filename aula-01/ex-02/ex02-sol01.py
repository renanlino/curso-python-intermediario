"""
Dada uma lista com n strings, determinar a string de MAIOR comprimento
Entrada: ["pato", "", "pipoca", "maravilhoso", "pizza"]
Saída Esperada: 'maravilhoso'
"""

entrada = ["pato", "", "pipoca", "maravilhoso", "pizza"]

maior_ate_agora = entrada[0]

for palavra in entrada:
    if len(palavra) > len(maior_ate_agora):
        maior_ate_agora = palavra

print(maior_ate_agora)