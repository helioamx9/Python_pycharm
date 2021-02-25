import pymysql as sql

conexao = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Amx344290',
    db = 'erp',
    charset = 'utf8mb4',
    cursorclass = sql.cursors.DictCursor
)

autenticate = False

def logarCadastrar(decidir):
    usuarioExistente = 0
    autenticate = False
    masterUser = False
    if decisao ==1:
        nomee = input('Digite o usuario')
        senha = input('Digite a senha')
        for linha in resultado:
            if nomee == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] ==1:
                    masterUser = False
                elif linha['nivel']==2:
                    masterUser = True
                autenticate = True
            else:
                autenticate = False
        if not autenticate:
            print('Usuario ou senha incorreto')
    elif decisao == 2:
        print('faça seu cadastro')
        nomee = input('Digite o usuario')
        senha = input('Digite uma senha')

        for linha in resultado:
            if nomee == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1
    
        if usuarioExistente ==1:
            print('Usuario já cadastrado')

        elif usuarioExistente ==0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros (nome, senha, nivel) values (%s, %s, %s)', (nomee, senha, 1))
                    conexao.commit()

                print('Usuario cadastrado com sucesso')
            except:
                print('Erro ao cadastrar o usuario')
    return autenticate, masterUser

while not autenticate: 
    decisao = int(input('Digite \n'
    '[1] Logar\n'
    '[2] Cadastro de Usuarios'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
            print(resultado)
    except:
        print('erro ao conectar ao banco')
    autenticate, masterUser = logarCadastrar(decisao)
'''
cursor = conexao.cursor()

with conexao.cursor() as cursor:
    cursor.execute('select * from cadastros')

    dados = cursor.fetchall()

print(dados)

cursor.close()
conexao.close()
'''