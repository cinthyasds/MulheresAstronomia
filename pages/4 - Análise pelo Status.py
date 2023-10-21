import streamlit as st 
#from PIL import Image
import pandas as pd
import plotly.express as px

def main():
	st.title('Análise dos dados de Status')
	#st.subheader('Dados', divider='violet')

if __name__ == '__main__':
	main()
st.markdown('<div style="text-align: justify;">\t A seguir são apresentados 2 gráficos, os quais expõem a distribuição de pessoas do gênero feminino e masculino por status, os quais são: concluído, ativo e formando.</div>', unsafe_allow_html=True)
#st.subheader('Causas da Desigualdade de Gênero na Ciência:', divider='violet')
#st.markdown("")

conta_mas2 = pd.read_csv('conta_mas2.csv')
conta_fem2 = pd.read_csv('conta_fem2.csv')


conta_fem2_grouped = conta_fem2.groupby(['Ano/Período de ingresso', 'Status'])['Contagem Feminino'].sum().reset_index()
conta_mas2_grouped = conta_mas2.groupby(['Ano/Período de ingresso', 'Status'])['Contagem Masculino'].sum().reset_index()

fig = px.scatter(conta_fem2_grouped, x='Ano/Período de ingresso', y='Contagem Feminino', color='Status',
                 labels={'Contagem Feminino': 'Quantidade', 'Ano/Período de ingresso': 'Ano'},
                 title='Quantidade por Status e Ano - Feminino')

fig.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    font=dict(family='Arial', color='white'),
    #plot_bgcolor='white'
)

st.plotly_chart(fig)

###############################################

fig = px.scatter(conta_mas2_grouped, x='Ano/Período de ingresso', y='Contagem Masculino', color='Status',
                 labels={'Contagem Masculino': 'Quantidade', 'Ano/Período de ingresso': 'Ano'},
                 title='Quantidade por Status e Ano - Masculino')

fig.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    font=dict(family='Arial', color='white'),
    #plot_bgcolor='white'
)

st.plotly_chart(fig)

