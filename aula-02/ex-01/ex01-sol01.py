"""
Qual a média salarial ofertada nos convites do arquivo?
"""

import csv

meu_arquivo = open("invites.csv", "r", encoding="utf-8")
leitor_csv  = csv.reader(meu_arquivo)

i = 0
media_total = []
for linha in leitor_csv:
    if i > 0:
        min_oferta = float(linha[12])
        max_oferta = float(linha[13])
        media = (min_oferta + max_oferta) / 2
        media_total.append(media)
    i += 1
print(sum(media_total)/len(media_total))
