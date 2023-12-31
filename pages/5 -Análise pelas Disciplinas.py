import streamlit as st 
import plotly.express as px
import pandas as pd

st.title('Participação nas disciplinas')
st.markdown('<div style="text-align: justify;">\t Os gráficos abaixo trazem a particpação em algumas disciplinas do curso (disciplinas de períodos iniciais e da própria astrofísica.)</div>', unsafe_allow_html=True)
st.markdown('')
st.markdown('**Os gráficos estão divididos por situação:**')
st.write('* Aprovado: Passou com sucesso.')
st.write('* Reprovado: Não atingiu o desempenho necessário.')
st.write('* Rep. Media/Faltas: Necessita de melhoria em médias ou frequência.')
st.write('* Trancado: Disciplina foi trancada (pausada) no determinado período.')
st.write('* Desistência: Abandonou definitivamente a disciplina.')
st.write('* Trancado: Matrícula temporariamente pausada.')
st.write('* Formando: Próximo da formatura.')
st.markdown('<div style="text-align: justify;">\tPara a UFRJ, só estão disponíveis 2 situações: Aprovado e Reprovado, dessa forma a análise de quantidades de pessoas do gênero feminino e masculino nas disciplinas torna-se mais incerta, uma vez que não há quantidades de trancamento e desistência informados.</div>', unsafe_allow_html=True)
st.markdown('')

#UFS

st.subheader('Disciplinas UFS')

ntabela_ok = pd.read_csv("nntabela_ok.csv")

disciplinas_disponiveis = ['PROGRAMACAO IMPERATIVA','FISICA 1','FISICA 2','FISICA 3','FISICA E SOCIEDADE','FISICA MATEMATICA 1','FISICA MATEMATICA 2','LABORATORIO DE FISICA 1','PERSPECTIVAS EM ASTROFISICA','INTRODUCAO A ASTRONOMIA E ASTROFISICA','SISTEMAS PLANETARIOS','METODOS EM ASTROFISICA OBSERVACIONAL','ASTROFISICA ESTELAR','LABORATORIO DE ASTRONOMIA E ASTROFISICA','ASTROFISICA GALACTICA','ASTROFISICA EXTRAGALACTICA','INTRODUCAO A COSMOLOGIA','CALCULO NUMERICO','VETORES E GEOMETRIA ANALITICA','CALCULO A','CALCULO B','CALCULO C','CALCULO D','EQUACOES DIFERENCIAIS I','QUIMICA I']

situacoes_disponiveis = ['APROVADO', 'REPROVADO', 'REP. MEDIA/FALTAS', 'TRANCADO', 'DESISTENCIA']


selected_disciplina = st.selectbox('Selecione a disciplina:', disciplinas_disponiveis)

selected_situacao = st.selectbox('Selecione a situação:', situacoes_disponiveis)


def generate_chart(disciplina, situacao):
    
    filtro = (ntabela_ok['codigo'] == disciplina) & (ntabela_ok['situacao'] == situacao)
    dados_filtrados = ntabela_ok[filtro].copy()

    dados_filtrados['total'] = dados_filtrados['qtd_feminino'] + dados_filtrados['qtd_masculino']

    dados_filtrados['porcentagem_feminino'] = (dados_filtrados['qtd_feminino'] / dados_filtrados['total']) * 100
    dados_filtrados['porcentagem_masculino'] = (dados_filtrados['qtd_masculino'] / dados_filtrados['total']) * 100

    fig = px.line(
        dados_filtrados,
        x='ano',
        y=['porcentagem_feminino', 'porcentagem_masculino'],
        labels={
            'porcentagem_feminino': 'Porcentagem Feminino',
            'porcentagem_masculino': 'Porcentagem Masculino',
        },
        title=f'Evolução de {situacao} na disciplina {disciplina}',
        markers=True,
    )

    fig.update_layout(
        #plot_bgcolor='white',
        font=dict(family='Arial', color='white'),
        legend=dict(title_text='Gênero'),
        yaxis_title='Porcentagem (%)'
    )

    return fig

st.plotly_chart(generate_chart(selected_disciplina, selected_situacao))

#UFRJ

st.subheader('Disciplinas UFRJ')

rjtabela_ok = pd.read_csv("ufrjtabela_ok.csv")

disciplinas_disponiveis = ['FISICA EXPERIMENTAL I','FISICA I','COMPUTACAO I','CALCULO DIFERENCIAL E INTEGRAL I','INTRODUCAO A ASTRONOMIA','FISICA EXPERIMENTAL II','FISICA II','CALCULO DIFERENCIAL E INTEGRAL II','ALGEBRA LINEAR II','ASTRONOMIA ESFERICA','FISICA III','FISICA EXPERIMENTAL III','CALCULO DIFERENCIAL E INTEGRAL III','INTRODUCAO A ESTATISTICA ','LABORATORIO DE ASTRONOMIA','METODOS COMPUTACIONAIS EM ASTRONOMIA ']

situacoes_disponiveis = ['APROVADO', 'REPROVADO']


selected_disciplina = st.selectbox('Selecione a disciplina:', disciplinas_disponiveis)

selected_situacao = st.selectbox('Selecione a situação:', situacoes_disponiveis)

def generate_chart(disciplina, situacao):
    
    filtro = (rjtabela_ok['codigo'] == disciplina) & (rjtabela_ok['situacao'] == situacao)
    dados_filtrados = rjtabela_ok[filtro].copy()

    dados_filtrados['total'] = dados_filtrados['qtd_feminino'] + dados_filtrados['qtd_masculino']

    dados_filtrados['porcentagem_feminino'] = (dados_filtrados['qtd_feminino'] / dados_filtrados['total']) * 100
    dados_filtrados['porcentagem_masculino'] = (dados_filtrados['qtd_masculino'] / dados_filtrados['total']) * 100

    fig = px.line(
        dados_filtrados,
        x='ano',
        y=['porcentagem_feminino', 'porcentagem_masculino'],
        labels={
            'porcentagem_feminino': 'Porcentagem Feminino',
            'porcentagem_masculino': 'Porcentagem Masculino',
        },
        title=f'Evolução de {situacao} na disciplina {disciplina}',
        markers=True,
    )

    fig.update_layout(
        #plot_bgcolor='white',
        font=dict(family='Arial', color='white'),
        legend=dict(title_text='Gênero'),
        yaxis_title='Porcentagem (%)'
    )

    return fig

st.plotly_chart(generate_chart(selected_disciplina, selected_situacao))

