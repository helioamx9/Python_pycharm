#!python3
notas =[]
indice = 1
while len(notas) < 4:
    nota = int(input(f"Digite a {indice}ª nota do aluno"))
    notas.append(nota)
    indice+=1

print(f'A média Aritimética é ',sum(notas)/len(notas))    
