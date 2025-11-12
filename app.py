import streamlit as st
import py3Dmol

st.title("Visualisation 3D de molécules")

smiles = st.text_input("Entrez une structure SMILES :", "CCO")  # Éthanol

if smiles:
    view = py3Dmol.view(width=400, height=400)
    view.addModel(smiles, "sdf")
    view.setStyle({"stick": {}})
    view.zoomTo()
    view.show()
