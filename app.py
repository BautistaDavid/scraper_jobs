import streamlit as st 
from scraper import funcion_scraper

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


local_css('style.css')
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


bienvenida = """
Bienvenido a la APP "Scraper de trabajos." . Esta APP es un pequeño ejercicio que 
implementa un scraper para realizar una búsqueda de cualquier término deseado en el
portal de empleo "El Empleo", además de eso logra filtrar los resultados por algún 
término en específico. La idea nació después de que una persona especial para mí 
se enfrentara al proceso de búsqueda de prácticas laborales, proceso el cual, por 
experiencia propia sé que puede llegar a ser frustrante, de modo que la finalidad 
de la herramienta es distraerse, explorando de otra manera información de un portal
de empleo. 
"""

st.title('Scraper de Trabajos. 📌')

st.text(bienvenida)

icon("search")
selected = st.text_input("Término de búsqueda:",'Escribe tu búsqueda acá. Ej: "Practicante analítica.".')
filter = st.text_input("Término de filtrado:",'Escriba el término por el cual desea filtrar. Ej: "python". Después presiona "Ok"')
button_clicked = st.button("Ok")




if button_clicked:
    st.dataframe(funcion_scraper(selected,filter))
else:
    None
