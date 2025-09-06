# 🐱 Sistema de Emoções Felinas com IA

Um sistema inteligente que ajuda pais de pets a entenderem melhor as emoções e comportamentos dos seus gatos, utilizando tecnologia RAG (Retrieval-Augmented Generation) com Flask e Ollama.

## 📋 Sobre o Projeto

Este sistema combina uma base de conhecimento científica sobre comportamento felino com inteligência artificial para fornecer respostas precisas e empáticas sobre as emoções dos gatos. Utilizando a técnica RAG, o sistema busca informações relevantes na base de conhecimento e gera respostas personalizadas através do modelo GPT OSS via Ollama.

## 🚀 Funcionalidades

- **Interface Web Simples**: Interface limpa e intuitiva para fazer perguntas sobre gatos
- **Base de Conhecimento Especializada**: Documentação científica sobre comportamento e emoções felinas
- **RAG (Retrieval-Augmented Generation)**: Busca inteligente na base + geração de respostas com IA
- **Integração com Ollama**: Utiliza modelos de IA locais para privacidade e controle
- **Respostas Empáticas**: Tom acolhedor e soluções práticas para pais de pets

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **IA**: Ollama com modelo GPT OSS
- **RAG**: Sistema de busca na base de conhecimento + geração de respostas
- **Frontend**: HTML/CSS/JavaScript simples
- **Base de Dados**: Arquivo Markdown estruturado

## 📁 Estrutura do Projeto

```
cat_emotions_rag/
├── app.py                      # Aplicação Flask principal
├── cat_emotions_knowledge.md   # Base de conhecimento sobre felinos
├── requirements.txt            # Dependências Python
└── README.md                   # Este arquivo
```

## 🔧 Instalação e Configuração

### Pré-requisitos

1. **Python 3.8+** instalado
2. **Ollama** instalado e configurado ([https://ollama.com/](https://ollama.com/))
3. **Modelo GPT OSS** baixado no Ollama

### Instalação do Ollama e Modelo

```bash
# Instalar Ollama (Windows/Mac/Linux)
# Visite: https://ollama.com/download

# Baixar o modelo GPT OSS
ollama pull gpt-oss
```

### Configuração do Projeto

1. **Clone ou baixe o projeto**
   ```bash
   cd cat_emotions_rag
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Usar

### 1. Iniciar o Ollama
```bash
# Certifique-se de que o Ollama está rodando
ollama serve
```

### 2. Executar o Sistema
```bash
python app.py
```

### 3. Acessar a Interface Web
Abra seu navegador e acesse: `http://localhost:5000`

### 4. Fazer Perguntas
Digite perguntas sobre comportamento felino, como:
- "Meu gato está miando muito à noite, o que pode ser?"
- "Como saber se meu gato está feliz?"
- "Por que meu gato se esconde quando chegam visitas?"
- "O que significa quando o gato ronrona?"

## 🔍 Como Funciona

1. **Usuário faz uma pergunta** através da interface web
2. **Sistema busca** na base de conhecimento por informações relevantes
3. **RAG constrói um prompt** combinando a pergunta + contexto encontrado
4. **Ollama (GPT OSS) gera** uma resposta empática e informativa
5. **Resposta é exibida** na interface web

## 📊 Base de Conhecimento

A base de conhecimento inclui:

- **Emoções Felinas**: Alegria, medo, ansiedade, curiosidade, afeto
- **Sinais Corporais**: Interpretação de cauda, orelhas, olhos, postura
- **Vocalizações**: Significados de miados, ronronares, sibilos
- **Causas Comportamentais**: Fatores ambientais, saúde, socialização
- **Manejo Prático**: Soluções para diferentes situações
- **Quando Procurar Veterinário**: Sinais de alerta
- **Enriquecimento Ambiental**: Prevenção e bem-estar

## 🔧 API Endpoints

### POST /perguntar
Endpoint principal para fazer perguntas via API.

**Request:**
```json
{
  "pergunta": "Como saber se meu gato está feliz?"
}
```

**Response:**
```json
{
  "resposta": "Um gato feliz demonstra contentamento através de vários sinais..."
}
```

### GET /
Interface web principal.

## 🎯 Próximos Passos / Melhorias

- [ ] Implementar busca vetorial (FAISS/Chroma) para RAG mais preciso
- [ ] Adicionar mais conteúdo à base de conhecimento
- [ ] Implementar histórico de conversas
- [ ] Adicionar imagens ilustrativas de comportamentos
- [ ] Criar API para integração com outras aplicações
- [ ] Implementar cache de respostas
- [ ] Adicionar validação de entrada mais robusta

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🐾 Sobre Felinos

Este sistema foi desenvolvido com amor pelos felinos e baseado em pesquisas científicas sobre comportamento animal. Sempre consulte um veterinário para questões de saúde do seu pet.

---

**Desenvolvido com ❤️ para ajudar pais de pets a entenderem melhor seus felinos.**

