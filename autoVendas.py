
import cx_Oracle
import pandas as pd
import random 
import numpy as np

class AutoVendas:

    
    def __init__(self) -> None:
        pass

    def createList(r1, r2): 
        return np.arange(r1, r2+1, 1) 


    def _getData(self,query):
        conn = cx_Oracle.connect('ADMIN/Amx2208163442@naybolsas_high')
        oracleCur = conn.cursor()
        oracleCur.execute(query)
        _result = oracleCur.fetchall()
        return _result

    def _insertOracle(self,__insertQuery):
        conn = cx_Oracle.connect('ADMIN/Amx2208163442@naybolsas_high')
        oracleCur = conn.cursor()        
        oracleCur.execute(__insertQuery)
    
    def _commit(self):
        conn = cx_Oracle.connect('ADMIN/Amx2208163442@naybolsas_high')
        conn.commit()

    def cidades (self):
        query = "select id_cidade from tc_cidades"
        _cidades = list(AutoVendas._getData(query))
        _cidades = [item for t in _cidades for item in t]
        return _cidades

    def alimentos():

        query = "select NU_REGISTRO_PRODUTO from tc_alimentos"
        _alimentos = list(AutoVendas._getData(query))
        _alimentos = [item for t in _alimentos for item in t]
        return _alimentos

    def vendasRandom (_cidades,_alimentos):
        for cit in _cidades:
            __totalCidades = len(_cidades)
            __totalAlimentos = len(_alimentos)
            __escolhaCidade = _cidades[random.randrange(0,__totalCidades)]
            __escolhaAlimentos = _alimentos[random.randrange(0,__totalAlimentos)]
            __venda = random.randint(1,100)
            _cidades.remove(__escolhaCidade)
            _alimentos.remove(__escolhaAlimentos)
            __insertQuery = f"insert into tf_vendas (ID_CIDADE,NU_REGISTRO_PRODUTO,QTD_VENDA,DATA_VENDA) values ('{__escolhaCidade}','{__escolhaAlimentos}',{__venda},to_date(sysdate,'dd/mm/yy')+{random.randint(0,6)})"
            AutoVendas._insertOracle(__insertQuery)

    def realiza_vendas():
        for i in range(50):
            
            query = "select id_cidade from tc_cidades"

            _cidades = list(AutoVendas._getData(query))
            _cidades = [item for t in _cidades for item in t]

            query = "select NU_REGISTRO_PRODUTO from tc_alimentos"
            _alimentos = list(AutoVendas._getData(query))
            _alimentos = [item for t in _alimentos for item in t]
            AutoVendas.vendasRandom(_cidades,_alimentos)
        AutoVendas._commit()
        return print(i)

# Executa o gerador de vendas 
AutoVendas.realiza_vendas()