#declarar
Horas_iniciais: int = 0
Horas_finais: int = 0
Minutos_iniciais: int = 0
Minutos_finais: int = 0
Duração: int = 0
Horas: int = 0
Minutos: int = 0

#inicio
Horas_iniciais = int(input("Digite a hora em que o jogo começou: "))
Minutos_iniciais = int(input("Digite os minutos em que o jogo começou: "))
Horas_finais = int(input("Digite a hora em que o jogo terminou: "))
Minutos_finais = int(input("Digite os minutos em que  o jogo terminou: "))
Duração = ((Horas_finais*60+Minutos_finais)-(Horas_iniciais*60+Minutos_iniciais))
if (Duração<0 and (Horas_finais<Horas_iniciais) or (Minutos_finais<Minutos_iniciais)):
    Duração = (Duração + 1440)
elif (Duração>1439):
    print ("O jogo durou 24 horas ou mais")
Horas = (Duração // 60)
Minutos = (Duração % 60)
print ("O jogo durou",Horas,"horas e",Minutos,"minutos")
#fim
