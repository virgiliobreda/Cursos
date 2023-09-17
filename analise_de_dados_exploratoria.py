import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataset_vendas_random.csv')


df = df.drop(columns=['CLIENTE'])
df = df.drop(columns=['SEXO'])
df = df.drop(columns=['ESTADO CIVIL'])
df = df.drop(columns=['LOJA'])
df = df.drop(columns=['VENDEDOR'])


print(df.head())
print(df.shape)

df['DATA'] = pd.to_datetime(df['DATA'])
df['PERIODO'] = pd.to_datetime(df['PERIODO'])
df['MES'] = pd.to_datetime(df['MES'])
print(df.dtypes)


desconto = df['DESCONTO'].sum() 
valor_total_sem_desc = df['VALOR'].sum() 
valor_total = valor_total_sem_desc - desconto 
print(valor_total)

media_valor_vendas = df['VALOR'].mean()
print(media_valor_vendas)

valores_nulos = df.isnull().sum()
print(valores_nulos)


#produtos_vendidos = df.groupby('PRODUTO')['QTDE'].sum().sort_values(ascending=False).plot.barh(title='Produtos Vendidos')
#print(produtos_vendidos)
#plt.xlabel('PRODUTO')
#plt.ylabel('QTDE')
#plt.show()

#df.groupby(df['DATA'].dt.year)['VALOR'].sum().plot.barh()
#plt.xlabel('DATA')
#plt.ylabel('VALOR')
#plt.show()

print(df.describe())

df.to_csv('df_vendas_novo.csv', index=False)