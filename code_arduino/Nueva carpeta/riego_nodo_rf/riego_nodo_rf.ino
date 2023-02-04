#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>
//#include <ArduinoJson.h>
#include <stdlib.h>


//Declaremos los pines CE y el CSN
#define CE_PIN 9
#define CSN_PIN 10

//creamos el objeto radio (NRF24L01)
RF24 radio(CE_PIN, CSN_PIN);   // nRF24L01 (CE,CSN)rd

RF24Network network(radio);  // Network uses that radio

const uint16_t this_node = 03;   // Address of our node in Octal format
const uint16_t base_node = 00;  // Address of the other node in Octal format

void setup() {
  //Serial.begin(9600);
  Serial.begin(115200);
  while (!Serial) {
    // some boards need this because of native USB capability
  }
  Serial.println(F("RF24Network/examples/helloworld_tx/"));

  if (!radio.begin()) {
    Serial.println(F("Radio hardware not responding!"));
    while (1) {
      // hold in infinite loop
    }
  }
  radio.setChannel(90);
  network.begin(/* node address*/ this_node);

  for (int i = 0; i <= 8; i++) {
    pinMode(i, OUTPUT);
  }

}

void loop() {
  network.update();  // Check the network regularly
  while (network.available()) {  // Is there anything ready for us?
    RF24NetworkHeader header;  // If so, grab it and print it out
    int len = 0;
    len = radio.getDynamicPayloadSize();
    char buf[64] = "";
    network.read(header, &buf, 64); //sizeof(data));

    String data = String(buf);
    data.trim();
    String response =  data;
    Serial.println(len);
    Serial.println(response);

    String nodo = getValue(response, "nodo");
    String pin = getValue(response, "pin");
    String command = getValue(response, "command");


    String pin_type = pin.substring(0, 1);
    int pin_number = pin.substring(1).toInt();

    if (pin_type.equals("D")) {
      Serial.println("Command: " + command + ", " + String(pin_number));
      digitalWrite(pin_number, (command == "ON" ? HIGH : LOW));
    }

    if (pin_type.equals("A")) {
      int value = analogRead(pin_number);
      Serial.println("Analog value: " + String(value));

      String response = "{'nodo':'" + String(this_node) + "'";
      response += ", 'pin':'" + pin + "'";
      response += ", 'value':" + String(value) + "}";

      sendData(response);
    }

  }
  // --- end while radio

}


String getValue(String input, String key) {
  int p1 = input.indexOf(key);
  int p2 = input.indexOf(":", p1);
  int p3 = input.indexOf(",", p2);
  if (p3 < 0) {
    p3 = input.indexOf("}", p2);
  }

  String object = input.substring(p2 + 1, p3);
  object.replace("\"", "");

  return object;
}


void sendData(String response) {
  RF24NetworkHeader header(base_node);

  int str_len = response.length() + 1;
  char message[str_len];
  response.toCharArray(message, str_len);
  bool ok = network.write(header, &message, strlen(message));
  Serial.println(message);
  Serial.println(ok ? F("ok.") : F("failed."));
}
