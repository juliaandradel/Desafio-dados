import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


#Carregando a planilha já tratada do desafio anterior
df = pd.read_excel('Base_padronizada.xlsx')

#Calculando quantos alunos foram aprovados e reprovados
contagem_aprovado = df['aprovado'].value_counts()
#Calculando o percentual
percentual_aprovado = df['aprovado'].value_counts(normalize=True) * 100

#Gerando gráfico pizza
labels_aprovado = []
for status_aprovado, quant_aprovado, perc_aprovado in zip(contagem_aprovado.index, contagem_aprovado.values, percentual_aprovado):
    label_aprovado = f'{status_aprovado} ({quant_aprovado} - {perc_aprovado:.1f}%)'
    labels_aprovado.append(label_aprovado)


plt.figure(figsize=(6, 6))
plt.pie(contagem_aprovado, labels=labels_aprovado, autopct='%1.1f%%', startangle=90, colors=['#FF1493', '#9370DB'])
plt.title('Gráfico de Aprovação')
plt.axis('equal') 
plt.tight_layout()
plt.savefig('grafico-aprovacao')

insight1= 'A maioria dos alunos foram reprovados, o que indica um desempenho não satisfatório da turma.É importante agora analisar os motivos que levaram a esse mal rendimento.'

#Contando quantos alunos se identificam com sexo masculino e feminino
contagem_sexo= df['sexo'].value_counts()
#Calculando o percentual
percentual_sexo = df['sexo'].value_counts(normalize=True) * 100

#Gerando gráfico pizza
labels_sexo = []
for status_sexo, quant_sexo, perc_sexo in zip(contagem_sexo.index, contagem_sexo.values, percentual_sexo):
    label_sexo = f'{status_sexo} ({quant_sexo} - {perc_sexo:.1f}%)'
    labels_sexo.append(label_sexo)

plt.figure(figsize=(6, 6))
plt.pie(contagem_sexo, labels=labels_sexo, autopct='%1.1f%%', startangle=90, colors=['#FF1493', '#9370DB'])
plt.title('Gráfico de distribuição por sexo')
plt.axis('equal') 
plt.tight_layout()
plt.savefig('grafico-sexo')

insight2= 'A quantidade de Homens e Mulheres na turma é quase equivalente, apresentando um número levemente maior de pessoas que se identificam com o sexo feminino, do que os que se indentificam com o masculino. Isso indica uma boa distribuição de sexos.'

#Ordenando os 5 Alunos com as Melhores Médias
df['Média'] = df['Média'].astype(str).str.replace(',', '.').astype(float)
df_ordenado_media = df.sort_values(by='Média', ascending=False).head(5)

#Criando gráfico de barras horizontais
plt.figure(figsize=(8, 5))
bars = plt.barh(df_ordenado_media['nome'], df_ordenado_media['Média'], color='#9370DB')
plt.xlabel('Média', fontsize=12)
plt.title('Os 5 Alunos com as Melhores Médias', fontsize=14, pad=20)
plt.gca().invert_yaxis()  
plt.xlim(7, 10)  
plt.tight_layout()
plt.savefig('grafico-melhores-medias')

insight3= 'Os 5 alunos que apresentaram as maiores médias foram: Mariana Barbosa, Miguel teixeira, Fernando Pinto, Renan Nogueira e Pietro Almeida. O aluno com a maior média apresentou uma média de 8.6, número cerca de 48% maior do que a média da turma, de 5.79. Todos os alunos possuem médias acima de 8.0, o que indica um ótimo desempenho acadêmico, mas com margem para melhora.'

# Ordenando os 5 Alunos mais Assíduos
df_ordenado_frequencia = df.sort_values(by='frequencia', ascending=False).head(5)

# Criando gráfico
plt.figure(figsize=(8, 5))
plt.barh(df_ordenado_frequencia['nome'], df_ordenado_frequencia['frequencia'], color='#9370DB')
plt.xlabel('Frequência')
plt.title('Os 5 Alunos mais assíduos')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('grafico-melhores-frequencias')

insight4= 'Os 5 alunos mais assíduos foram: Clarice da Mota, Renan Novaes, Maria Luiza Silva, Laís Farias, Ana Carolina Farias.Todos os 5 estudantes mais assíduos obtiveram frequência perto de 100. Percebemos que apesar das altas taxas de frequência, os 5 alunos mais assíduos não são os mesmos alunos que fazem parte dos 5 com as melhores médias, mostrando que os dados não se relacionam diretamente.'

# Gerando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Título
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Gráficos de desempenho acadêmico", ln=True, align="C")
pdf.ln(10)

# Gráfico 1
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, "1. Gráfico de Aprovação", ln=True)
pdf.image("grafico-aprovacao.png", w=170)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, insight1)
pdf.ln(5)

# Gráfico 2
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, "2. Gráfico de Distribuição por Sexo", ln=True)
pdf.image("grafico-sexo.png", w=170)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, insight2)
pdf.ln(5)

# Gráfico 3
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, "3. Os 5 alunos com as melhores médias", ln=True)
pdf.image("grafico-melhores-medias.png", w=170)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, insight3)
pdf.ln(5)

# Gráfico 4
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, "4. Os 5 alunos mais assíduos", ln=True)
pdf.image("grafico-melhores-frequencias.png", w=170)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, insight4)

pdf.output("relatorio_final.pdf")
