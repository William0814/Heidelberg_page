import streamlit as st
import time
import re
import smtplib, ssl
import os


def tema(self):
    if self == "Infraestructura":
         st.info("""Heidelberg está estratégicamente ubicada en el corazón de Europa,
                  dentro de la región metropolitana del Rin-Neckar, con excelentes 
                  conexiones por carretera y ferrocarril. La ciudad se beneficia de una
                  densa red de tranvías y autobuses operados por Rhein-Neckar-Verkehr GmbH (rnv),
                  con alrededor de 160.000 pasajeros diarios en 2018. Recientemente, se inauguró
                  el tranvía más largo del mundo, de 58,61 metros de longitud y capacidad para
                  368 pasajeros, que conecta Mannheim, Ludwigshafen y Heidelberg. HUFFINGTONPOST.ES
                  Además, Heidelberg promueve el uso de la bicicleta mediante la creación de nuevas
                  rutas, como la Gneisenaubrücke, que conecta Bahnstadt con Bergheim, y una vía para
                  ciclistas y peatones sobre el río Neckar. El nuevo distrito de Bahnstadt es la mayor
                  urbanización de casas pasivas del mundo, diseñada para albergar a 6.800 residentes y c
                  rear 6.000 empleos. Las áreas de conversión de la antigua base del ejército estadounidense,
                  que abarcan alrededor de 200 hectáreas, ofrecen oportunidades para el desarrollo de viviendas
                  y espacios comerciales.""")
        
    elif self == 'Economía':
            st.info("""Heidelberg es un destacado centro de servicios y ciencia
                     en la región del Rin-Neckar. En 2013, el 83,8% de la población 
                    activa trabajaba en el sector servicios, mientras que el 16,1% se 
                    dedicaba a la industria. En 2016, la ciudad registró un Producto 
                    Interno Bruto (PIB) de 8.391 millones de euros, con un PIB per 
                    cápita de 53.079 €, superando la media regional y nacional. La tasa
                     de desempleo en diciembre de 2018 fue del 3,6%, una de las más bajas
                     entre las grandes ciudades alemanas. El mayor empleador es la Universidad
                     de Heidelberg y su hospital universitario, que ofrecen más de 15.000 puestos
                     de trabajo. Empresas internacionales como ABB Stotz-Kontakt, Heidelberger Druckmaschinen,
                     Heidelberg Materials, Henkel-Teroson, Lamy y SAP tienen presencia en la ciudad. El turismo
                     también es significativo; en 2017, Heidelberg registró 1,44 millones de pernoctaciones comerciales.""")
            
    elif self == 'Patrimonio Cultural':
          st.info("""Heidelberg es reconocida por su riqueza cultural y su bien conservado casco antiguo.
                   El Castillo de Heidelberg es una de las ruinas más famosas de Alemania y alberga el Museo
                   Alemán de Farmacia. La ciudad celebra numerosos eventos culturales, como el Festival de Primavera
                   (Heidelberger Frühling) dedicado a la música clásica, festivales de jazz en otoño y mercados
                   navideños en diciembre. Heidelberg también fue un centro del Romanticismo alemán, atrayendo a poetas
                   y filósofos que encontraron inspiración en sus paisajes y ambiente intelectual.""")
          
    elif self == 'División Administrativa':
          st.info("""Cada distrito contribuye a la diversidad y riqueza cultural de Heidelberg, ofreciendo una
                   variedad de experiencias y ambientes para residentes y visitantes. 
                  Espero que esta información te proporcione una visión detallada de 
                  Heidelberg en cuanto a su economía, infraestructura, patrimonio cultural
                   y división administrativa.""")


# Function for disguise the buttons from Streamlit server interface.       
def not_menu():
      hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
      st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Function for send messages in Feedback page  
def send_comments(self):
      if self:
            with st.spinner("Enviando tu mensaje.."):
                  time.sleep(5)
                  st.info(f"Gracias Por tus comentarios :smile:")


 # Function for checkin the user email if is correct or no.     
def email_verfication(email):
      verification = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
      if re.match(verification, email):
            st.success(f"Email valido!!")
      else:
            st.error(f"Por favor ingrese un Email valido..")


# Function for send email of the form in the Feedback page.
def send_form(message):
    host = "smtp.gmail.com"
    port = 465
    username = "correo.aplicaciones.ardit@gmail.com"
    passwor = "cyjw awse agna egda"
    receiver = "correo.aplicaciones.ardit@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, passwor)
        server.sendmail(username, receiver, message)

