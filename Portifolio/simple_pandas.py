import pandas as pd

data = {
    'Alunos': ['caio','jorge'],
    'idade': ['15','16'],
    'notas': [8,9]
}

df = pd.DataFrame(data, columns=['Alunos', 'idade','notas'])


def encontrar(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(data)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in data[i][j]: # se encontrarmos elemento ('ana')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices


r = encontrar('caio') # chamamos a função e salvamos em r
print(r) # imprime índices
print(pos_nome)
