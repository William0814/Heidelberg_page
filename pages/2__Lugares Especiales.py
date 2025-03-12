import streamlit as st

st.sidebar.header("Conoce Más")
st. title("Algunos Sitios :blue[Turisticos..]")
st.divider()

col1, col2 = st.columns([1.7, 1.5])
with col1:
    st.image("images/H3.jpg", caption="Castillo De Heidelberg.")

with col2:
    st.subheader("Castillo De Heildelberg", divider="blue")
    st.write("""*Esta emblemática ruina es una de las más famosas de Alemania.
             El castillo alberga el Museo Alemán de Farmacia y ofrece vistas panorámicas
             del valle y la ciudad. Anualmente, se celebran eventos como los Schlossfestspiele
            (festivales teatrales) y el Ball der Vampire (baile de los vampiros).*""")
    
st.divider()

col3, col4 = st.columns([1.5, 1.5])

with col3:
    st.subheader("Centro Historico (Altstadt)", divider="blue")
    st.write("""*Caracterizado por su arquitectura barroca, el casco antiguo es una extensa
             zona peatonal que alberga iglesias como la Heiliggeistkirche (Iglesia del Espíritu Santo),
             la Universidad de Heidelberg con su histórica biblioteca y la Studentenkarzer
             (cárcel de estudiantes). Además, cuenta con una variedad de tiendas, bares y restaurantes.*""")
    
with col4:
    st.image("images/H4.webp", caption="Centro (AltStadt)")

st.divider()

col5, col6 = st.columns([1.5, 1.5])
with col5:
    st.image("images/H5.jpg", caption="Universidad De Heidelberg.")

with col6:
    st.subheader("Universidad De Heidelberg.", divider="blue")
    st.write("""*Fundada en 1386, la Universidad de Heidelberg es la más antigua de Alemania y una de las
              más prestigiosas de Europa. Ha sido reconocida como Universidad de élite en Alemania y cuenta
              con una amplia oferta académica en diversas disciplinas. La universidad ha estado asociada con
              figuras prominentes como Georg Wilhelm Friedrich Hegel, Karl Jaspers y Hannah Arendt. Sus facultades
              de humanidades y ciencias sociales se encuentran en el casco antiguo, mientras que las de medicina
              y ciencias naturales están en el Campus Neuenheimer Feld.*""")
    
st.divider()

col7, col8 = st.columns([1.5, 1])
with col7:
    st.subheader("La Iglesia de San Pedro", divider="blue")
    st.write("""*La Iglesia de San Pedro es la iglesia más antigua de Heidelberg. Aunque no se dispone de
              documentación precisa sobre su fecha exacta de construcción, se presume que fue edificada a 
              finales del siglo XII, antes de la fundación oficial de la ciudad. Su primera mención en 
              registros históricos data de 1196, cuando se hace referencia a un sacerdote llamado Konrad 
              en Heidelberg.*""")
    
with col8:
    st.image("images/H6.jpg", caption="Iglesia de San Pedro.")