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

