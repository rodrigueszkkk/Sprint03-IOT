import json

class ClyvoGenerativeAdvisor:
    def __init__(self):
        pass

    def build_clinical_prompt(self, pet_data, medical_record, telemetry_data, risk_assessment):
        prompt = f"""
[SYSTEM INSTRUCTION - CLYVO VET CLINICAL COPILOT]
Você é a IA Clínica Especialista do ecossistema CLYVO VET. Sua função é analisar dados de telemetria IoT em tempo real integrados ao prontuário médico eletrônico do paciente e gerar:
1. Orientação humanizada, empática e acionável para o tutor.
2. Relatório técnico estruturado no padrão SOAP para a equipe veterinária da clínica.

[CONTEXTO DO PACIENTE - BANCO DE DADOS CORE]
- Nome: {pet_data.get('name')}
- Espécie/Raça: {pet_data.get('breed')}
- Idade: {pet_data.get('age')} anos
- Tutor: {pet_data.get('tutorName')}
- Protocolo Pós-Operatório Ativo: {'SIM' if pet_data.get('needsPostOpCare') else 'NÃO'}

[HISTÓRICO CLÍNICO RECENTE - MEDICAL_RECORDS]
- Procedimento: {medical_record.get('description')}
- Diagnóstico Prévio: {medical_record.get('diagnosis')}
- Prescrição em Curso: {medical_record.get('treatment')}
- Veterinário Responsável: {medical_record.get('veterinarianName')}

[TELEMETRIA EM TEMPO REAL - IOT SMART COLLAR]
- Temperatura Corporal: {telemetry_data.get('temperature')} °C (Ref: 38.0°C - 39.2°C)
- Frequência Cardíaca: {telemetry_data.get('heartRateBpm')} BPM (Ref: 70 - 140 BPM)
- Nível de Atividade: {telemetry_data.get('movementLevel')}
- Botão de Pânico Tutor: {'ACIONADO' if telemetry_data.get('emergencyPressed') else 'NÃO ACIONADO'}

[INFERÊNCIA DO MODELO PREDITIVO DE RISCO]
- Classificação: {risk_assessment.get('risk_label')}
- Prioridade de Triagem: {risk_assessment.get('triage_priority')}
- Anomalias Detectadas: {', '.join(risk_assessment.get('vital_anomalies', []))}
"""
        return prompt.strip()

    def generate_guidance(self, pet_data, medical_record, telemetry_data, risk_assessment):
        risk_code = risk_assessment.get("risk_code", 0)
        pet_name = pet_data.get("name", "seu pet")
        tutor_name = pet_data.get("tutorName", "Tutor(a)")
        temp = telemetry_data.get("temperature", 38.5)
        bpm = telemetry_data.get("heartRateBpm", 100)

        if risk_code == 2:
            tutor_msg = (
                f"🚨 *ALERTA URGENTE CLYVO VET* 🚨\n\n"
                f"Olá, {tutor_name}! O colar inteligente do(a) *{pet_name}* detectou alterações críticas nos sinais vitais:\n"
                f"• Temperatura elevada: *{temp}°C* (sinal de hipertermia/febre)\n"
                f"• Batimentos acelerados: *{bpm} BPM*\n"
                f"• Movimentação incompatível com o repouso cirúrgico.\n\n"
                f"⚠️ *O QUE FAZER AGORA:*\n"
                f"1. Mantenha {pet_name} em local fresco, protegido e sem esforço físico.\n"
                f"2. NÃO administre medicamentos humanos ou doses extras sem autorização.\n"
                f"3. Leve-o imediatamente ao pronto-atendimento da CLYVO VET mais próxima.\n"
                f"📍 Já notificamos a equipe do plantão veterinário e o prontuário está aberto na sala de triagem!"
            )

            vet_report = (
                f"📋 *RELATÓRIO DE TRIAGEM CLÍNICA (PADRÃO S.O.A.P.)*\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"🔴 *PRIORIDADE:* P1 - VERMELHO (Atendimento Emergencial Imediato)\n"
                f"🐾 *PACIENTE:* {pet_name} ({pet_data.get('breed')}, {pet_data.get('age')} anos)\n\n"
                f"• [S] SUBJETIVO:\n"
                f"  Alerta automático de telemetria IoT. Tutor notificado via app.\n"
                f"  Histórico: {medical_record.get('description')}.\n\n"
                f"• [O] OBJETIVO:\n"
                f"  Temp: {temp}°C (Hipertermia importante) | FC: {bpm} BPM (Taquicardia sinusal provável).\n"
                f"  Atividade física detectada em paciente com repouso estrito pós-osteossíntese.\n\n"
                f"• [A] AVALIAÇÃO PRELIMINAR:\n"
                f"  Hipóteses: 1. Infecção precoce de ferida operatória / Sepse inicial.\n"
                f"             2. Dor aguda descompensada gerando taquicardia e agitação.\n"
                f"             3. Deiscência de sutura ou falha mecânica de implante.\n\n"
                f"• [P] PLANO SUGERIDO NA CHEGADA:\n"
                f"  1. Aferição física de sinais vitais, oximetria e tempo de preenchimento capilar (TPC).\n"
                f"  2. Inspeção detalhada do sítio cirúrgico e palpação de membro.\n"
                f"  3. Coleta de hemograma completo, lactato e proteína C-reativa (PCR).\n"
                f"  4. Avaliação radiográfica se houver claudicação ou instabilidade."
            )
        elif risk_code == 1:
            tutor_msg = (
                f"⚠️ *AVISO DE ATENÇÃO CLYVO VET*\n\n"
                f"Olá, {tutor_name}! Notamos uma leve variação nos sinais vitais do(a) {pet_name}:\n"
                f"• Temperatura em {temp}°C e batimentos em {bpm} BPM.\n"
                f"Recomendamos checar se {pet_name} tem água fresca disponível e garantir que permaneça em repouso. "
                f"Se os valores subirem nos próximos minutos, avisaremos imediatamente."
            )

            vet_report = (
                f"📋 *TRIAGEM CLÍNICA: P2 - AMARELO (Monitoramento Ativo)*\n"
                f"Paciente {pet_name} apresentando febrícula ou taquicardia limítrofe. Caso os parâmetros se mantenham elevados por mais de 30 minutos, sugerir antecipação de retorno ambulatorial."
            )
        else:
            tutor_msg = (
                f"💚 *CLYVO VET - STATUS DO PET: ESTÁVEL*\n\n"
                f"Tudo ótimo com {pet_name}! Sinais vitais em níveis ideais ({temp}°C, {bpm} BPM). O repouso está sendo cumprido com sucesso."
            )

            vet_report = (
                f"📋 *STATUS: P3 - VERDE (Parâmetros Fisiológicos Estáveis)*\n"
                f"Telemetria dentro dos limites de normalidade para a espécie e idade."
            )

        return {
            "tutor_message": tutor_msg,
            "veterinary_soap_report": vet_report
        }

