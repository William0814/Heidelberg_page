import streamlit as st
import functions


st.set_page_config(page_title="Historia", page_icon="icons/parchment.png")
functions.not_menu()
st.sidebar.header("Historia que deberias conocer..")

st.title("Origen de :blue[Heidelber..]")

st.write(""" Aunque la primera mención oficial de Heidelberg data de 1196,
            la zona estuvo habitada desde tiempos de los celtas y romanos. 
            En el siglo XIII, se construyó el castillo de Heidelberg, y la 
            ciudad se desarrolló como residencia de los condes palatinos del
            Rin, convirtiéndose en la capital del Electorado del Palatinado
            durante unos 500 años. En 1386, se fundó la Universidad de Heidelberg,
            la más antigua de Alemania. DE.WIKIPEDIA.ORG""")

st.subheader("Guerras y destrucción", divider="blue")

st.write("""Durante la Guerra de Sucesión del Palatinado (1688-1697), Heidelberg
            sufrió dos ocupaciones y destrucciones por parte de las tropas francesas
            bajo el mando del general Ezéchiel de Mélac. En 1693, la ciudad fue incendiada
            y el castillo quedó en ruinas. DE.WIKIPEDIA.ORG""")

st.subheader("Reconstrucción y cambios administrativos", divider="blue")

st.write("""Tras su destrucción, Heidelberg fue reconstruida en estilo barroco sobre su trazado
            medieval. En 1720, la residencia de los príncipes electores se trasladó a Mannheim,
            y en 1803, la ciudad pasó a formar parte de Baden. DE.WIKIPEDIA.ORG""")

st.subheader("Siglos XIX y XX", divider="blue")

st.write("""En el siglo XIX, Heidelberg se convirtió en un centro del Romanticismo alemán,
            atrayendo a poetas y pensadores que le dieron el sobrenombre de "ciudad del romanticismo".
            La ciudad se expandió mediante anexiones y proyectos de construcción, y durante la Segunda 
            Guerra Mundial, permaneció en gran medida intacta. Después de la guerra, Heidelberg albergó 
            el cuartel general de las fuerzas terrestres estadounidenses en Europa hasta 2013.""")

