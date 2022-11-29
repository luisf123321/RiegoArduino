#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>

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
const uint16_t node04 = 04;
const uint16_t node05 = 05;
const uint16_t node06 = 06;
const uint16_t node07 = 07;



const int ledPin = 8; // the pin that the LED is attached to
int incomingByte;
int contador = 0;

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
  network.begin(/* node address*/ this_node);
  pinMode(ledPin, OUTPUT);
}

void loop() {

  network.update();  // Check the network regularly
  while (network.available()) {  // Is there anything ready for us?

    RF24NetworkHeader header;  // If so, grab it and print it out
    //float data;
    int len=0;
    char gotmsg[]="";
          
    len = radio.getDynamicPayloadSize();
    radio.read( &gotmsg, len );
    len = radio.getDynamicPayloadSize();
    Serial.println(gotmsg);
    network.read(header, &data, sizeof(data));
    Serial.print(F("data nodo = "));
    Serial.println(header.from_node);
    Serial.print(F("humedad = "));
    Serial.println(data);   
  }

  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    
    if (incomingByte == 'A') {
      digitalWrite(ledPin, LOW);
    }
    if (incomingByte == 'B') {
      digitalWrite(ledPin, HIGH);
    }
    if (incomingByte == 'C') {
      float humedad = 34.76;
      Serial.println(humedad);
    }

    
    if (incomingByte == 'D') {
      sendData(1, 0);
    }
    if (incomingByte == 'E') {
      sendData(1, 1);
    }
    if (incomingByte == 'F') {
      sendData(1, 2);
    }


    if (incomingByte == 'G') {
      sendData(2, 0);
    }
    if (incomingByte == 'H') {
      sendData(2, 1);
    }
    if (incomingByte == 'I') {
      sendData(2, 2);
    }
  }

  
  //unsigned long now = millis();
  // If it's time to send a message, send it!  
  delay(100);
  
  if(contador >= 100){
    int command = 2;

    Serial.print(F("Sending... node01 "));
    Serial.println(command);
    RF24NetworkHeader header1(node01);
    bool ok1 = network.write(header1, &command, sizeof(command));
    Serial.println(ok1 ? F("ok1.") : F("failed1."));

    delay(1000);
    
    Serial.print(F("Sending... nocde02 "));
    Serial.println(command);
    RF24NetworkHeader header2(node02);
    bool ok2 = network.write(header2, &command, sizeof(command));
    Serial.println(ok2 ? F("ok2.") : F("failed2."));
    
    contador = 0;
  }
  contador = contador + 1;
}

void sendData(int node, int command){
  uint16_t output_node;
  
  if (node == 1){
    output_node = node01;  
  }
  if (node == 2){
    output_node = node02;  
  }
  
  RF24NetworkHeader header(output_node);
  bool ok = network.write(header, &command, sizeof(command));
  Serial.println(ok ? F("ok.") : F("failed."));
    
}
