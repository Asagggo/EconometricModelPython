import pandas as pd

# Cargar el archivo Excel con la información del dataframe
dataframe_path = r'C:\Users\adria\OneDrive\Documentos\Tesis docs\Data modelo tesis\Filtrados Pýthon\DataframeAbreviada.xlsx'
df = pd.read_excel(dataframe_path)

# Verificar y mostrar los nombres de las columnas en el dataframe
print("Columnas disponibles en el dataframe:")
print(df.columns)

# Ajustar el nombre correcto de la columna según el archivo cargado
columna_abreviacion = df.columns[1]  # Suponiendo que la columna con las abreviaciones está en la segunda posición
print(f"Se utilizará la columna: {columna_abreviacion}")

# Diccionario con la asignación de grupos según la imagen adjunta
grupo_asignacion = {
    'ARM': 2, 'AUS': 1, 'AUT': 1, 'BEL': 1, 'BGR': 2, 'BLR': 2, 'BRA': 2, 'CAN': 1, 'CHE': 1, 'CHL': 1,
    'CHN': 2, 'COL': 2, 'CRI': 2, 'CYP': 1, 'CZE': 1, 'DEU': 1, 'DNK': 1, 'DZA': 2, 'ECU': 2, 'EGY': 2,
    'ESP': 1, 'EST': 1, 'FIN': 1, 'FRA': 1, 'GBR': 1, 'GRC': 1, 'GTM': 2, 'HKG': 1, 'HRV': 1, 'HUN': 1,
    'IDN': 2, 'IND': 2, 'IRL': 1, 'IRN': 2, 'ISL': 1, 'ISR': 1, 'ITA': 1, 'JPN': 1, 'KAZ': 2, 'KEN': 2,
    'KOR': 1, 'LTU': 1, 'LVA': 1, 'MAR': 2, 'MDA': 2, 'MEX': 2, 'MKD': 2, 'MLT': 1, 'MNG': 2, 'MYS': 2,
    'NLD': 1, 'NOR': 1, 'NZL': 1, 'PAK': 2, 'PER': 2, 'PHL': 2, 'POL': 1, 'PRT': 1, 'ROU': 2, 'RUS': 2,
    'SAU': 1, 'SGP': 1, 'SVK': 1, 'SVN': 1, 'SWE': 1, 'THA': 2, 'TUN': 2, 'TUR': 2, 'UKR': 2, 'USA': 1,
    'ZAF': 2
}

# Crear una nueva columna "Grupo" basada en el diccionario
df['Grupo'] = df[columna_abreviacion].map(grupo_asignacion)

# Función para filtrar el dataframe por grupo
def filtrar_por_grupo(df, grupo):
    """
    Filtra el dataframe según el grupo especificado (1 o 2).

    Parámetros:
        df (DataFrame): El dataframe original.
        grupo (int): El grupo por el cual filtrar (1 o 2).

    Retorna:
        DataFrame: Un nuevo dataframe filtrado por el grupo especificado.
    """
    return df[df['Grupo'] == grupo]

# Filtrar por Grupo 1
grupo_1 = filtrar_por_grupo(df, 1)
print("Países del Grupo 1:")
print(grupo_1)

# Filtrar por Grupo 2
grupo_2 = filtrar_por_grupo(df, 2)
print("\nPaíses del Grupo 2:")
print(grupo_2)

# Guardar los resultados filtrados y el dataframe completo con grupos asignados
grupo_1.to_excel(r'C:\Users\adria\OneDrive\Documentos\Tesis docs\Data modelo tesis\Filtrados Pýthon\grupo_1.xlsx', index=False)
grupo_2.to_excel(r'C:\Users\adria\OneDrive\Documentos\Tesis docs\Data modelo tesis\Filtrados Pýthon\grupo_2.xlsx', index=False)
df.to_excel(r'C:\Users\adria\OneDrive\Documentos\Tesis docs\Data modelo tesis\Filtrados Pýthon\dataframe_con_grupos.xlsx', index=False)
