import streamlit as st
import pandas as pd

# Tytuł aplikacji
st.title("Most valuable data application")

# Pole do załadowania pliku
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xls", "xlsx", "json", "parquet"])

def load_file(file, file_type):
    """Funkcja do ładowania pliku do DataFrame w zależności od formatu"""
    if file_type == "csv":
        return pd.read_csv(file)
    elif file_type in ["xls", "xlsx"]:
        return pd.read_excel(file)
    elif file_type == "json":
        return pd.read_json(file)
    elif file_type == "parquet":
        return pd.read_parquet(file)
    else:
        raise ValueError("Unsupported file format")

# Przycisk do załadowania pliku
if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]
    if st.button("Load Data"):
        df = load_file(uploaded_file, file_extension)
        st.success("File loaded successfully!")
        st.write("### Preview of the dataset:")
        st.dataframe(df.head())
        
        # Lista wyboru kolumny, widoczna tylko gdy dane są załadowane
        column = st.selectbox("Select a column", df.columns)
