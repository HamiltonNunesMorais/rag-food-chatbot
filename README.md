# RAG FOOD Chatbot

Este projeto é um chatbot inteligente que responde perguntas sobre **comida regional brasileira** usando **RAG (Retrieval-Augmented Generation)** com FastAPI no backend e React no frontend.

## Arquivos do modelo Roberta

Este projeto inclui os arquivos menores do modelo `roberta-base-squad2` para facilitar a inicialização local.

Os arquivos grandes (pesados) não estão no repositório e devem ser baixados manualmente ou como seguinte script : **download_model** localizado na raiz do diretorio **RAG-PYTHON**:

---

## 🎥 Demonstração

> *( GIF mostrando o app funcionando)*  
> Exemplo: pergunta "Qual é o prato típico da Bahia?" → resposta "Acarajé"

---

## 🚀 Como iniciar o projeto

### 🔧 Backend (FastAPI + Transformers)

1. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/macOS
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Baixe os arquivos do modelo Roberta-base-SQuAD2:

```bash
python rag-python/download_model.py # Esse processo pode levar alguns minutos. 
#Os arquivos serão salvos no seu diretorio indicado no script. 
#Se necessário, mova manualmente para rag-python/models/roberta-base-squad2
```

4. Inicie o servidor FastAPI:

```bash
cd rag-python
uvicorn main:app --reload
```
A API estará disponível em: http://localhost:8000

### 💻 Frontend Raect

1. Vá para a pasta do frontend:
```bash
cd front-react
```
2. Instale as dependências e inicie o servidor React:
```bash
npm install
npm start
```

A interface estará disponível em: http://localhost:3000

### Estrutura do Projeto
```bash
rag-food-chatbot/
├── rag-python/         # Backend FastAPI + modelo Roberta
├── front-react/        # Frontend React
├── .gitignore
├── README.md
```

