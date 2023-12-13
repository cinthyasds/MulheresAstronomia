import streamlit as st 
from PIL import Image

st.set_page_config(
    page_title="Estrelas brasileiras",
    page_icon=":rocket:",
    layout="wide",
)

background = Image.open("logo_ufs.png")

col1, col2 = st.columns([2, 10])

col1.image(background, width=55)

col2.markdown("<h2 style='font-size: 35px;'>Universidade Federal de Sergipe</h2>", unsafe_allow_html=True)


def main():
	st.title("A evolução da participação feminina na astronomia brasileira")
	st.subheader('Apresentação', divider='violet')

if __name__ == '__main__':
	main()


st.markdown('<div style="text-align: justify;">\tBem-vind@ ao nosso site do projeto que busca contribuir para o avanço da participação feminina na astronomia e fornecer subsídios para a implementação de políticas de igualdade de gênero na área. Aqui, você encontrará informações sobre como a participação feminina se comportou entre os anos 2017 e 2023 na Universidade Federal de Sergipe e na Universidade Federal do Rio de Janeiro. O projeto foi desenvolvido por Cinthya Cerqueira Santana dos Santos sob a orientação do professor Dr. Diogo Martins Souto com o apoio financeiro do Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq), por meio do Edital Temático N.º 02/2023 COPES/POSGRAP/UFS - Representatividade Feminina no Ambiente Acadêmico. </div>', unsafe_allow_html=True)
st.markdown("")
st.subheader('A Presença Feminina nas Ciências STEM e o Caso Brasileiro', divider='violet')
st.markdown('<div style="text-align: justify;">A participação das mulheres nas áreas de STEM (Ciência, Tecnologia, Engenharia e Matemática) é um tema de grande relevância global, e o Brasil não fica de fora dessa discussão. Embora o Brasil apresente uma proporção relativamente alta de mulheres atuando em STEM, superando a média global (conforme um relatório da UNESCO em 2021), ainda persistem desigualdades de gênero na distribuição dessas áreas. Notadamente, as mulheres continuam sub-representadas em Engenharia e Matemática.</div>', unsafe_allow_html=True)
st.markdown("")
st.markdown('<div style="text-align: justify;">No entanto, é animador observar que, nos últimos anos, temos assistido a um aumento na participação feminina em STEM no Brasil, sinalizando um progresso positivo em direção à igualdade de gênero nessas esferas. Entretanto, quando falamos especificamente de Astronomia, observamos que a presença feminina ainda é limitada, especialmente em cargos de liderança administrativa e em posições de destaque em universidades federais ou centros de pesquisa no país. Não obstante, é importante ressaltar que muitas mulheres brasileiras têm feito contribuições notáveis para o campo da Astronomia. Elas enfrentam desafios, mas, com dedicação e paixão, estão conquistando seu espaço e deixando uma marca significativa nessa fascinante área científica.</div>', unsafe_allow_html=True)
st.markdown("")
#st.markdown('<div style="text-align: justify;"></div>', unsafe_allow_html=True
            
            
#image = Image.open('fig1.jpg')
#st.image(image, caption=None, width= 400, use_column_width=False, clamp=False, channels="RGB", output_format="auto")


background = Image.open("fig1.jpg")
col1, col2, col3 = st.columns([0.9, 5, 0.2])
col2.image(background, width=500)

st.subheader('Dados', divider='violet')
st.markdown('<div style="text-align: justify;">Nossa iniciativa tem como objetivo realizar um estudo temporal abrangente sobre a crescente participação das mulheres na comunidade astronômica brasileira. O foco central deste projeto é analisar a taxa de envolvimento feminino em todas as etapas, desde alunas de graduação até professoras universitárias. Acreditamos que essa análise proporcionará insights valiosos sobre o progresso e os desafios enfrentados pelas mulheres na área da astronomia no Brasil. Para essa análise foram necessários os dados a seguir: </div>', unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.markdown('**Dados gerais:**')
st.write('* Divisões entre gênero: masculino, feminimo, e se houver, dados não binários.')
st.write('* Status: Indicando o estado da matrícula do aluno (pode incluir opções como ATIVO, EXCLUÍDO, CANCELADO ou CONCLUÍDO).')
st.write('* % Integralizado: Porcentagem do curso integralizado pelo aluno até o momento.')
st.write('* Ano/Período da última matrícula válida: Informação sobre o ano e período da última matrícula efetuada pelo aluno.')
st.write('* Ano/Período de ingresso: Ano e período em que o aluno ingressou no curso.')

st.markdown("")
st.markdown('**Dados de disciplinas:**')
st.write('* Divisões entre gênero: masculino, feminimo, e se houver, dados não binários.')
st.write('* Código da disciplina.')
st.write('* Turma: Informação sobre a turma em que o aluno cursou a disciplina.')
st.write('* Ano: O ano em que a disciplina foi cursada pelo aluno.')
st.write('* Situação: Indicação se o aluno foi APROVADO ou REPROVADO na disciplina.')
st.write('* Período: período em que a disciplina foi cursada.')















