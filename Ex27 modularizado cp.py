#declarar
Número_voltas: int = 0
Extensão: int = 0
Duração: int = 0

def velocidadeMedia(n,Δs,Δt):
    Velocidade_média: float = 0.0
    Velocidade_média = ((Δs*n)/1000)/(Δt/60)
    print("A velocidade média foi:",Velocidade_média,"km/h")

def recValores():
    global Número_voltas, Extensão, Duração
    Número_voltas = int(input("Digite quantas voltas foram percorridas: "))
    Extensão = int(input("Digite quantos metros tem cada volta: "))
    Duração = int(input("Digite quantos minutos demorou pra completar todas voltas: "))
    velocidadeMedia(Número_voltas, Extensão, Duração)

def main():
    recValores()

if (__name__=="__main__"):
    main()