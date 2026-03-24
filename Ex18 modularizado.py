#declarar
valor1: int = 0
valor2: int = 0

def ordemDiferença ():
    global valor1
    global valor2
    diferença: int = 0
    if (valor1>valor2):
        diferença = (valor1-valor2)
        print ("Essa é a diferença entre seus números:", diferença)
    elif(valor1<valor2):
        diferença = (valor2-valor1)
        print ("Essa é a diferença entre seus números:", diferença)
    else:
        print ("Seus números são iguais")
    
def main():
    global valor1
    global valor2
    valor1 = int(input("Digite seu primeiro número: "))
    valor2 = int(input("Digite seu segundo número: "))
    ordemDiferença()

if __name__ == "__main__":
    main()     