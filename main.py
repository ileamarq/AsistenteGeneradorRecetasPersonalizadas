import streamlit as st
import requests
import os

st.title("Asistente generador de recetas personalizadas")
# Campo de texto para ingresar ingredientes
text = st.text_area("Ingresa la lista de ingredientes (separados por comas)")

# Input de selección múltiple para la categoría de receta
categoria = ["Aperitivo", "Ensalada", "Plato principal"]
categoria_seleccionada = st.selectbox("Selecciona la categoría de las recetas:", categoria)

# Datos para la solicitud
base_url = "https://api.dify.ai/v1"
path = "/completion-messages"
my_secret = os.environ['DIFY_APP_KEY']

headers = {
    "Authorization": f"Bearer {my_secret}",
    "Content-Type": "application/json"
}

data = {
    "inputs": {
     "text": text,
     "categoria": categoria_seleccionada 
   },

"response_mode": "blocking",
"user": "Buscadorrecetas"
}

# Realizar la solicitud POST
url_completa = base_url + path
if st.button('Consultar'):
  response = requests.post(url_completa, json=data, headers=headers)
  
  if response.status_code == 200:
   st.success("Recetas generadas exitosamente")
   
   result = response.json()
  # Imprimir la respuesta
   st.markdown("### Aqui tienes tus tres recetas:")
   st.markdown(result["answer"])
  else:
   st.error("Error al generar la receta")
  
