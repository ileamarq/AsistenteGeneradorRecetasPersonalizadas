import streamlit as st
import requests
import os

st.title("Asistente generador de recetas personalizadas")
# Campo de texto para ingresar ingredientes
ingredientes = st.text_area("Ingresa la lista de ingredientes (separados por comas)")

# Input de selección múltiple para la categoría de receta
categorias = ["Aperitivo", "Ensalada", "Plato principal"]
categoria_seleccionada = st.selectbox("Selecciona la categoría de la receta:", categorias)

# Guardar los valores en variables respectivas
ingredientes_lista = ingredientes.split(",") if ingredientes else []
categoria_elegida = categoria_seleccionada

# Mostrar los valores seleccionados
st.write(f"Ingredientes ingresados: {ingredientes_lista}")
st.write(f"Categoría seleccionada: {categoria_elegida}")

# Datos para la solicitud
base_url = "https://api.dify.ai/v1"
path = "/completion-messages"
my_secret = os.environ['TU_API_KEY']


data = {
    "text": text,
    "categoria": categoria
}


headers = {
    "Authorization": f"Bearer {my_secret}",
    "Content-Type": "application/json"
}

# Realizar la solicitud POST
url_completa = base_url + path
response = requests.post(url_completa, json=data, headers=headers)

# Imprimir la respuesta
print(response.text)

