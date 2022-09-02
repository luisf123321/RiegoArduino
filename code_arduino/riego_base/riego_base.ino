#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>
#include <ArduinoJson.h>

RF24 radio(9, 10);  // nRF24L01(+) radio attached using Getting Started board

RF24Network network(radio);         // Network uses that radio
const uint16_t this_node = 02;      // Address of our node in Octal format (04, 031, etc)
const uint16_t node01 = 00;         // Address of the node01 in Octal format

const int valvulePin = 8;
int incomingByte;                   // a variable to read incoming serial data into

void setup(void) {
  Serial.begin(115200);
  while (!Serial) {
    // some boards need this because of native USB capability
  }
  Serial.println(F("RF24Network/examples/helloworld_rx/"));

  if (!radio.begin()) {
    Serial.println(F("Radio hardware not responding!"));
    while (1) {
      // hold in infinite loop
    }
  }
  radio.setChannel(90);
  network.begin(this_node);

  pinMode(valvulePin, OUTPUT);
}

void loop(void) {

  DynamicJsonDocument doc(1024);

  doc["data"] = "data";
  String output;
  serializeJson(doc, output);
  Serial.println("info");
  Serial.println(output);
  delay(8000);
}
