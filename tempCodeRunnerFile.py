# Define o título do aplicativo
# st.title("Análise Sintática e Morfológica em Português")

# # Cria um campo de texto para entrada da palavra
# palavra = st.text_input("Digite uma palavra em português:")

# # Se a palavra foi digitada
# if palavra:

#     # Processa a palavra com o spaCy
#     doc = nlp(palavra)

#     # Exibe a análise sintática e morfológica completa
#     for token in doc:
#         st.write(f"<u>{token.text}</u><sub>{spacy.explain(token.pos_)} ({spacy.explain(token.tag_)})</sub>")