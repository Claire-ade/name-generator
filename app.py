import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

st.title("Générateur de noms IUPAC")

smiles = st.text_input("Entrez une structure SMILES :", "CCO")

if smiles:
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        st.image(Draw.MolToImage(mol), caption="Structure moléculaire")
        st.write("Nom IUPAC approximatif :", Chem.MolToSmiles(mol))
    else:
        st.error("Structure invalide.")

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
