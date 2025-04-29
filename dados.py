import pandas as pd

df = pd.read_csv('Cópia de Base_despadronizada - Base_Corrigida.csv')

#Organizando a coluna sexo
df['sexo']=df['sexo'].replace({'M': 'Masculino','masc': 'Masculino', 'F': 'Feminino', 'fem':'Feminino'})

# Garantindo que os valores nas colunas são números e trocando ',' por '.'
df['nota_matematica'] = df['nota_matematica'].astype(str).str.replace(',', '.').astype(float)
df['nota_portugues'] = df['nota_portugues'].astype(str).str.replace(',', '.').astype(float)

# Criando a coluna de média
df['Média'] = (df['nota_matematica'] + df['nota_portugues'] + (df['frequencia'] / 10)) / 3

# Criando coluna de aprovados
df['aprovado'] = ['Sim' if media >= 7 else 'Não' for media in df['Média']]

#Ajustando as notas para ',' de volta
df['nota_matematica'] = df['nota_matematica'].map(lambda x: f'{x:.1f}'.replace('.', ','))
df['nota_portugues'] = df['nota_portugues'].map(lambda x: f'{x:.1f}'.replace('.', ','))
df['Média'] = df['Média'].map(lambda x: f'{x:.1f}'.replace('.', ','))

# Salvando arquivo final em excel (.xlsx)
df.to_excel('Base_Padronizada.xlsx', index=False)
