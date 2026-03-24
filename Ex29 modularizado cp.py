#declarar
depósito: float = 0.0
tipo: int = 0
valor_reajustado: float = 0.0

def Tipo():
    global tipo
    while (tipo!=1 and tipo!=2):
        tipo = int(input("Digite o tipo de investimento, sendo 1 para poupança e 2 para renda fixa: "))
        if (tipo==1 or tipo==2):
            continue
        print ("Tipo inválido")

def Reajuste(t,vR,d):
    if (t==1):
        vR = (d*1.03)
        print ("Seu saldo reajustado pela poupança é",vR,"reais")
    elif (t==2):
        vR = (d*1.05)
        print ("Seu saldo reajustado pela renda fixa é",vR,"reais")

def main():
    global depósito
    Tipo()
    depósito = float(input("Digite quanto dinheiro foi colocado em aplicação: "))
    Reajuste(tipo,valor_reajustado,depósito)

if (__name__=="__main__"):
    main()