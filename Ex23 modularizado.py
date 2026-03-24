#declarar
valor1: float = 0.0
valor2: float = 0.0
valor3: float = 0.0
valor4: float = 0.0

def entrada():
    global valor1,valor2,valor3,valor4
    while True:
        valor1 = float(input("Digite seu primeiro valor: "))
        valor2 = float(input("Digite seu segundo valor: "))
        valor3 = float(input("Digite seu terceiro valor: "))
        if valor1 <= valor2 <= valor3:
            break
        print("Ordem ->CRESCENTE<-")
    valor4 = float(input("Digite seu quarto valor: "))

def ordem():
    if (valor4<=valor1):
        print (valor4,valor1,valor2,valor3, sep=", ")
    elif (valor4<=valor2):
        print (valor1,valor4,valor2,valor3, sep=", ")
    elif (valor4<=valor3):
        print (valor1,valor2,valor4,valor3, sep=", ")
    else:
        print (valor1,valor2,valor3,valor4, sep=", ")

def main():
    entrada()
    ordem()

if (__name__=="__main__"):
    main()