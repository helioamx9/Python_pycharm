
nomeCliente = input('Digite o nome do Cliente:')
dia = input('Digite o dia de vencimento:')
mes = input('Digite o mês de vencimento:')
valor = input('Digite o valor da fatura:')
msg = f'''
Olá, {nomeCliente}
A sua fatura com vencimento em {dia} de {mes} no valor de R$ {valor} está fechada.
'''
print(msg)