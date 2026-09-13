# Guia de Simulação IoT - Wokwi (CLYVO VET Smart Collar)

Este diretório contém os arquivos para a simulação do nó IoT da **Coleira Inteligente / Telemetria Pós-Operatória CLYVO VET**.

---

## 🔌 Componentes Utilizados no Circuito

| Componente | Pino no Arduino | Função no Sistema |
| :--- | :--- | :--- |
| **Arduino UNO** | - | Microcontrolador de borda (Edge Computing) |
| **Potenciômetro Temp** | Pino Analógico A1 | Sensor Analógico de Temperatura Corporal (35.0 a 42.0 °C) |
| **Potenciômetro Pulso** | Pino Analógico A0 | Simulação do Sensor de Pulso Cardíaco (50 a 180 BPM) |
| **Botão Azul (Activity)** | Pino Digital 3 | Sensor de Movimentação / Acelerômetro (Repouso vs Atividade) |
| **Botão Vermelho (SOS)** | Pino Digital 7 | Botão de Pânico / Acionamento de Emergência do Tutor |
| **LED Verde** | Pino Digital 10 | Status: Animal Estável / Sinais Vitais Normais |
| **LED Amarelo** | Pino Digital 11 | Status: Alerta / Variação Moderada |
| **LED Vermelho** | Pino Digital 12 | Status: Crítico / Risco Iminente |
| **Buzzer** | Pino Digital 13 | Alarme Sonoro de Emergência |

---

## 🚀 Como Executar a Simulação

### Opção 1: Link Direto no Wokwi (100% Nativo - 1 Clique)
Acesse diretamente o projeto montado e salvo (sem necessidade de bibliotecas externas):
👉 **[https://wokwi.com/projects/475082149974273025](https://wokwi.com/projects/475082149974273025)**
Basta clicar no botão verde **Play** (ou pressionar `Ctrl + Enter`).

---

### Opção 2: Montagem Manual no Navegador
1. Acesse [https://wokwi.com/projects/new/arduino-uno](https://wokwi.com/projects/new/arduino-uno).
2. Na aba **sketch.ino**, cole o conteúdo de [`smart_collar.ino`](smart_collar.ino).
3. Na aba **diagram.json**, cole o conteúdo de [`diagram.json`](diagram.json).
4. Clique no botão verde **Play / Start Simulation** (não precisa de nenhuma biblioteca externa!).

---

### Opção 3: No VS Code com a Extensão Wokwi
1. Instale a extensão **Wokwi Simulator** no VS Code.
2. Abra a pasta `IOT/simulation`.
3. Pressione `F1` e digite `Wokwi: Start Simulator`.

---

## 🧪 Como Testar os Cenários ao Vivo

1. **Cenário 1: Animal Saudável e Estável (LED Verde Aceso)**
   - Temperatura no DHT22 em 38.5°C.
   - Potenciômetro na faixa intermediária (~90 a 110 BPM).
   - Botão de movimento solto (Repouso).
   - *Saída Serial:* `{"status":"ESTAVEL", "riskScore":0}`.

2. **Cenário 2: Alerta Moderado (LED Amarelo Aceso)**
   - Aumente a temperatura no DHT22 para 39.3°C ou aumente o BPM para 135 BPM.
   - *Saída Serial:* `{"status":"ATENCAO", "riskScore":1}`.

3. **Cenário 3: Emergência Pós-Operatória Crítica (LED Vermelho + Buzzer)**
   - Aumente a temperatura para 39.8°C (febre alta).
   - Pressione o botão azul de Movimento (animal recém-cirúrgico se movimentando com febre).
   - O buzzer começará a apitar e o LED vermelho piscará.
   - *Saída Serial:* `{"status":"CRITICO", "riskScore":4}`.
