import pandas as pd
import plotly.express as px
import streamlit as st

rel_fem = pd.read_csv("relatorio_feminino.csv")

rel_mas = pd.read_csv("relatorio_masculino.csv")

status_ano_per_ing = rel_mas.groupby(['Status', 'Ano/Período de ingresso']).size().reset_index(name='Quantidade')
SAPIM = status_ano_per_ing

rel_fem['Gênero'] = 'Feminino'
rel_mas['Gênero'] = 'Masculino'

rels = pd.concat([rel_fem, rel_mas])

def remove_pontos_e_numeros(valor):
    return str(valor).split('.')[0]

colunas = ['Ano/Período de ingresso', 'Ano/Período última matrícula válida']
rels[colunas] = rels[colunas].applymap(remove_pontos_e_numeros)    
rels['% Integralizado'] = rels['% Integralizado'].str.replace('%', '') 
rels = rels.sort_values(by=['% Integralizado'])

# Garanta que a coluna "Ano/Período de ingresso" seja do tipo numérico
rels['Ano/Período de ingresso'] = pd.to_numeric(rels['Ano/Período de ingresso'], errors='coerce')

# Título da página
st.title('Distribuição de Gênero por Categoria e Ano')

# Adicione um seletor para a categoria
categorias_disponiveis = rels['Status'].unique()
categoria_selecionada = st.selectbox('Selecione a categoria desejada:', categorias_disponiveis)

# Adicione um seletor de ano com intervalo restrito de 2017 a 2023
anos_disponiveis = list(range(2017, 2024))  # Intervalo de 2017 a 2023
ano_desejado = st.selectbox('Selecione o ano desejado:', anos_disponiveis)

# Filtre os dados para a categoria e o ano selecionado
dados_filtrados = rels[(rels['Status'] == categoria_selecionada) & (rels['Ano/Período de ingresso'] == ano_desejado)]

# Calcule a contagem de gênero
dados = dados_filtrados['Gênero'].value_counts()

# Crie o gráfico de pizza
fig = px.pie(
    names=dados.index,
    values=dados.values,
    title=f'Distribuição de Gênero para a Categoria "{categoria_selecionada}" em {ano_desejado}',
    color_discrete_sequence=['gray', 'mediumpurple']
)

fig.update_traces(
    textfont=dict(size=16, color='white')
)

fig.update_layout(
    legend=dict(
        x=0.9,
        y=1.0,
        font=dict(family='Arial', size=16, color='white')
    ),
    title=dict(
        x=0.5,
        y=0.9,
        font=dict(family='Arial', size=20, color='black')
    )
)

# Exiba o gráfico no Streamlit
st.plotly_chart(fig)
