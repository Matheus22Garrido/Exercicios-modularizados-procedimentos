#declarar
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
média: float = 0.0

def recValores():
    global nota1
    global nota2
    global nota3
    global nota4
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    nota4 = float(input("Digite sua quarta nota: "))

def media():
    global média
    média = (nota1+nota2+nota3+nota4)/4

def aprovação():
    if (média>6):
      print ("Você foi aprovado")
    elif (média>=3 and média<6):
        print ("Você ficou pra fazer N3")
    else:
        print ("Você foi reprovado")

def main():
    recValores()
    media()
    aprovação()

if (__name__ == "__main__"):
    main()