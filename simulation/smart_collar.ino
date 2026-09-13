#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT22

#define PIN_PULSE_SENSOR A0
#define PIN_ACTIVITY_SENSOR 3
#define PIN_EMERGENCY_BTN 7

#define PIN_LED_GREEN 10
#define PIN_LED_YELLOW 11
#define PIN_LED_RED 12
#define PIN_BUZZER 13

DHT dht(DHTPIN, DHTTYPE);

const int PET_ID = 1;
const char* PET_NAME = "Thor";
const bool NEEDS_POST_OP_CARE = true;

unsigned long previousMillis = 0;
const long telemetryInterval = 3000;

void setup() {
  Serial.begin(9600);

  dht.begin();

  pinMode(PIN_PULSE_SENSOR, INPUT);
  pinMode(PIN_ACTIVITY_SENSOR, INPUT_PULLUP);
  pinMode(PIN_EMERGENCY_BTN, INPUT_PULLUP);

  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_LED_YELLOW, OUTPUT);
  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);

  digitalWrite(PIN_LED_GREEN, LOW);
  digitalWrite(PIN_LED_YELLOW, LOW);
  digitalWrite(PIN_LED_RED, LOW);
  digitalWrite(PIN_BUZZER, LOW);

  Serial.println("==================================================");
  Serial.println("  CLYVO VET - SMART COLLAR TELEMETRY NODE (IoT)   ");
  Serial.println("  Iniciando monitoramento de sinais vitais...     ");
  Serial.println("==================================================");
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= telemetryInterval) {
    previousMillis = currentMillis;

    float temperature = dht.readTemperature();
    if (isnan(temperature)) {
      temperature = 38.5;
    }

    int rawPulse = analogRead(PIN_PULSE_SENSOR);
    int heartRate = map(rawPulse, 0, 1023, 50, 180);

    bool isMoving = (digitalRead(PIN_ACTIVITY_SENSOR) == LOW);
    bool emergencyPressed = (digitalRead(PIN_EMERGENCY_BTN) == LOW);

    String statusStr = "ESTAVEL";
    int riskScore = 0;

    if (temperature > 39.5 || temperature < 37.2) {
      riskScore += 2;
    } else if (temperature > 39.2) {
      riskScore += 1;
    }

    if (heartRate > 150 || heartRate < 60) {
      riskScore += 2;
    } else if (heartRate > 130) {
      riskScore += 1;
    }

    if (NEEDS_POST_OP_CARE && isMoving) {
      riskScore += 2;
    }

    if (emergencyPressed) {
      riskScore += 4;
    }

    if (riskScore >= 3) {
      statusStr = "CRITICO";
      digitalWrite(PIN_LED_GREEN, LOW);
      digitalWrite(PIN_LED_YELLOW, LOW);
      digitalWrite(PIN_LED_RED, HIGH);
      tone(PIN_BUZZER, 1000, 200);
    } else if (riskScore >= 1) {
      statusStr = "ATENCAO";
      digitalWrite(PIN_LED_GREEN, LOW);
      digitalWrite(PIN_LED_YELLOW, HIGH);
      digitalWrite(PIN_LED_RED, LOW);
      noTone(PIN_BUZZER);
    } else {
      statusStr = "ESTAVEL";
      digitalWrite(PIN_LED_GREEN, HIGH);
      digitalWrite(PIN_LED_YELLOW, LOW);
      digitalWrite(PIN_LED_RED, LOW);
      noTone(PIN_BUZZER);
    }

    Serial.print("{\"deviceId\":\"CLYVO-COLLAR-01\",\"petId\":");
    Serial.print(PET_ID);
    Serial.print(",\"petName\":\"");
    Serial.print(PET_NAME);
    Serial.print("\",\"temperature\":");
    Serial.print(temperature, 1);
    Serial.print(",\"heartRateBpm\":");
    Serial.print(heartRate);
    Serial.print(",\"movementLevel\":\"");
    Serial.print(isMoving ? "ALTO" : "REPOUSO");
    Serial.print("\",\"needsPostOp\":");
    Serial.print(NEEDS_POST_OP_CARE ? "true" : "false");
    Serial.print(",\"riskScore\":");
    Serial.print(riskScore);
    Serial.print(",\"status\":\"");
    Serial.print(statusStr);
    Serial.println("\"}");
  }
}
