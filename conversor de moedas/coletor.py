def moeda():
    valor=float(input('me diga o valor de mercado da moeda(1 se for a de referencia): '))
    quantidade=float(input('me diga a quantidade de moedas(1 se for a que quer converter): '))
    return round(valor*quantidade,2)
def cambio(original,convertida):
    return round(original/convertida,2)
print(cambio(moeda(),moeda()))
