import random
def jogar_forca():
    print("*"*34)
    print("Bem - vindo ao Jogo da Forca")
    print("*"*34)

    arquivo = open("palavras.txt","r")
    
    palavras=[]

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    tentativas =0
    print(letras_acertadas)
    while(not enforcou and not acertou):
    
        chute = str(input("Qual Letra?")).upper().strip()

        if chute in palavra_secreta:

            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra    
                index +=1

            print(letras_acertadas)
        else:
            tentativas+= 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Parabéns você venceu o jogo")
    else:
        print(f"você foi enforcado:(\n A palavra éra {palavra_secreta}")
        


    print("Fim do Jogo")

if __name__ == "__main__":
    jogar_forca()