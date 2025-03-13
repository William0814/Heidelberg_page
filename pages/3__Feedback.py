import streamlit as st
import functions

st.set_page_config(page_title="FeedBack", page_icon="icons/talking.png")
st.sidebar.header("Tu Opinion Es Importante..")
functions.not_menu()
st.title("Deja Algun :blue[Comentario...]")
st.write("""Tienes alguna sugerencia ? O tal vez quieres agregar algo no dudes en dejar tu mensaje..""")

st.divider()

name = st.text_input(label="Cual es tu nombre:")
where = st.text_input("De donde eres:")
select = st.selectbox("Que tal te parecio esta pagina:", ("Me gusto", "Me da igual", "No me gusto"),
                       index=None, placeholder="Selecciona una respuesta..",)
menssage = st.text_area("Comentarios:")
st.write(f'Tu mensaje tiene {len(menssage)} carateres.')


send = st.button("Enviar")
functions.send_comments(send)