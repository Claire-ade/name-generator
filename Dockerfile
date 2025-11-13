FROM continuumio/miniconda3

# Create environment
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate environment
SHELL ["conda", "run", "-n", "rdkit-env", "/bin/bash", "-c"]

# Install Streamlit as entry point
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
