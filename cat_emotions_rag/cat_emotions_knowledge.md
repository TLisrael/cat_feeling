# Documentação Interna: Emoções e Sentimentos dos Felinos

## Introdução
Esta documentação reúne informações científicas, observacionais e práticas sobre as emoções dos gatos domésticos. O objetivo é fornecer um repositório abrangente e indexável para que o sistema RAG gere respostas precisas, empáticas e acionáveis para pais de pets.

## Visão geral das emoções felinas
Gatos não têm uma expressão emocional tão óbvia quanto humanos, mas exibem um conjunto de sinais físicos e comportamentais consistentes que podemos interpretar. Emoções comuns:

- Alegria / Contentamento
- Medo / Aversão
- Agressividade / Irritação
- Ansiedade / Estresse
- Curiosidade / Interesse
- Afeto / Vínculo
- Dor / Mal-estar (emocional e físico se misturam)

## Sinais corporais — interpretação detalhada
- Cauda:
	- Erguida com ponta levemente curvada: confiança e saudação.
	- Movimentos vibratórios curtos: excitação positiva (encontrar dono).
	- Batendo rápida e lateralmente: aborrecimento ou frustração.
	- Eriçada (pelo levantado): medo ou resposta defensiva.

- Orelhas:
	- Para frente: atenção/curiosidade.
	- Giradas lateralmente: incerteza.
	- Aplainadas contra a cabeça: medo, agressão ou estresse.

- Olhos e pupilas:
	- Semicerrados/olhos lentos: relaxamento e confiança.
	- Pupilas dilatadas: medo, excitação ou baixa iluminação (contexto importa).

- Postura corporal:
	- Postura relaxada deitado de lado: conforto.
	- Agachado e tenso: medo/alerta.
	- Postura arqueada e pelagem eriçada: tentativa de parecer maior — defesa/agressão.

- Pelagem e pelos eriçados: sinal claro de estresse agudo ou medo.

## Vocalizações — significados comuns
- Ronronar: geralmente associado a conforto, mas também pode ocorrer em dor/estresse; interpretar com contexto corporal.
- Miados: linguagem dirigida principalmente a humanos; variações no tom e frequência sinalizam diferentes pedidos (fome, atenção, desconforto).
- Sibilar / rosnar: aviso claro — não continuar a interação.

## Etiologias comuns (por que o gato sente X)
- Mudanças no ambiente: novos moradores, mudança de casa, obras.
- Problemas de saúde: dor, infecções do trato urinário, hipertiroidismo, problemas dentários.
- Rotina e enriquecimento insuficientes: tédio vira ansiedade/compulsão (lambedura excessiva).
- Socialização precoce inadequada: medo de humanos ou outros animais.

## Manejo prático por sentimento
- Separe medo e agressão: com medo, ofereça rota de fuga e espaço seguro; com agressão, diminua estímulos e não force interação.
- Para ansiedade: aumentar enriquecimento ambiental (arranhadores, brinquedos, esconderijos), rotina previsível, exercícios interativos.
- Para sinais de dor: encaminhar para veterinário imediatamente; alterações de comportamento + vocalização aguda são indicativos.

## Quando procurar um veterinário
- Mudança súbita e persistente no comportamento (menos interação, apetite reduzido).
- Vocalizações anormais e contínuas.
- Coceira/lambedura excessiva causando feridas.
- Marcação de urina dentro de casa, especialmente se associado a dor ao urinar.

## Enriquecimento e prevenção
- Oferecer arranhadores verticais e horizontais, prateleiras para escalada, caixas e esconderijos.
- Estimulação mental: brinquedos com alimentação, jogos de caça simulada.
- Socialização gradual com novos humanos e pets; respeitar território e dar rotas de fuga.

## Treinamento e reforço positivo
- Reforçar comportamentos desejados com petiscos, brinquedos ou carinho no momento certo.
- Evitar punição física ou gritar — isso aumenta medo e confusão.

## Estrutura de documentos para RAG (recomendação)
Cada entrada da base deve ser armazenada com campos para facilitar recuperação e contexto:

- id: string única
- title: título curto
- content: texto completo (1-3 parágrafos por chunk)
- tags: lista (ex.: "medo", "ronronar", "marcação" )
- source: referência (livro/artigo/autor)
- created_at/updated_at: timestamp

Notas para indexação: preferir chunks de 200–600 tokens; incluir metadados de tags e relevância clínica/comportamental.

## Estratégia RAG sugerida
- Pré-processar a documentação em chunks e gerar vetores com um modelo de embeddings compatível (ex.: sentence-transformers). Use um índice leve (FAISS, Chroma, SQLite + pgvector) local.
- Na consulta: 1) gerar embedding da pergunta; 2) recuperar top-k chunks; 3) construir prompt com contexto recuperado + instruções para o modelo (tom empático, citar fontes); 4) gerar resposta com o modelo local (Ollama gpt-oss).

## Exemplos de Q&A para treinar e validar respostas (base para RAG)
- Q: "Meu gato mia à noite toda — o que posso fazer?"
	A: "Verifique se há causas físicas (dor, fome, hiperatividade). Se for comportamento noturno por tédio, aumente atividades no dia, ofereça brinquedos interativos e crie rotina. Se persistir, consulte o vet para descartar problemas médicos."

- Q: "Meu gato esconde desde que trouxemos um bebê para casa."
	A: "Mudanças grandes no ambiente podem causar stress; ofereça locais tranquilos, permita fuga, e reintroduza com cheiros e reforço positivo.:

- Q: "O gato traz 'presentes' — isso é afeto?"
	A: "Sim, é comportamento natural de caça e compartilhamento; também pode ser tentativa de chamar atenção. Recompense sem punir."

## Glossário rápido
- Enriquecimento ambiental: estímulos que promovem atividade física e mental.
- RAG: Retrieval-Augmented Generation — técnica que combina recuperação de documentos com geração de texto.

## Referências e leituras adicionais
- Bradshaw, J. W. S. — Cat Sense (2013).
- Turner, D. C., & Bateson, P. — The Domestic Cat (2000).
- ISFM — guias práticos e artigos.
- Articles from journals on feline behaviour (search recommended for recent papers).

---
Esta base ampliada deve ser usada para gerar chunks e alimentar o índice vetorial do sistema RAG; se desejar, posso:

1. Gerar automaticamente os chunks e um arquivo JSONL pronto para importação no indexador.
2. Atualizar `app.py` para usar recuperação vetorial e construir prompts com as fontes.

Fim da documentação ampliada.
