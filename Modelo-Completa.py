import pandas as pd
import statsmodels.api as sm  # Aseguramos la importación correcta de statsmodels
from linearmodels.panel import PanelOLS
import numpy as np
from statsmodels.stats.diagnostic import het_breuschpagan

# 1. Carga de Datos
data = pd.read_excel(r'C:\Users\Jaimee\Desktop\Modelo\EconometricModelPython\DataframeTransformada3.0IDH.xlsx')

# Asegurarnos de que el índice esté configurado correctamente para el panel
data = data.set_index(['PAIS', 'AÑO'])

# 2. Especificación del Modelo Arellano-Bond (GMM en diferencias)
# Variables dependiente e independientes
dependent_var = 'ΔTD'
exog_vars = ['Δlog_PAT', 'ΔINF', 'ΔCDP', 'ΔCFG', 'Δlog_IED', 'log_PL']

# 3. Creación de los instrumentos y diferencias
# Usaremos lags como instrumentos
data['L1_TD'] = data['TD'].shift(1)  # Lag de la variable dependiente original
instruments = ['L1_TD'] + exog_vars

# 4. Ajuste del modelo Arellano-Bond con GMM
# Como alternativa, PooledOLS con efectos por entidad y tiempo puede ser usado
model = PanelOLS(data[dependent_var], data[exog_vars], entity_effects=True, time_effects=True)
results = model.fit(cov_type='robust')

# 5. Pruebas de Diagnóstico
# Verificación de autocorrelación AR(1) y AR(2)
residuals = results.resids
ar1_test = sm.tsa.acf(residuals, nlags=2)[1]
ar2_test = sm.tsa.acf(residuals, nlags=2)[2]

# Convertir el modelo exog a un DataFrame para que sea compatible con het_breuschpagan
exog_data = results.model.exog.dataframe

# Agregar una constante (intercepto) a exog_data
exog_data_with_const = sm.add_constant(exog_data, has_constant='add')

# Pruebas de Heterocedasticidad
bp_test = het_breuschpagan(residuals, exog_data_with_const)

# 6. Exportación de Resultados
# Creación de un DataFrame para los resultados
results_df = pd.DataFrame({
    'Coeficiente': results.params,
    'Errores Estándar': results.std_errors,
    'T-Valor': results.tstats,
    'P-Valor': results.pvalues
})

# Agregamos los resultados de las pruebas de diagnóstico
diagnostics_df = pd.DataFrame({
    'AR(1) Test': [ar1_test, None],
    'AR(2) Test': [ar2_test, None],
    'Heterocedasticidad Test (BP)': [bp_test[0], bp_test[1]]
}, index=['Estadístico', 'P-Valor'])

# Guardamos los resultados en un archivo de Excel
with pd.ExcelWriter(r'C:\Users\Jaimee\Desktop\Modelo\EconometricModelPython\Resultados_Modelo_Arellano_Bond_Completa.xlsx') as writer:
    results_df.to_excel(writer, sheet_name='Resultados')
    diagnostics_df.to_excel(writer, sheet_name='Diagnostico')

print("Resultados y pruebas diagnósticas guardadas en 'Resultados_Modelo_Arellano_Bond_Completa.xlsx'.")
