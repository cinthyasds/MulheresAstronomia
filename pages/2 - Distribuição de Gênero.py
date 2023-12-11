import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown("")
st.title('Gráfico de barras da distribuição de gênero por ano para as duas universidades')
st.markdown("")

conta_mas2 = pd.read_csv('conta_masufsNUMERO.csv')
conta_fem2 = pd.read_csv('conta_femufsNUMERO.csv')
nconta_masufrj = pd.read_csv('contagem_masrjNUMERO.csv')
nconta_femufrj = pd.read_csv('contagem_femrjNUMERO.csv')

#UFS
conta_fem2_2017 = conta_fem2[(conta_fem2['Ano/Período de ingresso'] == 2017)]
conta_mas2_2017 = conta_mas2[(conta_mas2['Ano/Período de ingresso'] == 2017)]
conta_fem2_2018 = conta_fem2[(conta_fem2['Ano/Período de ingresso'] == 2018)]
conta_mas2_2018 = conta_mas2[(conta_mas2['Ano/Período de ingresso'] == 2018)]
conta_fem2_2019 = conta_fem2[(conta_fem2['Ano/Período de ingresso'] == 2019)]
conta_mas2_2019 = conta_mas2[(conta_mas2['Ano/Período de ingresso'] == 2019)]
conta_fem2_2020 = conta_fem2[(conta_fem2['Ano/Período de ingresso'] == 2020)]
conta_mas2_2020 = conta_mas2[(conta_mas2['Ano/Período de ingresso'] == 2020)]
conta_fem2_2021 = conta_fem2[(conta_fem2['Ano/Período de ingresso'] == 2021)]
conta_mas2_2021 = conta_mas2[(conta_mas2['Ano/Período de ingresso'] == 2021)]
conta_fem2_2022 = conta_fem2[(conta_fem2['Ano/Período de ingresso'] == 2022)]
conta_mas2_2022 = conta_mas2[(conta_mas2['Ano/Período de ingresso'] == 2022)]
conta_fem2_2023 = conta_fem2[(conta_fem2['Ano/Período de ingresso'] == 2023)]
conta_mas2_2023 = conta_mas2[(conta_mas2['Ano/Período de ingresso'] == 2023)]

#UFRJ
nconta_femufrj_17 = nconta_femufrj[(nconta_femufrj['Ano/Período de ingresso'] == 2017)]
nconta_masufrj_17 = nconta_masufrj[(nconta_masufrj['Ano/Período de ingresso'] == 2017)]
nconta_femufrj_18 = nconta_femufrj[(nconta_femufrj['Ano/Período de ingresso'] == 2018)]
nconta_masufrj_18 = nconta_masufrj[(nconta_masufrj['Ano/Período de ingresso'] == 2018)]
nconta_femufrj_19 = nconta_femufrj[(nconta_femufrj['Ano/Período de ingresso'] == 2019)]
nconta_masufrj_19 = nconta_masufrj[(nconta_masufrj['Ano/Período de ingresso'] == 2019)]
nconta_femufrj_20 = nconta_femufrj[(nconta_femufrj['Ano/Período de ingresso'] == 2020)]
nconta_masufrj_20 = nconta_masufrj[(nconta_masufrj['Ano/Período de ingresso'] == 2020)]
nconta_femufrj_21 = nconta_femufrj[(nconta_femufrj['Ano/Período de ingresso'] == 2021)]
nconta_masufrj_21 = nconta_masufrj[(nconta_masufrj['Ano/Período de ingresso'] == 2021)]
nconta_femufrj_22 = nconta_femufrj[(nconta_femufrj['Ano/Período de ingresso'] == 2022)]
nconta_masufrj_22 = nconta_masufrj[(nconta_masufrj['Ano/Período de ingresso'] == 2022)]
nconta_femufrj_23 = nconta_femufrj[(nconta_femufrj['Ano/Período de ingresso'] == 2023)]
nconta_masufrj_23 = nconta_masufrj[(nconta_masufrj['Ano/Período de ingresso'] == 2023)]

#ufs
soma_fem_2017 = conta_fem2_2017['Contagem_Feminino'].sum()
soma_fem_2018 = conta_fem2_2018['Contagem_Feminino'].sum()
soma_fem_2019 = conta_fem2_2019['Contagem_Feminino'].sum()
soma_fem_2020 = conta_fem2_2020['Contagem_Feminino'].sum()
soma_fem_2021 = conta_fem2_2021['Contagem_Feminino'].sum()
soma_fem_2022 = conta_fem2_2022['Contagem_Feminino'].sum()
soma_fem_2023 = conta_fem2_2023['Contagem_Feminino'].sum()