if __name__ == "__main__":
    advisor = ClyvoGenerativeAdvisor()

    sample_pet = {
        "id": 1,
        "name": "Thor",
        "breed": "Golden Retriever",
        "age": 4,
        "tutorName": "Mariana Silva",
        "needsPostOpCare": True
    }

    sample_record = {
        "description": "Cirurgia ortopédica de ligamento cruzado cranial",
        "diagnosis": "Ruptura parcial de ligamento em membro pélvico direito",
        "treatment": "Anti-inflamatório Meloxicam e repouso absoluto por 14 dias",
        "veterinarianName": "Dra. Camila Torres - CRMV/SP 38421"
    }

    sample_telemetry = {
        "temperature": 39.8,
        "heartRateBpm": 148,
        "movementLevel": "ALTO",
        "emergencyPressed": False
    }

    sample_risk = {
        "risk_code": 2,
        "risk_label": "CRÍTICO (Emergência)",
        "triage_priority": "P1 - VERMELHO (Imediato)",
        "vital_anomalies": ["Hipertermia grave (39.8°C)", "Taquicardia acentuada (148 BPM)", "Violação de repouso pós-operatório"]
    }

    guidance = advisor.generate_guidance(sample_pet, sample_record, sample_telemetry, sample_risk)
    print("=" * 60)
    print(guidance["tutor_message"])
    print("=" * 60)
    print(guidance["veterinary_soap_report"])
    print("=" * 60)
