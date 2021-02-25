'''
This a little program to login and signup users on oracle DB
'''
import cx_Oracle

# here a config to connect on DB
conn = cx_Oracle.connect('ADMIN/Amx2208163442@naybolsas_high')

autentico = False
#function to validate user or register a new.
def logar(decisao):
    if decisao ==1:
        usuario = input('Digite o usuario:\n')
        senha = input('Digite a senha:\n')
        for linha in query:
            if usuario == linha['ID_USER'] and senha == linha['PASS']:
                autentico = True
                print('Bem Vindo {}'.format(linha['NAME_USER'].title()))
            else:
                autentico = False
        if not autentico:
            print('Usuario ou senha incorretos')
    elif decisao ==2:
        name_user = input('Digite um Nome de Usuario:\n').lower()
        senha = input('Digite um senha')
        try:
            with conn.cursor() as cursor:
                cursor.execute("insert into tc_users_erp (name_user, pass) values ('{}', '{}')".format(name_user, senha))
                cursor.execute('commit work')
                cursor.execute("select id_user from tc_users_erp where name_user = '{}' and pass = '{}'".format(name_user, senha)), 
                cursor.rowfactory = lambda *args: dict(zip([d[0] for d in cursor.description], args))
                result = cursor.fetchall()
                for linha in result:
                    print('Bem Vindo {}, sua matricula é: {}'.format(name_user.title(),linha['ID_USER']))
                autentico = True
            
        except:
            print('Erro ao conectar ao banco de dados')
# here the program load table of users on oracle DB
while not autentico:   
    decisao = int(input('[1] LOGAR''\n'
    '\n[2] CADASTRAR\n'))
    try:
        with conn.cursor() as cursor:
            cursor.execute('select to_char(ID_USER) ID_USER, NAME_USER, PASS from tc_users_erp')
            cursor.rowfactory = lambda *args: dict(zip([d[0] for d in cursor.description], args))
            query = cursor.fetchall()
            autentico = True
            #print(query)
    except:
        print('Erro ao conectar ao banco de dados')

logar(decisao)