soma_mas_2017 = conta_mas2_2017['Contagem_Masculino'].sum()
soma_mas_2018 = conta_mas2_2018['Contagem_Masculino'].sum()
soma_mas_2019 = conta_mas2_2019['Contagem_Masculino'].sum()
soma_mas_2020 = conta_mas2_2020['Contagem_Masculino'].sum()
soma_mas_2021 = conta_mas2_2021['Contagem_Masculino'].sum()
soma_mas_2022 = conta_mas2_2022['Contagem_Masculino'].sum()
soma_mas_2023 = conta_mas2_2023['Contagem_Masculino'].sum()

#ufrj
soma_fem_17 = nconta_femufrj_17['Contagem_Feminino'].sum()
soma_fem_18 = nconta_femufrj_18['Contagem_Feminino'].sum()
soma_fem_19 = nconta_femufrj_19['Contagem_Feminino'].sum()
soma_fem_20 = nconta_femufrj_20['Contagem_Feminino'].sum()
soma_fem_21 = nconta_femufrj_21['Contagem_Feminino'].sum()
soma_fem_22 = nconta_femufrj_22['Contagem_Feminino'].sum()
soma_fem_23 = nconta_femufrj_23['Contagem_Feminino'].sum()

soma_mas_17 = nconta_masufrj_17['Contagem_Masculino'].sum()
soma_mas_18 = nconta_masufrj_18['Contagem_Masculino'].sum()
soma_mas_19 = nconta_masufrj_19['Contagem_Masculino'].sum()
soma_mas_20 = nconta_masufrj_20['Contagem_Masculino'].sum()
soma_mas_21 = nconta_masufrj_21['Contagem_Masculino'].sum()
soma_mas_22 = nconta_masufrj_22['Contagem_Masculino'].sum()
soma_mas_23 = nconta_masufrj_23['Contagem_Masculino'].sum()


#ufs
total17_ufs = soma_fem_2017 + soma_mas_2017 
total18_ufs = soma_fem_2018 + soma_mas_2018 
total19_ufs = soma_fem_2019 + soma_mas_2019 
total20_ufs = soma_fem_2020 + soma_mas_2020 
total21_ufs = soma_fem_2021 + soma_mas_2021 
total22_ufs = soma_fem_2022 + soma_mas_2022 
total23_ufs = soma_fem_2023 + soma_mas_2023 

#ufrj
total17_ufrj = soma_fem_17 + soma_mas_17
total18_ufrj = soma_fem_18 + soma_mas_18
total19_ufrj = soma_fem_19 + soma_mas_19
total20_ufrj = soma_fem_20 + soma_mas_20
total21_ufrj = soma_fem_21 + soma_mas_21
total22_ufrj = soma_fem_22 + soma_mas_20
total23_ufrj = soma_fem_23 + soma_mas_23


pctfem17_ufs = soma_fem_2017/total17_ufs*100
pctfem18_ufs = soma_fem_2018/total18_ufs*100
pctfem19_ufs = soma_fem_2019/total19_ufs*100
pctfem20_ufs = soma_fem_2020/total20_ufs*100
pctfem21_ufs = soma_fem_2021/total21_ufs*100
pctfem22_ufs = soma_fem_2022/total22_ufs*100
pctfem23_ufs = soma_fem_2023/total23_ufs*100

pctmas17_ufs = soma_mas_2017/total17_ufs*100
pctmas18_ufs = soma_mas_2018/total18_ufs*100
pctmas19_ufs = soma_mas_2019/total19_ufs*100
pctmas20_ufs = soma_mas_2020/total20_ufs*100
pctmas21_ufs = soma_mas_2021/total21_ufs*100
pctmas22_ufs = soma_mas_2022/total22_ufs*100
pctmas23_ufs = soma_mas_2023/total23_ufs*100


pctfem17_ufrj = soma_fem_17/total17_ufrj*100
pctfem18_ufrj = soma_fem_18/total18_ufrj*100
pctfem19_ufrj = soma_fem_19/total19_ufrj*100
pctfem20_ufrj = soma_fem_20/total20_ufrj*100
pctfem21_ufrj = soma_fem_21/total21_ufrj*100
pctfem22_ufrj = soma_fem_22/total22_ufrj*100
pctfem23_ufrj = soma_fem_23/total23_ufrj*100

