import streamlit as st
import functions

st.set_page_config(page_title="FeedBack", page_icon="icons/talking.png")
st.sidebar.header("Tu Opinion Es Importante..")
functions.not_menu()
st.title("Deja Algun :blue[Comentario...]")
st.write("""Tienes alguna sugerencia ? O tal vez quieres agregar algo no dudes en dejar tu mensaje..""")

st.divider()

with st.form(key="form_comments"):

    user_email = st.text_input("Cual es tu correo:", placeholder="Enter para validar..")
    functions.email_verfication(user_email)
    
    name = st.text_input("Cual es tu nombre:")
    where = st.text_input("De donde eres:")
    select = st.selectbox("Que tal te parecio esta pagina:", ("", "Super!", "Algo interesante!", "No informa mucho!", "Nada llamativa!"),
                            placeholder="Selecciona una respuesta..",)
    message = st.text_area("Comentarios:")
    message1 = f"Subject: New message from {user_email}\n\nFrom: {name}\nCountry: {where}\nCalification: {select}\nMessage: {message}"
    st.write(f'Tu mensaje tiene {len(message)} carateres.')

    button = st.form_submit_button("Enviar")
    if button:
        functions.send_form(message1)
        functions.send_comments(button)