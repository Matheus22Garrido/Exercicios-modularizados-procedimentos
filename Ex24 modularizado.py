#declarar
numero: int = 0

#inicio
numero = int(input("Digite seu número: "))
if (numero%2==0 and numero%3==0):
    print ("Seu número é divisível por 2 e 3")
else:
    print ("Seu número não é divisível por 2 e 3")
#fim