pctmas17_ufrj = soma_mas_17/total17_ufrj*100
pctmas18_ufrj = soma_mas_18/total18_ufrj*100
pctmas19_ufrj = soma_mas_19/total19_ufrj*100
pctmas20_ufrj = soma_mas_20/total20_ufrj*100
pctmas21_ufrj = soma_mas_21/total21_ufrj*100
pctmas22_ufrj = soma_mas_22/total22_ufrj*100
pctmas23_ufrj = soma_mas_23/total23_ufrj*100


df = pd.DataFrame({
    'Ano': ['2017','2018', '2019', '2020', '2021', '2022', '2023'],
    'Feminino_ufs': [pctfem17_ufs, pctfem18_ufs, pctfem19_ufs, pctfem20_ufs, pctfem21_ufs, pctfem22_ufs, pctfem23_ufs],
    'Masculino_ufs': [pctmas17_ufs, pctmas18_ufs, pctmas19_ufs, pctmas20_ufs, pctmas21_ufs, pctmas22_ufs, pctmas23_ufs],
    'Feminino_ufrj': [pctfem17_ufrj, pctfem18_ufrj, pctfem19_ufrj, pctfem20_ufrj, pctfem21_ufrj, pctfem22_ufrj, pctfem23_ufrj],
    'Masculino_ufrj': [pctmas17_ufrj, pctmas18_ufrj, pctmas19_ufrj, pctmas20_ufrj, pctmas21_ufrj, pctmas22_ufrj, pctmas23_ufrj],
})



fig3 = px.bar(df, x='Ano', y=['Feminino_ufs', 'Masculino_ufs', 'Feminino_ufrj', 'Masculino_ufrj'], title=f'Distribuição de Gênero de 2017 a 2023 (UFRJ)',
                 labels={'value': 'Porcentagem', 'variable': 'Gênero'}, color_discrete_sequence=['mediumpurple', 'gray', 'purple', 'dimgray'],
                 width=1000, height=500
                )

fig3.update_layout(
    xaxis=dict(tickangle=-45, tickmode='array'),
    legend_title='Porcentagem por gênero',
    font=dict(family='Arial', color='white'),
    barmode='group',
        #plot_bgcolor='white'
    )

for idx, row in df.iterrows():
        fig3.add_annotation(
            x=row['Ano'],
            y=row['Feminino_ufs'],
            text=f"{row['Feminino_ufs']:.0f}%",
            showarrow=False,
            font=dict(size=12, color='white'),
            xanchor='right',
            yanchor='bottom',
            textangle=-45
        )
        fig3.add_annotation(
            x=row['Ano'],
            y=row['Masculino_ufs'],
            text=f"{row['Masculino_ufs']:.0f}%",
            showarrow=False,
            font=dict(size=12, color='white'),
            xanchor='center',
            yanchor='top',
            textangle=-45
        )

        fig3.add_annotation(
            x=row['Ano'],
            y=row['Feminino_ufrj'],
            text=f"{row['Feminino_ufrj']:.0f}%",
            showarrow=False,
            font=dict(size=12, color='white'),
            xanchor='center',
            yanchor='bottom',
            textangle=-45
        )

            
        fig3.add_annotation(
            x=row['Ano'],
            y=row['Masculino_ufrj'],
            text=f"{row['Masculino_ufrj']:.0f}%",
            showarrow=False,
            font=dict(size=12, color='white'),
            xanchor='left',
            yanchor='bottom',
            textangle=-45
        )

        
st.plotly_chart(fig3)

##################################################################################

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
st.markdown('<div style="text-align: justify;">Os gráficos a seguir nos permitem analisar a distribuição de participantes do gênero feminino e masculino no curso de Astrofísica da UFS e da UFRJ. Esses gráficos são essenciais para destacar as mudanças significativas que ocorreram ao longo dos anos no número de mulheres matriculadas no curso.</div>', unsafe_allow_html=True)
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
        font=dict(family='Arial', size=20, color='white')
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
        x=0.0,
        y=0.9,
        font=dict(family='Arial', size=20, color='white')
    )
)

st.plotly_chart(fig)






