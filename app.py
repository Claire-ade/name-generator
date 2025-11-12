import streamlit as st
import requests

st.title("Structure moléculaire à partir de SMILES")

smiles = st.text_input("Entrez une structure SMILES :", "CCO", key="smiles_input_2D")  # Éthanol

if smiles:
    # Utilise l'API de NCI pour générer une image PNG
    url = f"https://cactus.nci.nih.gov/chemical/structure/{smiles}/image"
    st.image(url, caption=f"Structure de {smiles}")

import streamlit as st

st.title("Visualisation 3D de molécules")

smiles = st.text_input("Entrez une structure SMILES :", "CCO", key="smiles_input_3D")

if smiles:
    html_code = f"""
    <div id="viewer" style="width: 500px; height: 400px;"></div>
    <script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
    <script>
      let element = document.getElementById("viewer");
      let config = {{ backgroundColor: "white" }};
      let viewer = $3Dmol.createViewer(element, config);
      $3Dmol.download("sdf:{smiles}", viewer, {{}}, function() {{
        viewer.setStyle({{}}, {{stick:{{}}}});
        viewer.zoomTo();
        viewer.render();
      }});
    </script>
    """
    st.components.v1.html(html_code, height=400, width=500)
