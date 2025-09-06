from flask import Flask, request, jsonify, render_template_string
import ollama
import os

app = Flask(__name__)

with open(os.path.join(os.path.dirname(__file__), 'cat_emotions_knowledge.md'), encoding='utf-8') as f:
    KNOWLEDGE_BASE = f.read()

def search_knowledge(query):
    results = []
    for line in KNOWLEDGE_BASE.split('\n'):
        if any(word.lower() in line.lower() for word in query.split()):
            results.append(line)
    return '\n'.join(results) if results else 'Nenhuma informação encontrada na base.'

@app.route('/perguntar', methods=['POST'])
def perguntar():
    try:
        data = request.json
        pergunta = data.get('pergunta', '')
        
        if not pergunta.strip():
            return jsonify({'error': 'Pergunta não pode estar vazia'}), 400
        
        contexto = search_knowledge(pergunta)
        prompt = f"""Base de conhecimento sobre comportamento felino:
{contexto}

Pergunta do usuário: {pergunta}

Instruções para resposta:
- Responda como um especialista em comportamento felino, de forma clara e empática
- Use texto corrido, sem formatação markdown, tabelas ou listas com símbolos
- Seja prático e ofereça soluções acionáveis
- Se mencionar várias estratégias, separe-as em parágrafos ou frases simples
- Mantenha um tom acolhedor e compreensivo
- Limite a resposta a 3-4 parágrafos no máximo"""
        
        resposta = ollama.chat(model='gpt-oss', messages=[{"role": "user", "content": prompt}])
        return jsonify({'resposta': resposta['message']['content']})
        
    except Exception as e:
        return jsonify({'error': f'Erro ao processar pergunta: {str(e)}. Verifique se o Ollama está rodando com o modelo gpt-oss.'}), 500

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>miau miau</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { text-align: center; }
        textarea { width: 100%; padding: 10px; margin: 10px 0; }
        button { padding: 10px 20px; width: 100%; }
        .resposta { margin-top: 20px; padding: 15px; background: #f0f0f0; }
    </style>
</head>
<body>
    <div>
        <h1>🐱 Sistema de Emoções Felinas</h1>
        <p style="text-align: center;">
            Pergunte sobre o comportamento e emoções do seu gato.
        </p>
        
        <form id="perguntaForm">
            <label for="pergunta">Faça sua pergunta sobre seu gato:</label>
            <textarea id="pergunta" name="pergunta" placeholder="Ex: Meu gato está miando muito à noite, o que pode ser?" required></textarea>
            <button type="submit" id="submitBtn">Perguntar à IA</button>
        </form>
        
        <div id="resposta" style="display: none;"></div>
    </div>

    </div>

    <script>
        document.getElementById('perguntaForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const pergunta = document.getElementById('pergunta').value.trim();
            if (!pergunta) return;
            
            const submitBtn = document.getElementById('submitBtn');
            const respostaDiv = document.getElementById('resposta');
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'Consultando IA...';
            respostaDiv.innerHTML = '<div class="resposta">🤔 Analisando comportamento felino...</div>';
            respostaDiv.style.display = 'block';
            
            try {
                const response = await fetch('/perguntar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ pergunta: pergunta })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    respostaDiv.innerHTML = `<div class="resposta"><strong>Resposta:</strong><br><br>${data.resposta}</div>`;
                } else {
                    throw new Error(data.error || 'Erro na resposta');
                }
                
            } catch (error) {
                respostaDiv.innerHTML = `<div class="resposta">Erro: ${error.message}</div>`;
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Perguntar à IA';
            }
        });
    </script>
</body>
</html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
