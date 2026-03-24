#declarar
valor1: float = 0.0
valor2: float = 0.0

#inicio
valor1 = float(input("digite seu primeiro número: "))
valor2 = float(input("digite seu segundo número: "))
if (valor1<valor2):
    print("O número", valor2, 'é maior que', valor1)
elif (valor1>valor2):
    print ("O número", valor1, 'é ,maior que', valor2)
else:
    print ("Seus números são iguais")
#fim