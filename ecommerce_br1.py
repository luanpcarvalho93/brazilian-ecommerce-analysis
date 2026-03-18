import pandas as pd

orders = pd.read_csv(r"C:\Users\Luan Carvalho\Documents\archive (2)\Ecommerce-analises\data\orders.csv")
print(orders.head())

orders.shape
orders.info()

orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

orders['month'] = orders['order_purchase_timestamp'].dt.to_period('M')

orders.groupby('month').size()

import matplotlib.pyplot as plt

orders.groupby('month').size().plot()

plt.title('Pedidos por Mês')
plt.xlabel('Mês')
plt.ylabel('Número de Pedidos')
plt.savefig("pedidos_por_mes.png")

plt.show()

###Quantos pedidos foram entregues, cancelados ou atrasados###
orders['order_status'].value_counts().plot(kind='bar')

plt.title('Status dos Pedidos')
plt.xlabel('Status')
plt.ylabel('Quantidade')
plt.savefig("status_pedido.png")

plt.show()

###Pedidos por dia da Semana###
orders['weekday'] = orders['order_purchase_timestamp'].dt.day_name()
orders['weekday'].value_counts().plot(kind='bar')

plt.title('Pedidos por dia da semana')
plt.xlabel('Dia')
plt.ylabel('Número de Pedidos')

plt.savefig("pedidos_por_dia.png")

plt.show()

