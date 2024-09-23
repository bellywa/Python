Código 8: Análise de Resultados dos Testes A/B

import pandas as pd
from scipy import stats

# Carrega os resultados dos testes A/B
results_control = pd.read_csv('/path/to/control_group.csv')
results_test = pd.read_csv('/path/to/test_group.csv')

# Calcula métricas de interesse, por exemplo, taxa de cliques e conversão
control_click_rate = results_control['clicks'].sum() / results_control['impressions'].sum()
test_click_rate = results_test['clicks'].sum() / results_test['impressions'].sum()

# Realiza um teste estatístico para comparar as duas taxas
stat, p_value = stats.ttest_ind(results_control['clicks'], results_test['clicks'])

print(f"Control Group Click Rate: {control_click_rate:.4f}")
print(f"Test Group Click Rate: {test_click_rate:.4f}")
print(f"p-value: {p_value:.4f}")

# Interpretação dos resultados
if p_value < 0.05:
    print("Diferença estatisticamente significativa entre os grupos.")
else:
    print("Nenhuma diferença estatisticamente significativa foi encontrada.")