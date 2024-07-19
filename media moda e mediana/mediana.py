from geradora import gera_lista
def mediana():
    lista=gera_lista()#recebe uma lista de numeros float
    lista.sort()#ordena a lista em crescente

    if len(lista)%2==1:
        return lista[int((len(lista)/2)-0.5)]#se for impar retorna o número do meio

    else:
        return  (
                    (
                        (lista[int((len(lista)/2)-0.5)]) + (lista[int((len(lista)/2)+0.5)])
                    )/2#se for par retorna a media dos dois números do meio
                )

if __name__=="__main__":
    print(f"a mediana é {round(mediana(),5)}")