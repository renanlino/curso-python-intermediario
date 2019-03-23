import csv
import string #opicional!

def busca_palavra(frequencias, palavra):
    """
    Procura 'palavra' dentro de 'frequencias' (vide abaixo).
    Se encontra, retorna a linha onde ela está armazenada.
    Se não a encontra, retorna None
    formato esperado de 'frequencias':
        freqs = [
            ["palavra1", 30],
            ["palavra3", 25],
            ["palavra4", 20],
            ["palavra5", 15]
        ]
    """
    # gera i de 0 até len(frequencias)
    for i in range(len(frequencias)):
        # procura pelo match e retorna se encontrar
        if frequencias[i][0] == palavra:
            return i
    return None

meu_arquivo = open("invites.csv", "r", encoding="utf-8")
leitor_csv  = csv.reader(meu_arquivo)

i = 0
freqs = []
for linha in leitor_csv:
    if i > 0:
        desc = linha[5]
        # parte opcional: retira pontuação do texto
        for ponto in string.punctuation:
            desc = desc.replace(ponto, "")
        # fim da parte opcional: retira pontuação do texto
        # retira a quebra de linha do texto e troca por espaço:
        desc = desc.replace("\n", " ")
        # transforma tudo em minúsculas:
        desc = desc.lower()
        # separa as palavras na ocorrência de espaço:
        palavras = desc.split(" ")
        
        for palavra in palavras:
            # procura pela palavra atual no banco de frequências:
            posicao = busca_palavra(freqs, palavra)
            # se a palavra já existe no banco:
            if posicao is not None:
                freqs[posicao][1] += 1
            # se não existe...
            else:
                nova_entrada = [palavra, 1]
                freqs.append(nova_entrada)
    i += 1

# opcional: ordernar do maior para o menor:
freqs.sort(key = lambda x: x[1], reverse=True)

#abre e cria o arquivo de saída
#quer visualizar? sugiro subir no google drive e abrir usando o google sheets
arquivo_de_saida = open("output_oculto.csv", "w", encoding="utf-8")
gravador = csv.writer(arquivo_de_saida)

#grava o cabeçalho
gravador.writerow(["palavra","frequência"])

#grava o conteúdo
for entrada in freqs:
    gravador.writerow(entrada)

#não se esqueça de fechar o arquivo
arquivo_de_saida.close()
