Código 10: Simulação de Cenários com o Modelo Treinado
from surprise import SVD, Dataset, Reader
import pandas as pd

# Carrega o modelo previamente treinado (simulação)
model = SVD()
data = Dataset.load_from_file('user_data.csv', reader=Reader(line_format='user item rating timestamp', sep=','))

# Função para simular cenários
def simulate_recommendations(user_id, top_n=5):
    items = [str(i) for i in range(100)]  # Simulando 100 itens
    predictions = [model.predict(user_id, item) for item in items]
    predictions.sort(key=lambda x: x.est, reverse=True)
    
    # Retorna as top-N recomendações
    return [(pred.iid, pred.est) for pred in predictions[:top_n]]

# Simulação de recomendações para um usuário específico
user_id = '123'
recommendations = simulate_recommendations(user_id)
print(f"Top {len(recommendations)} recomendações para o usuário {user_id}:")
for item_id, score in recommendations:
    print(f"Item {item_id} - Score: {score:.2f}")
