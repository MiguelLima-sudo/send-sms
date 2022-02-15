# pandas
# openpyxl
# twilio

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9da294d20eba957e4a90333c8bf17903"
# Your Auth Token from twilio.com/console
auth_token  = "c259b27cb6b1f1eb241e949e35fc5396"
client = Client(account_sid, auth_token)


#Passo a Passo da Solução

#Abrir os 6 Arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a Meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5585997177826",
            from_="+19362263045",
            body=f'No mês {mes} alguém bateu a Meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)

#Para cada Arquivo:

# Verifcar se cada valor na coluna Vendas daquele Arquivo é maior que 55.000
# Se for maior que 55.000 -> enviar um SMS, com Nome, Mês e as Vendas do Vendedor
# Caso não seja maior que 55.000, não fazer nada.