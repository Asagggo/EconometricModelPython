import pandas as pd

# Cargar el archivo de datos principales
data_path = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\DataframeAbreviada.xlsx'
data = pd.read_excel(data_path)

# Cargar el archivo con la clasificación de países en grupos
grupos_path = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\Grupos_paises.xlsx'  
grupos_data = pd.read_excel(grupos_path)

# Unir los datos principales con la clasificación de grupos
merged_data = pd.merge(data, grupos_data, on='PAÍS')

# Mostrar las primeras filas para verificar
print(merged_data.head())

# Dividir los datos en dos grupos
grupo_alto_idh = merged_data[merged_data['GRUPO'] == 1]
grupo_bajo_idh = merged_data[merged_data['GRUPO'] == 2]

# Calcular estadísticas descriptivas para cada grupo
desc_stats_alto_idh = grupo_alto_idh.describe()
desc_stats_bajo_idh = grupo_bajo_idh.describe()

# Mostrar las estadísticas descriptivas
print("Estadísticas Descriptivas para Países con Alto IDH")
print(desc_stats_alto_idh)

print("\nEstadísticas Descriptivas para Países con Bajo IDH")
print(desc_stats_bajo_idh)

# Guardar las estadísticas descriptivas en archivos CSV para revisión
desc_stats_alto_idh.to_csv('Estadisticas_Descriptivas_Alto_IDH.csv')
desc_stats_bajo_idh.to_csv('Estadisticas_Descriptivas_Bajo_IDH.csv')

# Guardar los DataFrames de cada grupo en archivos Excel separados
grupo_alto_idh.to_excel('Datos_Alto_IDH.xlsx', index=False)
grupo_bajo_idh.to_excel('Datos_Bajo_IDH.xlsx', index=False)
