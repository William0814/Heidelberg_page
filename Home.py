import streamlit as st
import pandas as pd
import numpy as np
import functions


st.set_page_config(page_title="Home")

st.sidebar.header("Que es Heidelberg ?")
st.sidebar.title("Menu")

st. title("Ciudad de :blue[Heidelberg...]")
st.divider()

col1, col2 = st.columns([1.5, 1.5])
with col1:
    st.image("images/H2.jpg", caption="Heidelberg city")

with col2:
    st.write("""*Heidelberg es una ciudad situada en el valle del río Neckar, 
         en el noroeste de Baden-Wurtemberg, Alemania. Es reconocida por su
         centro histórico bien conservado y por albergar la universidad más 
         antigua del país, lo que la convierte en un importante centro cultural y turístico.*""")

if st.checkbox('Mostrar tabla tecnica'):
    df = pd.DataFrame({
        'Descripción': ["Habitantes", "Diametro", "Altitud", "Clima"],
        'Detalle': [162.273, '108.83 Km2', '114 mts/Nivel del Mar', '11°C, Precipitaciones de 800 mm']})
    st.write(df)

st.divider()


df = pd.DataFrame({
    'first column': ["", "Infraestructura", "Economía", "Patrimonio Cultural", "División Administrativa"],
    'second column': [10, 20, 30, 40, 50]
    })

option = st.selectbox(
    'Seleccione tema de su interes',
     df['first column'])

functions.tema(option)

st.divider()

st.link_button(label="Mapa", url="https://www.google.de/maps/place/69123+Heidelberg/@49.4178422,8.5376347,12z/data=!3m1!4b1!4m6!3m5!1s0x4797c6fbb04d42bd:0x1c1ffd3ff5a4c640!8m2!3d49.4160136!4d8.6171786!16s%2Fg%2F1vlz99jd?entry=ttu&g_ep=EgoyMDI1MDMxMC4wIKXMDSoASAFQAw%3D%3D")










