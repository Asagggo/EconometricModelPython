import pandas as pd
import numpy as np

# Cargar el archivo de Excel
file_path = r'C:\Users\Jaimee\Downloads\Archivos tesis\Datos\Por grupo\DataframeAbreviada.xlsx'
data = pd.read_excel(file_path)

# Filtrar valores negativos en IED (necesario para la transformación logarítmica)
data = data[data['IED'] > 0]

# Transformaciones
# TD: Calcular diferencias
data['ΔTD'] = data.groupby('PAIS')['TD'].diff()

# INF: Calcular diferencias
data['ΔINF'] = data.groupby('PAIS')['INF'].diff()

# CDP: Calcular diferencias
data['ΔCDP'] = data.groupby('PAIS')['CDP'].diff()

# CFG: Calcular diferencias
data['ΔCFG'] = data.groupby('PAIS')['CFG'].diff()

# IED: Transformación logarítmica (después de filtrar valores negativos) y luego diferencias
data['log_IED'] = np.log(data['IED'])
data['Δlog_IED'] = data.groupby('PAIS')['log_IED'].diff()

# PL: Transformación logarítmica directa
data['log_PL'] = np.log(data['PL'])

# PAT: Añadir constante de 1 y luego transformación logarítmica
data['log_PAT'] = np.log(data['PAT'] + 1)
data['Δlog_PAT'] = data.groupby('PAIS')['log_PAT'].diff()

# Eliminar filas con NaN generados por la operación diff()
data_cleaned = data.dropna()

# Guardar el dataframe transformado y limpio en un nuevo archivo Excel
output_file_path = r'C:\Users\Jaimee\Downloads\Archivos tesis\Datos\Por grupo\DataframeTransformada3.0.xlsx'
data_cleaned.to_excel(output_file_path, index=False)
