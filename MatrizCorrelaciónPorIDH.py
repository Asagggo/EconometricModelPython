import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
file_path = r'C:\Users\Jaimee\Desktop\Modelo\EconometricModelPython\DataframeTransformada3.0IDH.xlsx' 

# Cargar los datos
data = pd.read_excel(file_path)

# Selección de las variables transformadas relevantes para el análisis preliminar
variables_transformadas = [
    'ΔTD', 'ΔINF', 'ΔCDP', 'ΔCFG', 'Δlog_IED', 'log_PL', 'Δlog_PAT'
]

# Filtrar los datos por grupo de IDH
data_alto_IDH = data[data['GRUPO'] == 1][variables_transformadas]
data_bajo_IDH = data[data['GRUPO'] == 2][variables_transformadas]

# Generar la matriz de correlación para cada grupo
corr_matrix_alto_IDH = data_alto_IDH.corr()
corr_matrix_bajo_IDH = data_bajo_IDH.corr()

# Visualizar las matrices de correlación utilizando heatmaps
plt.figure(figsize=(16, 12))

# Matriz para Alto IDH
plt.subplot(2, 1, 1)
sns.heatmap(corr_matrix_alto_IDH, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación - Alto IDH')

# Matriz para Bajo IDH
plt.subplot(2, 1, 2)
sns.heatmap(corr_matrix_bajo_IDH, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación - Bajo IDH')

plt.tight_layout()
plt.show()
