import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Home", page_icon="")


st.sidebar.header("What is Heidelberg?")
st. title("Heidelberg City...")

st.image("images/H1.jpg")

st.write("""Heidelberg es una ciudad situada en el valle del río Neckar, 
         en el noroeste de Baden-Wurtemberg, Alemania. Es reconocida por su
         centro histórico bien conservado y por albergar la universidad más 
         antigua del país, lo que la convierte en un importante centro cultural y turístico.""")

st.write("Here's our first attempt at using data to create a table:")

if st.checkbox('Mostrar tabla tecnica'):
    st.table(pd.DataFrame({
        'Descripción': ["Habitantes", "Diametro", "Altitud", "Clima"],
        'Detalle': [162.273, '108.83 Km2', '114 mts/Nivel del Mar', '11°C, Precipitaciones de 800 mm']
}))

df = pd.DataFrame({
    'first column': ["Infraestructura", "Economía", "Patrimonio cultural", "División administrativa"],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Seleccione tema de su interes',
     df['first column'])

if option == "Infraestructura":
    st.write("""La ciudad cuenta con una red de transporte público eficiente, 
             incluyendo tranvías y autobuses, y está bien conectada por carretera
              y ferrocarril con otras ciudades alemanas""")
    
elif option == 'Economía':
    st.write("""Heidelberg es un centro económico en la región del Rin-Neckar,
              con sectores destacados en la investigación, la educación superior,
              la biotecnología y el turismo.""")



    

