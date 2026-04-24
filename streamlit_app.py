import streamlit as st
import pandas as pd

st.title("CSV Data Inspector")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview")
    st.dataframe(df)

    st.subheader("Dataset Info")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Column Types")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isna().sum())

    st.subheader("Basic Stats")
    st.write(df.describe(include="all"))

    if st.button("Drop Empty Rows"):
        df = df.dropna()
        st.success("Empty rows removed")
        st.dataframe(df)