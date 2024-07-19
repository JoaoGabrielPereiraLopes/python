from geradora import gera_lista
def media():
    espaço_amostral=gera_lista()#numeros usados
    somatoria=0#um numero que receberá a soma de todos os numeros do espaço amostral
    for x in espaço_amostral:
        somatoria+=x#soma todos os numeros a somatória
    return somatoria/len(espaço_amostral)#tira a média da lista
if __name__=="__main__":
    print(f"a média é {round(media(),5)}")