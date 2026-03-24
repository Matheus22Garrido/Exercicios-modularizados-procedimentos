#declarar
Velocidade_média: float = 0.0
Número_voltas: int = 0
Extensão: int = 0
Duração: int = 0

#inicio
Número_voltas = int(input("Digite quantas voltas foram percorridas: "))
Extensão = int(input("Digite quantos metros tem cada volta: "))
Duração = int(input("Digite quantos minutos demorou pra completar todas voltas: "))
Velocidade_média = (((Extensão*Número_voltas)/1000)/(Duração/60))
print ("A velocidade média foi",Velocidade_média,"km/h")
#fim