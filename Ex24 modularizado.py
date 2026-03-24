#declarar
numero: int = 0

def divisivel():
    if (numero%2==0):
        if(numero%3==0):
            print ("Seu número é divisível por 2 e 3")
        else:
            print("Seu número é divisível por 2")
    elif (numero%3==0):
            print ("Seu número é divisivel por 3")
    else:
        print ("Seu número não é divisivel nem por 2 nem por 3")

def main():
    global numero
    numero = int(input("Digite seu número: "))
    divisivel()

if (__name__=="__main__"):
    main()