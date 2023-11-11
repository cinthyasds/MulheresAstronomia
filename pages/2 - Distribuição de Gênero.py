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


rels['Ano/Período de ingresso'] = pd.to_numeric(rels['Ano/Período de ingresso'], errors='coerce')


st.title('Distribuição de Gênero por Categoria e Ano')

st.markdown("")
st.markdown('<div style="text-align: justify;">Os gráficos a seguir nos permitem analisar a distribuição de participantes do gênero feminino e masculino no curso de Astrofísica da UFS. Esses gráficos são essenciais para destacar as mudanças significativas que ocorreram ao longo dos anos no número de mulheres matriculadas no curso.</div>', unsafe_allow_html=True)
st.markdown("")
st.markdown('**Os gráficos estão divididos por categorias qu são:**')
st.write('* Excluído: Removido definitivamente.')
st.write('* Cancelado: Interrupção antes da conclusão.')
st.write('* Ativo: Em andamento.')
st.write('* Pendente Cadastro: Processo de inscrição incompleto.')
st.write('* Concluído: Curso finalizado.')
st.write('* Trancado: Matrícula temporariamente pausada.')
st.write('* Formando: Próximo da formatura.')
st.markdown("")

#UFS 

st.subheader('Distribuição de gênero UFS')

categorias_disponiveis = rels['Status'].unique()
categoria_selecionada = st.selectbox('Selecione a categoria desejada:', categorias_disponiveis)

anos_disponiveis = list(range(2017, 2024))  
ano_desejado = st.selectbox('Selecione o ano desejado:', anos_disponiveis)

dados_filtrados = rels[(rels['Status'] == categoria_selecionada) & (rels['Ano/Período de ingresso'] == ano_desejado)]

dados = dados_filtrados['Gênero'].value_counts()

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
        x=0.0,
        y=0.9,
        font=dict(family='Arial', size=16, color='white')
    )
)

st.plotly_chart(fig)

#UFRJ

st.subheader('Distribuição de gênero UFRJ')

rjdist = pd.read_csv("rjdist_genero.csv")

rjcategorias_disponiveis = rjdist['Status'].unique()
rjcategoria_selecionada = st.selectbox('Para a UFRJ, selecione a categoria desejada:', rjcategorias_disponiveis)

rjanos_disponiveis = list(range(2017, 2024))  
rjano_desejado = st.selectbox('Selecione o ano desejado (UFRJ):', rjanos_disponiveis)

rjdados_filtrados = rjdist[(rjdist['Status'] == rjcategoria_selecionada) & (rjdist['Ano/Período de ingresso'] == rjano_desejado)]

rjdados = rjdados_filtrados['qtd']

fig = px.pie(
    values=rjdados,
    names=rjdados_filtrados['Gênero'],
    title=f'Distribuição de Gênero para a Categoria "{rjcategoria_selecionada}" em {rjano_desejado} UFRJ',
    color_discrete_sequence=['gray', 'mediumpurple']
)

fig.update_traces(
    textinfo='percent+label',
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

st.plotly_chart(fig)






