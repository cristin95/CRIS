import pandas as pd
import cufflinks as cf
import plotly.offline as py
from IPython.display import display, HTML  # Necesario si estás en un Jupyter Notebook

# Configurar plotly para trabajar en modo offline
py.init_notebook_mode(connected=True)

# Configurar cufflinks para trabajar en modo offline
cf.go_offline()

# Leer el archivo CSV
df = pd.read_csv('D:/cursopython/population_total.csv')  # o usa r'D:\cursopython\population_total.csv'

# Verificar la estructura del DataFrame
print(df.head())
print(df.columns)

# Borrar los datos nulos
df = df.dropna()

# Pivotear el DataFrame
df_pivot = df.pivot(index='year', columns='country', values='population')

# Seleccionar ciertos países para simplificar el gráfico
selected_countries = ['United States', 'India', 'China', 'Indonesia', 'Brazil']
df_filtered = df_pivot[selected_countries]

# Crear un gráfico interactivo
df_filtered.iplot(kind='line', title='Población Total por País',
                  xTitle='Año', yTitle='Población', 
                  filename='cufflinks/line-chart')

