/**
 * Swarm simulation in Arduino Uno.
 */
#include <SoftwareSerial.h>

SoftwareSerial unoSerial(4, 5); // rx, tx

void setup() {
  // setup serial port
  Serial.begin(115200);

  while (!Serial) {
  }

  // setup serial pin
  unoSerial.begin(115200);
}

void loop() {
  if (unoSerial.available() > 0) {
    Serial.println(unoSerial.readString());
  }
}
