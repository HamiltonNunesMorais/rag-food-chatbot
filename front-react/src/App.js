import React, { useState } from 'react';
import './App.css';

function App() {
  const [pergunta, setPergunta] = useState('');
  const [resposta, setResposta] = useState('');
  const [historico, setHistorico] = useState([]);

  const enviarPergunta = async () => {
    if (!pergunta.trim()) return;

    try {
      const res = await fetch(`http://localhost:8000/rag?q=${encodeURIComponent(pergunta)}`);
      const data = await res.json();
      setResposta(data.resposta);

      // Adiciona ao histórico
      setHistorico(prev => [...prev, { pergunta, resposta: data.resposta }]);
      setPergunta('');
    } catch (error) {
      setResposta('Erro ao buscar resposta.');
    }
  };

  return (
    <div className="container">
      <h1>RAG FOOD</h1>
      <p>Faça sua pergunta sobre comida regional:</p>
      <input
        type="text"
        value={pergunta}
        onChange={(e) => setPergunta(e.target.value)}
        placeholder="Ex: Qual é o prato típico da Bahia?"
      />
      <button onClick={enviarPergunta}>Perguntar</button>

      {resposta && (
        <div className="resposta">
          <strong>Resposta:</strong> {resposta}
        </div>
      )}

      {historico.length > 0 && (
        <div className="historico">
          <h2>Histórico</h2>
          <ul>
            {historico.map((item, index) => (
              <li key={index}>
                <strong>Pergunta:</strong> {item.pergunta}<br />
                <strong>Resposta:</strong> {item.resposta}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
