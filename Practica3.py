import streamlit as st
import pandas as pd

df = pd.read_csv('nba_all_elo.csv')
st.line_chart(df)

add_selecbox = st.sidebar.selectbox('Seleccionar año', (df['year_id']).unique())