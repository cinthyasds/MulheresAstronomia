import streamlit as st 
import pandas as pd
import plotly.express as px

def main():
	st.title('Análise dos dados de porcentagem de integralização de curso')
	#st.subheader('Dados', divider='violet')

if __name__ == '__main__':
	main()

st.markdown('<div style="text-align: justify;">\t Outro dado interessante de ser analisado e exposto é o da porcentagem de integralização de curso, isto é, o quanto o estudante já fez do seu curso que varia de 0% a 100%. Os gráficos apresentados mostram a média do percentual cursado (soma de todos os percentuais e divisão pela quantidade de estudantes) para o gêneros feminino e masculino em cada ano, considerando somente os alunos ativos. </div>', unsafe_allow_html=True)

#UFS

integralizacao = pd.read_csv('integralizacaoufs.csv')

cores = {'Feminino': 'mediumpurple', 'Masculino': 'gray'}

fig = px.bar(integralizacao, x='Ano/Período de ingresso', y='Média % Integralizado', color='Gênero', barmode='group',
             color_discrete_map=cores, labels={'porcentagem': 'Porcentagem (%)'})

fig.update_traces(texttemplate='%{y:.1f}%', textposition='outside')

fig.update_layout(
    title='Porcentagem por Ano e Gênero (UFS)',
    xaxis_title='Ano',
    yaxis_title='Porcentagem (%)',
    legend_title='Gênero',
    barmode='group',
    bargap=0.1  
)

st.plotly_chart(fig)


#UFRJ


integralizacao = pd.read_csv('integralizacaoufrj.csv')

cores = {'Feminino': 'mediumpurple', 'Masculino': 'gray'}

fig = px.bar(integralizacao, x='ano', y='porcentagem', color='genero', barmode='group',
             color_discrete_map=cores, labels={'porcentagem': 'Porcentagem (%)'})

fig.update_traces(texttemplate='%{y:.1f}%', textposition='outside')

fig.update_layout(
    title='Porcentagem por Ano e Gênero (UFRJ)',
    xaxis_title='Ano',
    yaxis_title='Porcentagem (%)',
    legend_title='Gênero',
    barmode='group',
    bargap=0.2,  
    bargroupgap=0.1, 
)

st.plotly_chart(fig)
