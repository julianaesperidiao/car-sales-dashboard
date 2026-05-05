import pandas as pd
import plotly.express as px
import streamlit as st

# título do app
st.header("Análise de anúncios de carros")

# carregar dados
df = pd.read_csv("vehicles.csv")

# layout em colunas
col1, col2 = st.columns(2)

with col1:
    show_hist = st.checkbox("Histograma de preço")

    if show_hist:
        st.write("Distribuição dos preços dos carros")
        fig = px.histogram(df, x="price")
        st.plotly_chart(fig)

with col2:
    show_scatter = st.checkbox("Preço vs quilometragem")

    if show_scatter:
        st.write("Relação entre preço e km rodados")
        fig = px.scatter(df, x="odometer", y="price")
        st.plotly_chart(fig)
        
    