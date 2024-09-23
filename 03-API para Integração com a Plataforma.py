Código 3: API para Integração com a Plataforma
from fastapi import FastAPI
from pydantic import BaseModel
from surprise import SVD, Dataset, Reader

app = FastAPI()

# Carrega o modelo previamente treinado
model = SVD()
# (Neste exemplo, não carregamos dados reais para simplicidade)

class RecomendationRequest(BaseModel):
    user_id: str
    item_id: str

@app.post("/recommendation/")
def get_recommendation(request: RecomendationRequest):
    # Faz uma previsão com o modelo treinado
    prediction = model.predict(request.user_id, request.item_id)
    return {"user_id": request.user_id, "item_id": request.item_id, "prediction": prediction.est}

# Comando para rodar a API com Uvicorn
# uvicorn main:app --reload