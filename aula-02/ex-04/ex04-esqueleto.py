import csv

#calcule aqui as frequências, como no ex. 3. deve ser algo parecido com isso no final:
freqs = [
    ["palavra1", 30],
    ["palavra3", 25],
    ["palavra4", 20],
    ["palavra5", 15]
    ]

#abre e cria o arquivo de saída
#quer visualizar? sugiro subir no google drive e abrir usando o google sheets
arquivo_de_saida = open("output.csv", "w", encoding="utf-8")
gravador = csv.writer(arquivo_de_saida)

#grava o cabeçalho
gravador.writerow(["palavra","frequência"])

#grava o conteúdo
for entrada in freqs:
    gravador.writerow(entrada)

#não se esqueça de fechar o arquivo
arquivo_de_saida.close()
