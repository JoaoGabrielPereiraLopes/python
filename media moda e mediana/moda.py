from geradora import gera_lista
def moda():
    lista=gera_lista()#recebe uma lista de numeros
    moda=0#cria uma variavel que vai receber 1 valor das modas
    modas=[]#recebe todas as modas
    for x in lista:
        if lista.count(x)>lista.count(moda):#se a ocorencia de x for maior que a da moda dos numeros já testadas, a moda se torna x
            moda=x
            modas=[x]#faz a lista modas ter apenas o valor de x
        elif lista.count(x)==lista.count(moda) and x not in modas:#se a ocorencia de x for igual a da moda dos numeros já testadas e não for igual a um numero já testado, adiciona x na lista modas
            modas+=[x]
    if len(modas)>1:
        return modas#se não existe só uma moda, então retorna a lista modas
    else:
        return moda #se não retorna a moda
if __name__=="__main__":
    resultado=moda()
    if type(resultado)==list:
        geral=''
        for x in resultado:
            geral+=str(x)+' '
        print(f'os resultaods são {geral}')
    else:
        print(f'o resultado é {resultado}')