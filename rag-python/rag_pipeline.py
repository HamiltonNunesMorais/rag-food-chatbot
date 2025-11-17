from sentence_transformers import SentenceTransformer
import faiss
import json

# Carregar dados JSON
with open("data/food_data.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    docs = [
        f"{d['nome']} é um prato típico de {d['estado']}. "
        f"{d['descricao']} Categoria: {d['categoria']}. "
        f"Ingredientes: {', '.join(d['ingredientes'])}. "
        f"Em {d['mais_vendido']['ano']}, foi vendido {d['mais_vendido']['quantidade']} vezes, "
        f"ocupando o ranking {d['mais_vendido']['ranking']}."
        for d in dados
    ]

# Modelo de embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Criar índice FAISS
dimension = embedder.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(dimension)

# Adicionar embeddings ao índice
embs = embedder.encode(docs)
index.add(embs)

def buscar_contexto(query, k=3, threshold=1.0): 
    q_emb = embedder.encode([query])
    D, I = index.search(q_emb, k)

    resultados = []
    for dist, idx in zip(D[0], I[0]):
        if dist < threshold:
            resultados.append(docs[idx])

    return resultados

