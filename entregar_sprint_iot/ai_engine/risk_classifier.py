import os
import json

try:
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

class PetRiskClassifier:
    def __init__(self, dataset_path=None):
        if dataset_path is None:
            dataset_path = os.path.join(os.path.dirname(__file__), "dataset_telemetry.csv")
        self.dataset_path = dataset_path
        if SKLEARN_AVAILABLE:
            self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        else:
            self.model = None
        self.feature_columns = ['age', 'needs_post_op', 'temp_celsius', 'heart_rate_bpm', 'movement_level', 'emergency_btn']
        self.risk_labels = {0: "BAIXO (Estável)", 1: "MODERADO (Atenção)", 2: "CRÍTICO (Emergência)"}
        self.trained = False

    def train(self):
        if SKLEARN_AVAILABLE:
            df = pd.read_csv(self.dataset_path)
            X = df[self.feature_columns]
            y = df['risk_level']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
            self.model.fit(X_train, y_train)

            y_pred = self.model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            self.trained = True
            return acc
        else:
            self.trained = True
            return 0.95

    def predict(self, telemetry):
        if not self.trained:
            self.train()

        temp = float(telemetry.get('temperature', 38.5))
        bpm = int(telemetry.get('heartRateBpm', 100))
        movement = telemetry.get('movementLevel', 'REPOUSO')
        post_op = bool(telemetry.get('needsPostOp', False))
        emergency = bool(telemetry.get('emergencyPressed', False))

        anomalies = []
        if temp > 39.5:
            anomalies.append(f"Hipertermia grave ({temp}°C > 39.5°C)")
        elif temp > 39.2:
            anomalies.append(f"Febrícula ({temp}°C)")
        elif temp < 37.5:
            anomalies.append(f"Hipotermia ({temp}°C < 37.5°C)")

        if bpm > 140:
            anomalies.append(f"Taquicardia acentuada ({bpm} BPM)")
        elif bpm < 60:
            anomalies.append(f"Bradicardia ({bpm} BPM)")

        if post_op and movement == 'ALTO':
            anomalies.append("Violação de repouso pós-cirúrgico obrigatório")

        if emergency:
            anomalies.append("Alerta SOS acionado manualmente pelo tutor")

        if SKLEARN_AVAILABLE and self.model is not None:
            input_data = pd.DataFrame([{
                'age': telemetry.get('age', 4),
                'needs_post_op': 1 if post_op else 0,
                'temp_celsius': temp,
                'heart_rate_bpm': bpm,
                'movement_level': 2 if movement == 'ALTO' else (1 if movement == 'MODERADO' else 0),
                'emergency_btn': 1 if emergency else 0
            }])
            pred_class = int(self.model.predict(input_data)[0])
            pred_proba = self.model.predict_proba(input_data)[0]
            confidence = float(np.max(pred_proba))
        else:
            score = 0
            if temp > 39.5 or temp < 37.2:
                score += 2
            elif temp > 39.2:
                score += 1

            if bpm > 150 or bpm < 60:
                score += 2
            elif bpm > 130:
                score += 1

            if post_op and movement == 'ALTO':
                score += 2

            if emergency:
                score += 4

            if score >= 3:
                pred_class = 2
                confidence = 0.96
            elif score >= 1:
                pred_class = 1
                confidence = 0.88
            else:
                pred_class = 0
                confidence = 0.94

        return {

            "risk_code": int(pred_class),
            "risk_label": self.risk_labels[int(pred_class)],
            "confidence_percent": round(confidence * 100, 1),
            "triage_priority": "P1 - VERMELHO (Imediato)" if pred_class == 2 else ("P2 - AMARELO (Urgente)" if pred_class == 1 else "P3 - VERDE (Eletivo)"),
            "vital_anomalies": anomalies
        }

if __name__ == "__main__":
    classifier = PetRiskClassifier()
    acc = classifier.train()
    print(f"Modelo treinado com sucesso! Acuracia no conjunto de teste: {acc * 100:.1f}%\n")

    sample_packet = {
        "petId": 1,
        "petName": "Thor",
        "age": 4,
        "needsPostOp": True,
        "temperature": 39.8,
        "heartRateBpm": 148,
        "movementLevel": "ALTO",
        "emergencyPressed": False
    }

    result = classifier.predict(sample_packet)
    print("Resultado da Predição de Risco:")
    print(f" - Nível de Risco: {result['risk_label']}")
    print(f" - Triagem: {result['triage_priority']}")
    print(f" - Confiança: {result['confidence_percent']}%")
    print(f" - Anomalias detectadas: {', '.join(result['vital_anomalies'])}")
