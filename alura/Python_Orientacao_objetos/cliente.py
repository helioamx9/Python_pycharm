
class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    @property #essa property ajuda a "simplificar" o codigo em sua execução premitindo acessar o metodo sem o uso de () ao ser chamado
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self,nome):
        self.__nome = nome