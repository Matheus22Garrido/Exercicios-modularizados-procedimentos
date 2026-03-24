#declarar
a: float = 0.0
b: float = 0.0
c: float = 0.0
Delta: float = 0.0
raiz1: float = 0.0
raiz2: float = 0.0

#inicio
a = float(input("digite o número que acompanha x²: "))
b = float(input("digite o número que acompanha x: "))
c = float(input("digite o número sozinho: "))
Delta = (b * b - 4 * a * c)
if (Delta<0):
    print ("essa equação não tem raiz real")
elif (Delta>0):
    raiz1 = (-b + Delta**(1/2)/2*a)
    raiz2 = (-b - Delta**(1/2)/2*a)
    print ("Raiz 1:",raiz1)
    print ("Raiz 2:",raiz2)
else:
    raiz1 = (-b/2*a)
    print ("nessa equação delta é igual a zero e só tem 1 raiz real:",raiz1)
#fim