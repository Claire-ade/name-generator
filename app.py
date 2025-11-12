import streamlit as st
import py3Dmol

st.title("Visualisation 3D de molécules")

smiles = st.text_input("Entrez une structure SMILES :", "CCO")  # Éthanol

if smiles:
    mol_view = py3Dmol.view(width=400, height=400)
    mol_view.addModel(smiles, "sdf")
    mol_view.setStyle({"stick": {}})
    mol_view.zoomTo()
    html = mol_view._make_html()
    st.components.v1.html(html, height=400, width=400)
