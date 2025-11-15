from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from rag_pipeline import buscar_contexto

app = FastAPI()

# Habilitar CORS para permitir acesso do frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ou ["*"] para liberar geral
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar modelo QA
qa = pipeline("question-answering", model="models/roberta-base-squad2")

@app.get("/rag")
def rag(q: str):
    # Buscar contexto relevante
    contextos = buscar_contexto(q)
    print("Contextos encontrados:", contextos)

    # Se não encontrar nada relevante
    if not contextos:
        return {"resposta": "Desculpe, só tenho informações sobre comida regional brasileira."}

    # Unir os contextos
    contexto = " ".join(contextos)

    # Gerar resposta
    resposta = qa(question=q, context=contexto)["answer"]

    # Se a resposta for vazia ou genérica
    if not resposta.strip():
        return {"resposta": "Desculpe, só tenho informações sobre comida regional brasileira."}

    return {"resposta": resposta}
