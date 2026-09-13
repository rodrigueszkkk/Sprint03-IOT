# Roteiro do Vídeo Pitch (~5 minutos) - CLYVO VET
## Disciplina: Disruptive Architectures: IoT, IoB & Generative AI (Sprint 3)
### Tema: Monitoramento Contínuo e Copiloto Clínico com IA para a Jornada do Pet

---

### ⏱️ Divisão de Tempo do Pitch (5 Minutos)

| Tempo | Etapa | O que mostrar na tela |
| :--- | :--- | :--- |
| **00:00 - 01:00** | Bloco 1: O Problema de Negócio | Slide inicial / `README.md` no GitHub com Nomes e RMs |
| **01:00 - 02:00** | Bloco 2: A Solução e Arquitetura | Diagrama Arquitetural de IoT & IA (`assets/iot_ai_architecture.png`) |
| **02:00 - 03:30** | Bloco 3: Demonstração da IA e IoT | Simulação no Wokwi e execução do script Python (`main.py`) |
| **03:30 - 04:30** | Bloco 4: Benefícios para Tutor e Clínica | Dashboard de Triagem / Mensagem gerada ao tutor |
| **04:30 - 05:00** | Bloco 5: Conclusão e Futuro | Conclusão do pitch e chamada para a entrega |

---

## 🎬 Roteiro Falado Passo a Passo (Casual, Natural e Confiante)

---

### BLOCO 1: Identificação e a Dor de Negócio (00:00 - 01:00)
**Tela:** Repositório no GitHub aberto no `README.md`, mostrando a tabela de integrantes.

**Como falar:**
> *"Fala, professor! Tudo bem? Aqui é o Kaiky Pereira (RM 564578), e hoje apresento o pitch da Sprint 3 de Disruptive Architectures: IoT, IoB e Generative AI com o meu grupo, o Leandro Guarido (RM 561760) e o Gabriel Solano (RM 562325).*  
> *O nosso projeto é a **CLYVO VET**, e nós focamos em resolver uma das maiores dores da assistência veterinária atual: o que acontece com o pet depois da alta médica?*  
> *Hoje existe um verdadeiro 'apagão' de informações quando o animal sai da clínica operado ou doente. Os tutores têm dificuldade de perceber os primeiros sinais de dor ou febre, e quando decidem levar o pet de volta, muitas vezes o quadro já virou uma emergência grave de choque ou infecção. Ao mesmo tempo, as clínicas ficam sobrecarregadas, sem conseguir priorizar quem realmente está em risco de vida."*

---

### BLOCO 2: A Solução CLYVO VET e Arquitetura (01:00 - 02:00)
**Tela:** Mudar para o diagrama arquitetural (`assets/iot_ai_architecture.png`).

**Como falar:**
> *"Pra resolver isso, a gente uniu **Hardware de Borda (IoT)** com **Inteligência Artificial Híbrida** integrada ao nosso sistema de prontuários em nuvem.*  
> *A solução começa na **CLYVO Smart Collar**, uma coleira inteligente com sensores que lê a temperatura corporal, a frequência cardíaca e o nível de movimentação do animal em tempo real.*  
> *Esses dados são enviados via internet e cruzados diretamente com o prontuário eletrônico do pet no nosso banco de dados relacional.*  
> *E é aí que entra o coração do projeto: o nosso motor de IA em duas etapas. Primeiro, um modelo preditivo de Machine Learning que calcula o risco vital do animal na hora; e segundo, um copiloto de IA Generativa que traduz tudo isso em ações práticas tanto pro tutor quanto pro veterinário."*

---

### BLOCO 3: Demonstração Funcional ao Vivo (02:00 - 03:30)
**Tela:**
1. Mostrar o **Wokwi** rodando o circuito com os sensores variando e o monitor serial gerando o JSON.
2. Mudar para o terminal e rodar `python main.py critico`.

**Como falar:**
> *"Aqui na tela o senhor pode ver o nosso nó IoT simulado no Wokwi. Quando o sensor detecta uma alteração, por exemplo, o pet Thor tendo febre de 39.9°C e batimentos a 152 BPM logo após uma cirurgia ortopédica, o dispositivo gera o pacote de telemetria em JSON.*  
> *Agora eu rodo o nosso pipeline de IA aqui no terminal: `python main.py critico`.*  
> *Reparem o que aconteceu em frações de segundo:*  
> *O modelo preditivo identificou a hipertermia e a taquicardia com 96% de confiança e classificou o caso como **CRÍTICO - Prioridade P1 Vermelha**.*  
> *Imediatamente, o nosso Copiloto com IA Generativa cruzou esses sinais com a cirurgia de fêmur do Thor gravada no banco e gerou dois relatórios automáticos:*  
> *Uma mensagem humanizada no WhatsApp da tutora Mariana, explicando sem pânico o que fazer e orientando o deslocamento imediato; e um relatório clínico no padrão internacional **SOAP** direto na tela do veterinário de plantão, com as hipóteses de infecção ou dor aguda e as condutas para quando o Thor chegar!"*

---

### BLOCO 4: Benefícios para o Tutor e para a Clínica (03:30 - 04:30)
**Tela:** Destacar no `README.md` a seção de Benefícios ou a mensagem gerada.

**Como falar:**
> *"Esse fluxo gera um impacto gigantesco pros dois lados da ponta:*  
> *Pro tutor, traz a tranquilidade de saber que o pet tá sendo monitorado 24 horas por dia por profissionais, acabando com a angústia da recuperação pós-cirúrgica em casa.*  
> *E pra clínica veterinária, isso revoluciona a rotina: o veterinário já recebe o paciente triado, com hipóteses diagnósticas e sinais vitais mastigados, reduzindo o tempo de consulta em mais de 40%. Além disso, a clínica abre uma nova linha de receita recorrente oferecendo planos de telemetria pós-operatória inteligente."*

---

### BLOCO 5: Conclusão e Encerramento (04:30 - 05:00)
**Tela:** Voltar ao repositório GitHub com o diagrama e logos da FIAP / CLYVO VET.

**Como falar:**
> *"A CLYVO VET transforma a medicina veterinária de um modelo puramente reativo para um modelo proativo e contínuo, unindo IoT na borda, banco de dados em nuvem e inteligência artificial preditiva e generativa.*  
> *Todos os códigos da simulação, os modelos de IA em Python e a documentação completa estão disponíveis no nosso repositório no GitHub.*  
> *Muito obrigado pelo semestre e pela mentoria, professor!"*

---

### 📋 Dicas para a Gravação do Pitch:
- Mantenha o tom dinâmico e empolgado: é um **pitch de negócios e tecnologia**!
- Não precisa de edição pesada, basta compartilhar a tela e alternar entre o `README`, o Wokwi e o terminal rodando `python main.py`.
- O tempo ideal é de **4 minutos e 30 segundos a 5 minutos**.
