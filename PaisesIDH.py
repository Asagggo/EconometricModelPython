import pandas as pd

# Cargar los archivos
grupo_data = pd.read_excel(r'C:\Users\Jaimee\Downloads\Archivos tesis\Datos\Por grupo\Grupos_paises.xlsx')
new_data = pd.read_excel(r'C:\Users\Jaimee\Downloads\Archivos tesis\Datos\Por grupo\DataframeTransformada3.0.xlsx')

# Realizar la fusión en base al nombre del país
merged_data = pd.merge(grupo_data, new_data, how='right', left_on='PAÍS', right_on='PAIS')

# Eliminar la columna duplicada "PAÍS"
merged_data = merged_data.drop(columns=['PAÍS'])

# Reorganizar columnas para colocar 'GRUPO' al inicio
cols = ['GRUPO'] + [col for col in merged_data if col != 'GRUPO']
merged_data = merged_data[cols]

# Guardar el archivo final con la nueva columna
merged_data.to_excel(r'C:\Users\Jaimee\Desktop\Modelo\EconometricModelPython\DataframeTransformada3.0IDH.xlsx', index=False)
