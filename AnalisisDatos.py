#En este codigo se realizaran los análisis exploratorios de las variables
#Primero importamos las paqueterias instaladas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el dataframe
data_path = r'C:\Users\adria\OneDrive\Escritorio\EconometricModelPython\DataframeAbreviada.xlsx'
data = pd.read_excel(data_path)


# Mostrar las primeras filas del dataframe cargado para verificar su estructura
print(data.head())

# Seleccionar sólo las columnas de las variables explicativas
variables_explicativas = ['TD', 'INF', 'CDP', 'CFG', 'IED', 'PL', 'PAT']
desc_stats = data[variables_explicativas].describe()
print(desc_stats)

# Guardar estadísticas descriptivas en un archivo CSV para revisión
desc_stats.to_csv('Estadisticas_Descriptivas_2.csv')

# Visualización de la tasa de desempleo a lo largo del tiempo
plt.figure(figsize=(12, 8))
for country in data['PAÍS'].unique():
    country_data = data[data['PAÍS'] == country]
    plt.plot(country_data['AÑO'], country_data['TD'], label=country)
plt.xlabel('Año')
plt.ylabel('Tasa de Desempleo (%)')
plt.title('Evolución de la Tasa de Desempleo por País')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()