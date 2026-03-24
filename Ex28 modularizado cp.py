#declarar
venda_mensal: int = 0
preço_atual: float = 0.0
preço_novo: float = 0.0

#inicio
venda_mensal = int(input("Digite qual foi a venda desse mes do seu produto: "))
preço_atual = float(input("Digite o preço atual do seu produto: "))
if (venda_mensal<500) and (preço_atual<30):
    preço_novo = (preço_atual*1.1)
    print ("Seu produto depois do reajuste será",preço_novo,"reais")
elif (venda_mensal>=500 and venda_mensal<1000) and (preço_atual>=30 and preço_atual<80):
    preço_novo = (preço_atual*1.15)
    print ("Seu produto depois do reajuste será ",preço_novo,"reais")
elif (venda_mensal>=1000) and (preço_atual>=80):
    preço_novo = (preço_atual*0.95)
    print ("Seu produto depois do reajuste será ",preço_novo,"reais")
#fim