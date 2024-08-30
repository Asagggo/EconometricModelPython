import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
file_path = r'C:\Users\Jaimee\Desktop\Modelo\EconometricModelPython\DataframeTransformada3.0IDH.xlsx'  #Ruta datos transformados

# Cargar los datos
data = pd.read_excel(file_path)

# Selección de las variables transformadas relevantes para el análisis preliminar
variables_transformadas = [
    'ΔTD', 'ΔINF', 'ΔCDP', 'ΔCFG', 'Δlog_IED', 'log_PL', 'Δlog_PAT'
]

# Filtrar el DataFrame para las variables seleccionadas
data_transformada = data[variables_transformadas]

# Generar la matriz de correlación
corr_matrix = data_transformada.corr()

# Visualizar la matriz de correlación utilizando un heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación - Variables Transformadas')
plt.show()
