"""
Toda classe deve ser Coesa, ter apenas uma razão para existir.
"""

class Conta: # Classes são a "receita do programa" e são entituladas com o padrão CamelCase, classes são criadas com o intuito de "agrupar" Funções "que aqui são chamados de métodos" que são relacionadas a um objeto.
    
    def __init__(self, numero, titular, saldo, limite, codigo_banco): #__init__ é a forma de definir uma "função" construtora e o self é a variavel de refencia do python para este objeto.
        self.__numero = numero #Adicionar 2 underscores significa que este atributo é privado.
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        


    def depositar(self, valor):
        self.__saldo+= valor

    def __pode_sacar(self,valor_saque):
        valor_disponivel = self.__saldo+self.__limite
        return valor_saque <= valor_disponivel
    def sacar (self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor solicitado é superior ao limite em {abs(valor-(self.__saldo+self.__limite))}")

    def transferir(self,valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor
        
    @property
    def extrato(self):
        print(f'O saldo do Titular {self.__titular} é R$ {self.__saldo:.2f} \n O Limite da conta é de R$ {self.__limite}')

    @staticmethod # metodods estaticos é definido para a classe, algo que não muda com os objetos mas estão de alguma forma relacionados aos objetos
    def codigo_banco():
        return "001"
    
    @staticmethod # metodods estaticos é definido para a classe, algo que não muda com os objetos mas estão de alguma forma relacionados aos objetos
    def codigos_bancos():
        return {"Banco do Brasil":"001","Santander":"033","Bradesco":"247"}
    