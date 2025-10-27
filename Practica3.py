import streamlit as st
import pandas as pd

df = pd.read_csv('nba_all_elo.csv')

st.sidebar.header('Filtros')

year_list = df['year_id'].unique()
team_list = df['team_id'].unique()
tipo_list = df['is_playoffs'].unique()

opciones = ['regular', 'plpayoffs', 'ambos']

with st.sidebar:
    year = st.selectbox('Seleccionar año', year_list, 0)
    team = st.selectbox('Seleccionar equipo', team_list, 0)
    tipo = st.pills('Seleccionar tipo', opciones)
 
