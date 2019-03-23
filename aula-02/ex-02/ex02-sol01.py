"""
Qual a empresa responsável pelo invite com maior média salarial?
"""

import csv

meu_arquivo = open("invites.csv", "r", encoding="utf-8")
leitor_csv  = csv.reader(meu_arquivo)

i = 0
maior_media = 0
empresa_maior_media = None
for linha in leitor_csv:
    if i > 0:
        min_oferta = float(linha[12])
        max_oferta = float(linha[13])
        media = (min_oferta + max_oferta) / 2
        if media > maior_media:
            maior_media = medias
            empresa_maior_media = linha[18]
    i += 1
print("O maior invite (R$%.2f) foi feito pela empresa de id = %s" %(maior_media, empresa_maior_media))
