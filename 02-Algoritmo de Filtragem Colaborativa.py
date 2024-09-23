Código 2: Algoritmo de Filtragem Colaborativa

from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import cross_validate

# Carrega os dados de exemplo
data = Dataset.load_from_file('user_data.csv', reader=Reader(line_format='user item rating timestamp', sep=','))

# Define o modelo de filtragem colaborativa
model = SVD()

# Realiza a validação cruzada do modelo
cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Treinamento do modelo completo
trainset = data.build_full_trainset()
model.fit(trainset)

# Exemplo de previsão para um usuário específico
user_id = str(123)
item_id = str(456)
pred = model.predict(user_id, item_id)
print(pred)
