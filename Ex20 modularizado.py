#declarar
a: float = 0.0
b: float = 0.0
c: float = 0.0
Delta: float = 0.0

def delta():
    global Delta
    Delta = (b*b-4*a*c)

def raizes():
    if (Delta<0):
        print ("Essa equação não tem raiz real")
    elif (Delta>0):
        raiz1 = (-b + (Delta**0.5))/(2*a)
        raiz2 = (-b - (Delta**0.5))/(2*a)
        print ("Raiz 1:",raiz1)
        print ("Raiz 2:",raiz2)
    else:
        raiz1 = (-b)/(2*a)
        print ("Nessa equação delta é igual a zero e só tem 1 raiz real:",raiz1)

def main():
    global a
    global b
    global c
    a = float(input("Digite o número que acompanha x²: "))
    b = float(input("Digite o número que acompanha x: "))
    c = float(input("Digite o número sozinho: "))
    delta()
    raizes()

if (__name__ == "__main__"):
    main()