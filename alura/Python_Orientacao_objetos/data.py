class Data:
    def __init__(self,dia,mes,ano):
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    def formadata(self):
        print(f"{self.dia}/{self.mes:02}/{self.ano}")