#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>
#include <ArduinoJson.h>

RF24 radio(9, 10);  // nRF24L01(+) radio attached using Getting Started board

RF24Network network(radio);  // Network uses that radio

const uint16_t this_node = 02;        // Address of our node in Octal format
const uint16_t base_node = 00;        // Address of the other node in Octal format

const int valvulePin = 8;             // the pin that the LED is attached to
int incomingByte;                     // a variable to read incoming serial data into

void setup(void) {
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
  network.begin(this_node);

  pinMode(valvulePin, OUTPUT);
}

void loop() {

  network.update();  // Check the network regularly

  while (network.available()) {  // Is there anything ready for us?
    RF24NetworkHeader header;  // If so, grab it and print it out

    unsigned char input[1024];
    network.read(header, &input, sizeof(input));
    
    DynamicJsonDocument doc(1024);
    deserializeJson(doc, input);
    JsonObject obj = doc.as<JsonObject>();

    long node = obj[String("node")];
    long command = obj[String("command")];

    if (command == 0){
      digitalWrite(valvulePin, LOW);
    }
     if (command == 1){
      digitalWrite(valvulePin, HIGH);
    }
     if (command == 2){
      sendData();
    }
  } 

}

void sendData(){
  StaticJsonDocument<1024> doc;
  doc["node"] = this_node;
  doc["humidity"] = 34.76;
 
  char out[1024];
  int b = serializeJson(doc, out);
  Serial.print("publishing bytes = ");
  Serial.println(b, DEC);
  //boolean rc = mqttClient.publish("arduino-test", out);

  RF24NetworkHeader header(base_node);
  bool ok = network.write(header, &out, sizeof(out));
  Serial.println(ok ? F("ok.") : F("failed."));
}
