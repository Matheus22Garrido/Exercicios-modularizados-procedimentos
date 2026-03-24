#declarar
depósito: float = 0.0
tipo: int = 0
valor_reajustado: float = 0.0

#inicio
depósito = float(input("Digite quanto dinheiro foi colocado em aplicação: "))
while (tipo!=1 and tipo!=2):
    tipo = int(input("Digite o tipo de investimento, sendo 1 para poupança e 2 para renda fixa: "))
    print ("Tipo inválido")
if (tipo==1):
    valor_reajustado = (depósito*1.03)
    print ("Seu saldo reajustado pela poupança é",valor_reajustado,"reais")
elif (tipo==2):
    valor_reajustado = (depósito*1.05)
    print ("Seu saldo reajustado pela renda fixa é",valor_reajustado,"reais")
#fim