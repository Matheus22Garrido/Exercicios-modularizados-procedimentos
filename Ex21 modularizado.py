#declarar
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
média: float = 0.0

#inicio
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
nota4 = float(input("digite sua quarta nota: "))
média = ((nota1 + nota2 + nota3 + nota4)/4)
if (média>6):
    print ("Você foi aprovado")
elif (média>=3 and média<6):
    print ("Você ficou pra fazer N3")
else:
    print ("Você foi reprovado")
#fim