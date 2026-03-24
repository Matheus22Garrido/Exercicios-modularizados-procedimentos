#declarar
x: int = 0
y: int = 0

#inicio
x = int(input("Digite seu primeiro valor: "))
y = int(input("Digite seu segundo valor: "))
if (x<y):
    if (y%x==0):
        print("O segundo valor é multiplo do primeiro ")
    else:
        print ("O segundo valor não é multiplo do primeiro")
elif (x>y):
    if (x%y==0):
        print ("O primeiro valor é multiplo do segundo")
    else:
        print ("O primeiro valor não é multiplo do segundo")
else:
    print ("Seus valores são iguais")
#fim