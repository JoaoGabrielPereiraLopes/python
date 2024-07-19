def juros(meses,juros,mensaliidade):
    dinheiro=int(input('diga o valor do capital inicial do investimento: '))
    tentativas=0
    while tentativas<meses:
        dinheiro+=dinheiro*(juros/100)
        dinheiro+=mensaliidade
        tentativas+=1
    return round(dinheiro,2)
def coletor_meses():
    return int(input('diga o numero de tempo em meses do investimento: '))
def coletor_juros():
    return int(input('diga o valor do juros do investimento: '))
def coletor_mensalidade():
    return int(input('diga o valor da mensalidade do investimento: '))
print(juros(coletor_meses(),coletor_juros(),coletor_mensalidade()))
