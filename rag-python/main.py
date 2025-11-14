from fastapi import FastAPI
from transformers import pipeline
from rag_pipeline import buscar_contexto

app = FastAPI()

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
