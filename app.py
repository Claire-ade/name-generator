import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

st.set_page_config(page_title="Molécule 2D", layout="centered")
st.title("🧪 Visualisation 2D de molécules")

st.markdown("Entrez une structure **SMILES** pour afficher sa représentation 2D.")

smiles = st.text_input("Structure SMILES :", "CCO", key="smiles_input")

if smiles:
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            img = Draw.MolToImage(mol, size=(400, 400), kekulize=True, wedgeBonds=True)
            st.image(img, caption=f"Structure 2D de {smiles}")
        else:
            st.error("❌ Structure SMILES invalide. Veuillez réessayer.")
    except Exception as e:
        st.error(f"Erreur lors du rendu : {e}")
