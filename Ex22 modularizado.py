#declarar
valor1: int = 0
valor2: int = 0

def numDiferentes():
    global valor1
    global valor2
    while (valor1==valor2):
        print ("É pra digitar números diferentes")
        valor1 = int(input("digite seu primeiro número: "))
        valor2 = int(input("digite seu segundo número: "))

def ordem():
    if (valor1>valor2):
        print ("Valores em ordem crescente: ",valor1,",", valor2, sep="")
    else:
        print ("Valores em ordem crescente: ",valor2,"," ,valor1, sep="")

def main():
    numDiferentes()
    ordem()

if (__name__ == "__main__"):
    main()