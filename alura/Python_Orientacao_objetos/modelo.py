class Programa:
    def __init__(self, nome, ano ):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    
    def dar_likes(self):
        self._likes +=1


    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.likes} likes'
        


class Filme(Programa):
    def __init__(self, nome, ano , duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min- {self.likes} likes'
    


class Serie(Programa):
    def __init__(self, nome, ano , temporadas,):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self): # sempre que precisarmos retornar um print de atributos devemos utilisar este metodo Build-in para retornar o objeto como string.
       return f'{self._nome} - {self.ano} - {self.temporadas} temporadas {self.likes} likes'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__ (self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)



vingadores = Filme('vingadores - guerra infinita',2018,160)
atlanta = Serie('atlanta', 2019,5)
tmep = Filme('todo mundo em panico', 1999,100)
demolidor = Serie('demolidor',2008,6)

vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_e_series = [vingadores, atlanta]
playlist_fim_de_semana = Playlist('fim de semana',[vingadores,atlanta,tmep,demolidor])

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho: {len(playlist_fim_de_semana.listagem)}')
