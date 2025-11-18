# RAG FOOD Chatbot

Este projeto é um chatbot inteligente que responde perguntas sobre **comida regional brasileira** usando **RAG (Retrieval-Augmented Generation)** com FastAPI no backend e React no frontend.
> O projeto atualmente está em fase de **testes**.  
> As respostas são baseadas em dados de um arquivo JSON simples, o que torna o contexto limitado.  
> Futuramente, o projeto poderá ser expandido para utilizar um **banco de dados completo**, aumentando a precisão e a variedade das respostas.

## Arquivos do modelo Roberta

Este projeto inclui os arquivos menores do modelo `roberta-base-squad2` para facilitar a inicialização local.

Os arquivos grandes (pesados) não estão no repositório e devem ser baixados manualmente ou como seguinte script : **download_model.py** localizado na raiz do diretorio **RAG-PYTHON**:

---

## Demonstração


![alt text](<Video Project 1.gif>)  
> Exemplo: pergunta "Qual é o prato típico da Bahia?" → resposta "Acarajé"

---

## Como iniciar o projeto

### Backend (FastAPI + Transformers)

1. Baixe os arquivos do modelo Roberta-base-SQuAD2:

```bash
python rag-python/download_model.py # Esse processo pode levar alguns minutos. 
#Os arquivos serão salvos no seu diretorio indicado no script. 
#Se necessário, mova manualmente para rag-python/models/roberta-base-squad2
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  
# ou source venv/bin/activate no Linux/macOS
```

3. Instale as dependências:

```bash
cd rag-python
pip install -r requirements.txt
```

4. Inicie o servidor FastAPI:

```bash
uvicorn main:app --reload
```
A API estará disponível em: http://localhost:8000
![alt text](image.png)

### Frontend React

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

Para que o chatbot funcione corretamente, **mantenha dois terminais abertos**:

- Um terminal rodando o backend com FastAPI (`uvicorn main:app --reload`)
- Outro terminal rodando o frontend com React (`npm start`)

Isso garante que a interface consiga se comunicar com a API sem interrupções.


```bash
rag-food-chatbot/
├── rag-python/         # Backend FastAPI + modelo Roberta
├── front-react/        # Frontend React
├── .gitignore
├── README.md
```

