from huggingface_hub import snapshot_download

# Caminho local onde o modelo será salvo
local_path = "C:\<user_folder>\\rag-food-chatbot\\rag-python\\models"


# Baixar o modelo completo
snapshot_download(
    repo_id="deepset/roberta-base-squad2",
    local_dir=local_path,
    local_dir_use_symlinks=False  # evita problemas com links no Windows
)
