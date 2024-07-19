def salva(nomeArquivo, valor): #modo w
    arq = open(nomeArquivo, 'w')
    arq.write(valor)
    arq.close()

def carrega(nomeArquivo): #modo r
    try:
        arq = open(nomeArquivo, 'r')
        valor = arq.read()
        arq.close()
        return valor
    except FileNotFoundError:
        print("Arquivo", nomeArquivo, "inexistente.")
        return 0

def carregaLinhaALinha(nomeArquivo):
    lista = []
    try:
        arq = open(nomeArquivo, 'r')
        while True:
            linha = arq.readline()
            if linha == "":
                break
            lista.append(linha)
        arq.close()
        return lista
    except FileNotFoundError:
        print("Arquivo", nomeArquivo, "inexistente.")
