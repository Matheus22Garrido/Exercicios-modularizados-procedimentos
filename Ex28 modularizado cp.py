#declarar
venda_mensal: int = 0
preço_atual: float = 0.0

def recValores():
    global venda_mensal, preço_atual
    venda_mensal = int(input("Digite qual foi a venda desse mes do seu produto: "))
    preço_atual = float(input("Digite o preço atual do seu produto: "))
    calcPnovo(venda_mensal,preço_atual)

def calcPnovo(vM,pA):
    preço_novo: float = 0.0
    if (vM<500) and (pA<30):
        preço_novo = (pA*1.1)
        print ("Seu produto depois do reajuste será",preço_novo,"reais")
    elif (vM>=500 and vM<1000) and (pA>=30 and pA<80):
        preço_novo = (pA*1.15)
        print ("Seu produto depois do reajuste será ",preço_novo,"reais")
    elif (vM>=1000) and (pA>=80):
        preço_novo = (pA*0.95)
        print ("Seu produto depois do reajuste será ",preço_novo,"reais")

def main():
    recValores()

if (__name__=="__main__"):
    main()