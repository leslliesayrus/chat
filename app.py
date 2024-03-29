import streamlit as st

def page1():
    st.title('Página 1')
    st.write('Conteúdo da página 1')

def page2():
    st.title('Página 2')
    st.write('Conteúdo da página 2')

# Menu de seleção para escolher a página
page = st.sidebar.radio("Escolha uma página:", ('Página 1', 'Página 2'))

# Mostra a página selecionada
if page == 'Página 1':
    page1()
elif page == 'Página 2':
    page2()
