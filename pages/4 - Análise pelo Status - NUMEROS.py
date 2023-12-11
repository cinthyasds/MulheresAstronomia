import streamlit as st 
#from PIL import Image
import pandas as pd
import plotly.express as px

def main():
	st.title('Análise dos dados de Status')
	#st.subheader('Dados', divider='violet')

if __name__ == '__main__':
	main()

st.markdown('<div style="text-align: justify;">\t A seguir são apresentados 4 gráficos, que expõem a distribuição de pessoas do gênero feminino e masculino por status, os quais são: concluído, ativo e formando para a UFS e concluído, ativo e cancelada para a UFRJ.</div>', unsafe_allow_html=True)
#st.subheader('Causas da Desigualdade de Gênero na Ciência:', divider='violet')
#st.markdown("")

#UFS

conta_mas2 = pd.read_csv('C:/Users/usuario/Downloads/st-multi_app/conta_masufsNUMERO.csv')
conta_fem2 = pd.read_csv('C:/Users/usuario/Downloads/st-multi_app/conta_femufsNUMERO.csv')


conta_fem2_grouped = conta_fem2.groupby(['Ano/Período de ingresso', 'Status'])['Contagem_Feminino'].sum().reset_index()
conta_mas2_grouped = conta_mas2.groupby(['Ano/Período de ingresso', 'Status'])['Contagem_Masculino'].sum().reset_index()

fig = px.scatter(conta_fem2_grouped, x='Ano/Período de ingresso', y='Contagem_Feminino', color='Status',
                 labels={'Contagem Feminino': 'Quantidade', 'Ano/Período de ingresso': 'Ano'},
                 title='Quantidade por Status e Ano - Feminino (UFS)')

fig.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    font=dict(family='Arial', color='white'),
    #plot_bgcolor='white'
)

st.plotly_chart(fig)

#################################################################################

fig = px.scatter(conta_mas2_grouped, x='Ano/Período de ingresso', y='Contagem_Masculino', color='Status',
                 labels={'Contagem Masculino': 'Quantidade', 'Ano/Período de ingresso': 'Ano'},
                 title='Quantidade por Status e Ano - Masculino (UFS)')

fig.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    font=dict(family='Arial', color='white'),
    #plot_bgcolor='white'
)

st.plotly_chart(fig)

#UFRJ

nconta_masufrj = pd.read_csv('C:/Users/usuario/Downloads/st-multi_app/contagem_masrjNUMERO.csv')
nconta_femufrj = pd.read_csv('C:/Users/usuario/Downloads/st-multi_app/contagem_femrjNUMERO.csv')


nconta_femufrj_grouped = nconta_femufrj.groupby(['Ano/Período de ingresso', 'Status'])['Contagem_Feminino'].sum().reset_index()
nconta_masufrj_grouped = nconta_masufrj.groupby(['Ano/Período de ingresso', 'Status'])['Contagem_Masculino'].sum().reset_index()

fig = px.scatter(nconta_femufrj_grouped, x='Ano/Período de ingresso', y='Contagem_Feminino', color='Status',
                 labels={'Contagem Feminino': 'Quantidade', 'Ano/Período de ingresso': 'Ano'},
                 title='Quantidade por Status e Ano - Feminino (UFRJ)')

fig.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    font=dict(family='Arial', color='white'),
    #plot_bgcolor='white'
)

st.plotly_chart(fig)

###############################################

fig = px.scatter(nconta_masufrj_grouped, x='Ano/Período de ingresso', y='Contagem_Masculino', color='Status',
                 labels={'Contagem Masculino': 'Quantidade', 'Ano/Período de ingresso': 'Ano'},
                 title='Quantidade por Status e Ano - Masculino (UFRJ)')

fig.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    font=dict(family='Arial', color='white'),
    #plot_bgcolor='white'
)

st.plotly_chart(fig)



