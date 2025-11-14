# rag-food-chatbot
Rag App to retrieve data about food

## 🧠 Arquivos do modelo Roberta

Este projeto inclui os arquivos menores do modelo `roberta-base-squad2` para facilitar a inicialização local.

Os arquivos grandes (pesados) não estão no repositório e devem ser baixados com:

```bash
python script_down.py

### ⚙️ Ambiente virtual (Python)

> Os comandos abaixo funcionam no **Windows**. Para Linux/macOS, substitua `venv\Scripts\activate` por `source venv/bin/activate`.

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor FastAPI
python -m uvicorn rag_python.main:app --reload
