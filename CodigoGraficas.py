import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo de Excel con los datos transformados
file_path = r'C:\Users\Jaimee\Downloads\Archivos tesis\Datos\Por grupo\DataframeTransformada3.0.xlsx'
data = pd.read_excel(file_path)

# Lista de variables antes de las transformaciones y sus respectivas transformaciones
variables_originales = ['TD', 'INF', 'CDP', 'CFG', 'IED', 'PL', 'PAT']
variables_transformadas = ['ΔTD', 'ΔINF', 'ΔCDP', 'ΔCFG', 'Δlog_IED', 'log_PL', 'log_PAT']

# Generar gráficos para cada variable original y transformada
for original, transformada in zip(variables_originales, variables_transformadas):
    # Crear figura y ejes
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfico de la variable original
    axs[0].plot(data['AÑO'], data[original], color='blue')
    axs[0].set_title(f'{original} - Datos sin transformar')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel(f'{original}')

    # Gráfico de la variable transformada
    axs[1].plot(data['AÑO'], data[transformada], color='green')
    axs[1].set_title(f'{transformada} - Datos Transformados')
    axs[1].set_xlabel('Year')
    axs[1].set_ylabel(f'{transformada}')

    # Ajustar el diseño y guardar la imagen
    plt.tight_layout()
    plt.savefig(f'{original}_vs_{transformada}.png')
    plt.close()
