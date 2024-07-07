import pandas as pd

# Cargar el archivo de Excel
file_path = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\DataframeAbreviada.xlsx'  
data = pd.read_excel(file_path)

#Importamos el resto de librerias
import seaborn as sns
import matplotlib.pyplot as plt

# Mostrar las primeras filas del dataframe para confirmar que se cargó correctamente
print(data.head())

# Estadísticas descriptivas básicas (excluyendo 'PAIS' y 'AÑO')
numeric_data = data.drop(columns=['PAIS', 'AÑO'])
descriptive_stats = numeric_data.describe()
print(descriptive_stats)

# Sesgo (Skewness) y Curtosis (Kurtosis)
skewness = numeric_data.skew()
kurtosis = numeric_data.kurt()

print("\nSkewness:")
print(skewness)
print("\nKurtosis:")
print(kurtosis)

# Guardar resultados en un archivo Excel
output_file = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\Análisis descriptivo\analysis_results_all_countries.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Guardar estadísticas descriptivas
    descriptive_stats.to_excel(writer, sheet_name='Descriptive Stats')
    
    # Guardar sesgo y curtosis
    skew_kurt = pd.DataFrame({'Skewness': skewness, 'Kurtosis': kurtosis})
    skew_kurt.to_excel(writer, sheet_name='Skewness and Kurtosis')

    # Guardar matriz de correlación
    correlation_matrix = numeric_data.corr()
    correlation_matrix.to_excel(writer, sheet_name='Correlation Matrix')

# Generar gráficos y guardarlos en el archivo Excel
import openpyxl
from openpyxl.drawing.image import Image

# Cargar el archivo para añadir gráficos
wb = openpyxl.load_workbook(output_file)

# Función para añadir gráficos al archivo Excel
def add_plot_to_excel(plot_func, sheet_name, cell):
    plot_func()
    plt.savefig('/mnt/data/temp_plot.png')
    plt.close()
    img = Image('/mnt/data/temp_plot.png')
    ws = wb[sheet_name]
    ws.add_image(img, cell)

# Crear una hoja para los gráficos
wb.create_sheet('Plots')

# Gráficos de distribución y boxplots para cada variable
row_counter = 1
for column in numeric_data.columns:  # Solo variables numéricas
    # Gráfico de distribución
    plt.figure()
    sns.histplot(numeric_data[column], kde=True).set_title(f'Distribution of {column}')
    plt.savefig(f'/mnt/data/{column}_distribution.png')
    plt.close()
    img = Image(f'/mnt/data/{column}_distribution.png')
    ws = wb['Plots']
    ws.add_image(img, f'A{row_counter}')
    
    # Gráfico de boxplot
    plt.figure()
    sns.boxplot(x=numeric_data[column]).set_title(f'Boxplot of {column}')
    plt.savefig(f'/mnt/data/{column}_boxplot.png')
    plt.close()
    img = Image(f'/mnt/data/{column}_boxplot.png')
    ws.add_image(img, f'E{row_counter}')
    
    row_counter += 20

# Guardar el archivo con gráficos incluidos
wb.save(output_file)
