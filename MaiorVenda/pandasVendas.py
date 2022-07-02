# Criado um código para identificar o momento em que o primeiro funcionario bater a marca mensal de R$ 55.000,00 em vendas

import pandas as pd

meses = 'janeiro fevereiro marco abril maio junho'.split()

for mes in meses:
    tabela_mes = pd.read_excel(mes + '.xlsx')
    if (tabela_mes['Vendas'] >= 55000).any():
        vendedor = tabela_mes.loc[tabela_mes['Vendas'] >= 55000,'Vendedor'].values[0]
        vendas = tabela_mes.loc[tabela_mes['Vendas'] >= 55000,'Vendas'].values[0]

print(f'Atenção, o vendedor {vendedor} alcançou a marca de R${vendas},00 em vendas no mês de {mes} e é o vencedor')
        