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

const uint16_t this_node = 00;   // Address of our node in Octal format
const uint16_t node01 = 01;  // Address of the other node in Octal format
const uint16_t node02 = 02;  // Address of the other node in Octal format
const uint16_t node03 = 03;

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
    RF24NetworkHeader header;

    int len = 0;
    len = radio.getDynamicPayloadSize();
    char buf[64] = "";
    network.read(header, &buf, 64);

    //char myChar = 'char';
    String data = String(buf);
    data.trim();
    String response = data;

    Serial.println(response);
  }

  //------------------------------------------------------------
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    String request = Serial.readString();  //read until timeout
    request.trim();                        // remove any \r \n whitespace at the end of the String

    //Serial.println(request);

    String nodo = getValue(request, "nodo");
    String pin = getValue(request, "pin");
    String command = getValue(request, "command");

    //Serial.println("Nodo: " + nodo);
    //Serial.println("Pin: " + pin);
    //Serial.println("Command: " + command);


    String pin_type = pin.substring(0, 1);
    int pin_number = pin.substring(1).toInt();

    if (pin_type.equals("D")) {
      if (nodo.toInt() == this_node) {
        digitalWrite(pin_number, (command == "ON" ? HIGH : LOW));

        String response = "{\"type\":\"response\"";
        response += ", \"node\":\"" + String(this_node) + "\"";
        response += ", \"pin\":\"" + pin + "\"";
        response += ", \"command\":" + command;
        response += "}";

        Serial.println(response);
      }
      else {
        sendData(nodo, request);
      }
    }

    if (pin_type.equals("A")) {
      if (nodo.toInt() == this_node) {
        int value = analogRead(pin_number);

        String response = "{\"type\":\"response\"";
        response += ", \"node\":\"" + String(this_node) + "\"";
        response += ", \"pin\":\"" + pin + "\"";
        response += ", \"value\":" + String(value);
        response += "}";

        Serial.println(response);
      }
      else {
        sendData(nodo, request);
      }
    }
  }
  //--- end Serial ---
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


void sendData(String node, String request) {
  String hexa = "0x" + node;
  // we use .c_str() to access the underlying C string
  int16_t output_node = strtol(hexa.c_str(), NULL, 0);
  //Serial.println(output_node);

  //RF24NetworkHeader header(output_node);

  Serial.println(request);
  Serial.println(node);
  Serial.println(F("Sending... "));
  RF24NetworkHeader header( output_node);
  int str_len = request.length() + 1;
  char message[str_len];
  request.toCharArray(message, str_len);
  bool ok = network.write(header, &message, strlen(message));
  Serial.println(message);
  Serial.println(ok ? F("ok.") : F("failed."));

}
