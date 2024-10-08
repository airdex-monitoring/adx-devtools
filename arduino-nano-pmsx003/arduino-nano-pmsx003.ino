#include <PMserial.h>
SerialPM pms(PMSx003, 10, 11);  // PMSx003, RX, TX

void setup() {
  Serial.begin(9600);
  pms.init();
}

void loop() {
  pms.read();

  if (pms) {
    Serial.print(F("{"));
    Serial.print(F("\"pm_1_0\": ")); Serial.print(pms.pm01); Serial.print(F(", "));
    Serial.print(F("\"pm_2_5\": ")); Serial.print(pms.pm25); Serial.print(F(", "));
    Serial.print(F("\"pm_10\": ")); Serial.print(pms.pm10);
    Serial.println(F("}"));
  } else {
    Serial.println("Error reading sensor data.");
  }

  delay(1000);
}