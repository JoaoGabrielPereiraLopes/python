def gera_lista():
    lista=[]#cria uma lista azia ara receber is numeros digitados
    while True:
        try:
            lista+=[float(input('me informe mais um numero ou digite qualquer outra coisa pra sair: '))]#inclementa numeros floats digitados na lista
        except:
            return (lista)