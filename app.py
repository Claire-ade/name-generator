import streamlit as st
import requests

st.title("Structure moléculaire à partir de SMILES")

smiles = st.text_input("Entrez une structure SMILES :", "CCO")  # Éthanol

if smiles:
    # Utilise l'API de NCI pour générer une image PNG
    url = f"https://cactus.nci.nih.gov/chemical/structure/{smiles}/image"
    st.image(url, caption=f"Structure de {smiles}")
