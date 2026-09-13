import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from risk_classifier import PetRiskClassifier
from generative_advisor import ClyvoGenerativeAdvisor


def run_pipeline(scenario="critico"):
    print("=" * 65)
    print("   CLYVO VET - ECOSSISTEMA INTELIGENTE DE IOT & IA VETERINÁRIA    ")
    print("   Disruptive Architectures: IoT, IoB & Generative AI - Sprint 3 ")
    print("=" * 65)

    pet_db = {
        1: {
            "id": 1,
            "name": "Thor",
            "breed": "Golden Retriever",
            "age": 4,
            "tutorName": "Mariana Silva",
            "needsPostOpCare": True
        }
    }

    record_db = {
        1: {
            "description": "Cirurgia ortopédica de osteossíntese femoral",
            "diagnosis": "Fratura completa de fêmur direito tratada com placa e parafusos",
            "treatment": "Anti-inflamatório Meloxicam 0.1mg/kg por 7 dias e repouso absoluto",
            "veterinarianName": "Dra. Camila Torres - CRMV/SP 38421"
        }
    }

    if scenario == "critico":
        raw_iot_packet = {
            "deviceId": "CLYVO-COLLAR-01",
            "petId": 1,
            "petName": "Thor",
            "age": 4,
            "needsPostOp": True,
            "temperature": 39.9,
            "heartRateBpm": 152,
            "movementLevel": "ALTO",
            "emergencyPressed": False,
            "timestamp": "2026-09-13T14:30:00Z"
        }
    elif scenario == "atencao":
        raw_iot_packet = {
            "deviceId": "CLYVO-COLLAR-01",
            "petId": 1,
            "petName": "Thor",
            "age": 4,
            "needsPostOp": True,
            "temperature": 39.3,
            "heartRateBpm": 132,
            "movementLevel": "MODERADO",
            "emergencyPressed": False,
            "timestamp": "2026-09-13T14:30:00Z"
        }
    else:
        raw_iot_packet = {
            "deviceId": "CLYVO-COLLAR-01",
            "petId": 1,
            "petName": "Thor",
            "age": 4,
            "needsPostOp": True,
            "temperature": 38.5,
            "heartRateBpm": 95,
            "movementLevel": "REPOUSO",
            "emergencyPressed": False,
            "timestamp": "2026-09-13T14:30:00Z"
        }

    print("\n[ETAPA 1/4] RECEBIMENTO DE TELEMETRIA DO DISPOSITIVO IOT (WOKWI / ESP32):")
    print(json.dumps(raw_iot_packet, indent=2))

    print("\n[ETAPA 2/4] PROCESSAMENTO NO MODELO PREDITIVO DE RISCO (MACHINE LEARNING):")
    classifier = PetRiskClassifier()
    classifier.train()
    risk_assessment = classifier.predict(raw_iot_packet)

    print(f" -> Classificação de Risco: {risk_assessment['risk_label']}")
    print(f" -> Prioridade de Triagem : {risk_assessment['triage_priority']}")
    print(f" -> Confiança do Modelo   : {risk_assessment['confidence_percent']}%")
    if risk_assessment['vital_anomalies']:
        print(" -> Anomalias Detectadas  :")
        for anom in risk_assessment['vital_anomalies']:
            print(f"    * {anom}")
    else:
        print(" -> Nenhuma anomalia fisiológica detectada.")

    print("\n[ETAPA 3/4] ENRIQUECIMENTO DE DADOS COM PRONTUÁRIO CLÍNICO (MYSQL / API):")
    pet = pet_db.get(raw_iot_packet["petId"])
    record = record_db.get(raw_iot_packet["petId"])
    print(f" -> Paciente: {pet['name']} | Tutor: {pet['tutorName']} | Pós-Op: {pet['needsPostOpCare']}")
    print(f" -> Último Prontuário: {record['description']} ({record['veterinarianName']})")

    print("\n[ETAPA 4/4] INFERÊNCIA DA IA GENERATIVA (COPILOTO CLYVO VET):")
    advisor = ClyvoGenerativeAdvisor()
    guidance = advisor.generate_guidance(pet, record, raw_iot_packet, risk_assessment)

    print("\n" + "=" * 30 + " MENSAGEM AO TUTOR " + "=" * 30)
    print(guidance["tutor_message"])

    print("\n" + "=" * 25 + " RELATÓRIO CLÍNICO DE TRIAGEM (SOAP) " + "=" * 25)
    print(guidance["veterinary_soap_report"])
    print("=" * 70)

if __name__ == "__main__":
    scenario = "critico"
    if len(sys.argv) > 1:
        scenario = sys.argv[1].lower()
    run_pipeline(scenario)
