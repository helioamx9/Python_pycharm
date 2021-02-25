import random
def jogar_advinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


    numero_secreto = random.randint(1,100+1)
    total_de_tentativas = int(input('Escolha o nível de Dificuldade:\n (1) Difícil \n (2) Normal \n (3) Fácil'))*10

    rodada = 1
    pontos = 1000
    while rodada < (total_de_tentativas +1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        lista = []
        for i in range(1,100+1):
            lista.append(int(i))
            i+=1
        
        chute_str = input("Digite um numero entre 1 e 100: ")
        if int(chute_str) not in lista:
            
            print("Você digitou um numero invalido!")
            chute_str = input("Digite um numero entre 1 e 100: ")

        print("Você digitou ",chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute ==numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("você acertou!")
            break
        else:
            if(maior):
                print("Você digitou um número maior que o número secreto!")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos    

        rodada+= 1    
    print(f"Fim de Jogo, O numero secréto éra {numero_secreto}.\n Sua pontuação foi de {pontos}")   

if __name__ == "__main__":
    jogar_advinhacao()