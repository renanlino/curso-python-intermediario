"""
Qual a média salarial ofertada nos convites do arquivo?
"""

import csv

meu_arquivo = open("invites.csv", "r", encoding="utf-8")
leitor_csv  = csv.reader(meu_arquivo)

i = -1
media_total = 0
for linha in leitor_csv:
    if i > -1:
        min_oferta = float(linha[12])
        max_oferta = float(linha[13])
        media = (min_oferta + max_oferta) / 2
        media_total += (media)
    i += 1
print(media_total/i)
