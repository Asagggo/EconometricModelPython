import pandas as pd
import numpy as np

# Cargar el archivo de Excel
file_path = r'C:\Users\Jaimee\Downloads\Archivos tesis\Datos\Por grupo\DataframeAbreviada.xlsx'
data = pd.read_excel(file_path)

# Transformación de cada variable según lo recomendado

# TD: Calcular diferencias
data['ΔTD'] = data.groupby('PAIS')['TD'].diff()

# INF: Calcular diferencias
data['ΔINF'] = data.groupby('PAIS')['INF'].diff()

# CDP: Calcular diferencias
data['ΔCDP'] = data.groupby('PAIS')['CDP'].diff()

# CFG: Calcular diferencias
data['ΔCFG'] = data.groupby('PAIS')['CFG'].diff()

# IED: Transformación logarítmica y luego diferencias
data['log_IED'] = np.log(data['IED'] + 1)
data['Δlog_IED'] = data.groupby('PAIS')['log_IED'].diff()

# PL: Transformación logarítmica
data['log_PL'] = np.log(data['PL'])

# PAT: Transformación logarítmica y luego diferencias
data['log_PAT'] = np.log(data['PAT'] + 1)
data['Δlog_PAT'] = data.groupby('PAIS')['log_PAT'].diff()

# Guardar el dataframe transformado en un nuevo archivo Excel
output_file_path = r'C:\Users\Jaimee\Downloads\Archivos tesis\Datos\Por grupo\DataframeTransformada2.0.xlsx'
data.to_excel(output_file_path, index=False)

# Mostrar las primeras filas del dataframe transformado
data.head()
