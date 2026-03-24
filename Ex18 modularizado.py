#declarar
valor1: int = 0
valor2: int = 0
diferença: int = 0

#inicio
valor1 = int(input("digite seu primeiro número: "))
valor2 = int(input("digite seu segundo número: "))
if (valor1>valor2):
    diferença = (valor1-valor2)
    print ("essa é a diferença entre seus números:", diferença)
elif(valor1<valor2):
    diferença = (valor2-valor1)
    print ("essa é a diferença entre seus números:", diferença)
else:
    print ("seus números são iguais")
#fim