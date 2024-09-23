Código 5: Validação do Modelo de Recomendação

from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate, KFold
from surprise import accuracy

# Carrega os dados de exemplo
data = Dataset.load_from_file('user_data.csv', reader=Reader(line_format='user item rating timestamp', sep=','))

# Define o modelo de filtragem colaborativa
model = SVD()

# Configura a validação cruzada com KFold
kf = KFold(n_splits=5)

# Validação cruzada manual para detalhar os resultados
for trainset, testset in kf.split(data):
    # Treina o modelo
    model.fit(trainset)
    # Faz previsões
    predictions = model.test(testset)
    # Calcula e exibe as métricas
    rmse = accuracy.rmse(predictions, verbose=True)
    mae = accuracy.mae(predictions, verbose=True)
    print(f"Fold RMSE: {rmse}, Fold MAE: {mae}")

# Resultados da validação cruzada
results = cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
