import streamlit as st
import requests

st.title("Structure moléculaire à partir de SMILES")

smiles = st.text_input("Entrez une structure SMILES :", "CCO")  # Éthanol

if smiles:
    # Utilise l'API de NCI pour générer une image PNG
    url = f"https://cactus.nci.nih.gov/chemical/structure/{smiles}/image"
    st.image(url, caption=f"Structure de {smiles}")

import streamlit as st
import py3Dmol

st.title("Visualisation 3D de molécules")

smiles = st.text_input("Entrez une structure SMILES :", "CCO")  # Éthanol

if smiles:
    try:
        view = py3Dmol.view(width=500, height=400)
        view.addModel(smiles, "sdf")
        view.setStyle({"stick": {}})
        view.zoomTo()
        html = view._make_html()
        st.components.v1.html(html, height=400, width=500)
    except Exception as e:
        st.error(f"Erreur lors de l'affichage : {e}")
