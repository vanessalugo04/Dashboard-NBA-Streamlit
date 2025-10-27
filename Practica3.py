import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('nba_all_elo.csv')

st.sidebar.header('Filtros')

year_list = df['year_id'].unique()
team_list = df['team_id'].unique()
tipo_list = df['is_playoffs'].unique()

opciones = ['regular', 'playoffs', 'ambos']

with st.sidebar:
    year = st.selectbox('Seleccionar año', year_list, 0)
    team = st.selectbox('Seleccionar equipo', team_list, 0)
    tipo = st.pills('Seleccionar tipo', opciones)


st.title("Datos!")
st.write(f"Equipo: {team}")
st.write(f"Año: {year}")
st.write(f'Tipo {tipo}')

resultado = df['is_playoffs'] == 0
if tipo == 'regular':
    resultado = df['is_playoffs'] == 0
elif tipo == 'playoffs':
    resultado = df['is_playoffs'] == 1
else:
    resultado = (df['is_playoffs'] == 1) | (df['is_playoffs'] == 0)

df_temp = df[(df['year_id'] == int(year)) & (df['team_id'] == team) & resultado].copy()

print(df_temp)
df_temp = df_temp.sort_values('seasongame').reset_index(drop=True)

df_temp['ganado'] = (df_temp['game_result'] == 'W').astype(int)
df_temp['perdido'] = (df_temp['game_result'] == 'L').astype(int)

df_temp['ganado_acum'] = df_temp['ganado'].cumsum()
df_temp['perdido_acum'] = df_temp['perdido'].cumsum()
df_final =  df_temp.loc[:, ['seasongame', 'ganado_acum', 'perdido_acum']].set_index('seasongame')

st.line_chart(df_final)

 
total_ganados = df_temp['ganado'].sum()
total_perdidos = df_temp['perdido'].sum()

fig, ax = plt.subplots()
ax.pie(
    [total_ganados, total_perdidos],
    labels=['Ganados', 'Perdidos'],
    autopct='%1.1f%%',
    colors=['green', 'red'],
    startangle=90
)
ax.set_title(f'Porcentaje de juegos ganados y perdidos - {team} {year}')
ax.axis('equal')  # Para que sea circular

st.subheader("Distribución de resultados")
st.pyplot(fig)