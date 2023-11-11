import streamlit as st 
import plotly.express as px
import pandas as pd

#from PIL import Image

def main():
	st.title('Situações de Andamento no Curso de Graduação em Astronomia (UFS)')
	#st.subheader('Dados', divider='violet')

if __name__ == '__main__':
	main()

st.markdown('<div style="text-align: justify;">\tNo âmbito do curso de graduação em Astronomia, os estudantes podem se encontrar em várias situações de andamento, cada uma refletindo um estágio diferente em sua jornada acadêmica. Essas situações, que abrangem desde "APROVADO" até "REPROVADO POR FALTAS," são indicativos essenciais do progresso dos estudantes e das eventuais barreiras que podem enfrentar em seu caminho para a conclusão do curso. Assim, para cada ano, foi feito um gráfico de barras, o qual mostra a comparação de cada situação para o gênero feminino e masculino. </div>', unsafe_allow_html=True)
#st.subheader('', divider='violet')
st.markdown("")

# Carregue seus DataFrames para cada ano
ndf17 = pd.read_csv('ndf17.csv', encoding='utf-8')
ndf18 = pd.read_csv('ndf18.csv', encoding='utf-8')
ndf19 = pd.read_csv('ndf19.csv', encoding='utf-8')
ndf20 = pd.read_csv('ndf20.csv', encoding='utf-8')
ndf21 = pd.read_csv('ndf21.csv', encoding='utf-8')
ndf22 = pd.read_csv('ndf22.csv', encoding='utf-8')
ndf23 = pd.read_csv('ndf23.csv', encoding='utf-8')


# Crie um dicionário para mapear anos para DataFrames
dataframes = {
    '2017': ndf17,
    '2018': ndf18,
    '2019': ndf19,
    '2020': ndf20,
    '2021': ndf21,
    '2022': ndf22,
    '2023': ndf23
}


# Função para criar e mostrar gráfico
def create_and_show_bar_chart(data, year):
    data['TOTAL'] = data['FEMININO'] + data['MASCULINO']
    data['FEMININO_PCT'] = (data['FEMININO'] / data['TOTAL']) * 100
    data['MASCULINO_PCT'] = (data['MASCULINO'] / data['TOTAL']) * 100

    fig = px.bar(data, x='SITUACAO', y=['FEMININO_PCT', 'MASCULINO_PCT'], title=f'Distribuição de Situação por Gênero ({year})',
                 labels={'value': 'Porcentagem', 'variable': 'Gênero'}, color_discrete_sequence=['mediumpurple', 'gray'],
                 width=800, height=500
                )

    fig.update_layout(
        xaxis=dict(tickangle=-45, tickmode='array'),
        legend_title='Porcentagem por gênero',
        font=dict(family='Arial', color='white'),
        barmode='group',
        #plot_bgcolor='white'
    )

    for idx, row in data.iterrows():
        fig.add_annotation(
            x=row['SITUACAO'],
            y=row['FEMININO_PCT'],
            text=f"{row['FEMININO_PCT']:.0f}%",
            showarrow=False,
            font=dict(size=12, color='white'),
            xanchor='center',
            yanchor='bottom',
            textangle=-45
        )
        fig.add_annotation(
            x=row['SITUACAO'],
            y=row['MASCULINO_PCT'],
            text=f"{row['MASCULINO_PCT']:.0f}%",
            showarrow=False,
            font=dict(size=12, color='white'),
            xanchor='center',
            yanchor='bottom',
            textangle=-45
        )

    return fig



# Dropdown para selecionar o ano
years = list(dataframes.keys())
selected_year = st.selectbox("Selecione o ano:", years)

# Chame a função para criar e mostrar o gráfico com base no ano selecionado
if selected_year == '2017':
    st.plotly_chart(create_and_show_bar_chart(ndf17, selected_year))
elif selected_year == '2018':
    st.plotly_chart(create_and_show_bar_chart(ndf18, selected_year))
elif selected_year == '2019':
    st.plotly_chart(create_and_show_bar_chart(ndf19, selected_year))
elif selected_year == '2020':
    st.plotly_chart(create_and_show_bar_chart(ndf20, selected_year))
elif selected_year == '2021':
    st.plotly_chart(create_and_show_bar_chart(ndf21, selected_year))
elif selected_year == '2022':
    st.plotly_chart(create_and_show_bar_chart(ndf22, selected_year))
elif selected_year == '2023':
    st.plotly_chart(create_and_show_bar_chart(ndf23, selected_year))



