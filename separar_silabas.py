import spacy
import streamlit as st
import pandas as pd
import pyphen

# st.set_page_config(page_title="Análise Gramatical e Separação Silábica em Português", page_icon=":book:", layout="wide")
try:
    nlp = spacy.load('pt_core_news_lg')
except OSError:
    spacy.cli.download("pt_core_news_lg")
    nlp = spacy.load('pt_core_news_lg')

def separar_silabas_personalizado(palavra):
    casos_especiais = {
        "uruguai": "u-ru-guai",
        "arara": "a-ra-ra",
        "ônibus": "ô-ni-bus"
    }
    
    if palavra.lower() in casos_especiais:
        return casos_especiais[palavra.lower()]
    
    dic = pyphen.Pyphen(lang='pt-BR')
    return dic.inserted(palavra)

def formatar_classificacao_personalizado(palavra, tag):
    casos_especiais = {
        # "arara": "artigo"
    }
    return casos_especiais.get(palavra.lower(), tag)

def formatar_descricao(descricao):
    traducoes = {
        "NOUN": "substantivo",
        "VERB": "verbo",
        "ADJ": "adjetivo",
        "ADV": "advérbio",
        "PROPN": "substantivo próprio",
        "DET": "artigo",
        "CCONJ": "conjunção coordenativa",
        "AUX": "verbo auxiliar",
        "ADP": "preposição",
        "NUM": "numeral",
        "DEP": "dependência",
    }
    return traducoes.get(descricao, descricao)


nlp = spacy.load("pt_core_news_lg")

# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title("Análise Gramatical e Separação Silábica em Português (MarceloFullstack)")
palavra = st.text_input("Digite uma palavra em português:")

if palavra:
    doc = nlp(palavra)
    
    data = []
    for token in doc:
        silabas = separar_silabas_personalizado(token.text)
        silabas_lista = silabas.split("-")
        tag = formatar_descricao(token.pos_)
        tag_personalizado = formatar_classificacao_personalizado(token.text, tag)
        data.append([token.text, tag_personalizado, silabas])

    df = pd.DataFrame(data, columns=["Palavra", "Classe Gramatical", "Separação Silábica"])
    st.write(df)
