FROM continuumio/miniconda3

# Copy environment file and create Conda environment
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate environment
SHELL ["conda", "run", "-n", "rdkit-env", "/bin/bash", "-c"]

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
