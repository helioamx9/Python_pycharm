import forca
import adivinhacao

print("*" * 34)
print("*********Escolha seu Jogo*********")
print("*" * 34)

jogo = int(input('(1) Advinhação\n(2) Forca\n'))

if (jogo == 1):
    print('Jogando Advinhação!')
    adivinhacao.jogar_advinhacao()
elif (jogo == 2 ):
    print('Jogando Forca!')
    forca.jogar_forca()
