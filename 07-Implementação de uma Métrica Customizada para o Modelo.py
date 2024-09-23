Código 7: Implementação de uma Métrica Customizada para o Modelo

from surprise import accuracy, SVD, Dataset, Reader
from surprise.model_selection import train_test_split

# Carrega os dados
data = Dataset.load_from_file('user_data.csv', reader=Reader(line_format='user item rating timestamp', sep=','))

# Divide os dados em treino e teste
trainset, testset = train_test_split(data, test_size=0.2)

# Define o modelo
model = SVD()

# Treina o modelo
model.fit(trainset)

# Faz previsões no conjunto de teste
predictions = model.test(testset)

# Define uma métrica customizada: Mean Percentage Error
def mean_percentage_error(predictions):
    errors = [abs(true_r - est) / true_r for (_, _, true_r, est, _) in predictions]
    return sum(errors) / len(errors)

# Calcula o RMSE padrão e a métrica customizada
rmse = accuracy.rmse(predictions)
mpe = mean_percentage_error(predictions)

print(f"RMSE: {rmse}, Mean Percentage Error: {mpe}")
