#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>

//Declaremos los pines CE y el CSN
#define CE_PIN 9
#define CSN_PIN 10 

//creamos el objeto radio (NRF24L01)
RF24 radio(CE_PIN, CSN_PIN);   // nRF24L01 (CE,CSN)rd

RF24Network network(radio);  // Network uses that radio

const uint16_t this_node = 01;   // Address of our node in Octal format
const uint16_t other_node = 00;  // Address of the other node in Octal format


const int ledPin = 8; // the pin that the LED is attached to

const int pinD0 = 0;
const int pinD1 = 1;
const int pinD2 = 2;
const int pinD3 = 3;
const int pinD4 = 4;
const int pinD5 = 5;
const int pinD6 = 6;
const int pinD7 = 7;



const int pinA1 = 1;
const int pinA2 = 2;
const int pinA3 = 3;
const int pinA4 = 4;
const int pinA5 = 5;
const int pinA0 = 0;



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
  network.begin( this_node);
  pinMode(ledPin,OUTPUT);
  pinMode(pinD0,OUTPUT);
  pinMode(pinD1,OUTPUT);
  pinMode(pinD2,OUTPUT);
  pinMode(pinD3,OUTPUT);
  pinMode(pinD4,OUTPUT);
  pinMode(pinD5,OUTPUT);
  pinMode(pinD6,OUTPUT);
  pinMode(pinD7,OUTPUT);
}

void loop() {

  network.update();  // Check the network regularly
  while (network.available()) {  // Is there anything ready for us?

    RF24NetworkHeader header;  // If so, grab it and print it out
    int command;
    network.read(header, &command, sizeof(command));
    Serial.print(F("command from nodo00 = "));
    Serial.print(command);
    Serial.println("");

    if (command == 0) {
      digitalWrite(ledPin, LOW);
    }
    if (command == 1) {
      digitalWrite(ledPin, HIGH);
    }

    if (command == 00) {
      digitalWrite(pinD0, LOW);
    }
    if (command == 01) {
      digitalWrite(pinD1, LOW);
    }
    if (command == 02) {
      digitalWrite(pinD2, LOW);
    }
    if (command == 03) {
      digitalWrite(pinD3, LOW);
    }
    if (command == 04) {
      digitalWrite(pinD4, LOW);
    }
    if (command == 05) {
      digitalWrite(pinD5, LOW);
    }
    if (command == 06) {
      digitalWrite(pinD6, LOW);
    }
    if (command == 07) {
      digitalWrite(pinD7, LOW);
    }
  

     if (command == 10) {
      digitalWrite(pinD0, HIGH);
    }
    if (command == 11) {
      digitalWrite(pinD1, HIGH);
    }
    if (command == 12) {
      digitalWrite(pinD2, HIGH);
    }
    if (command == 13) {
      digitalWrite(pinD3, HIGH);
    }
    if (command == 14) {
      digitalWrite(pinD4, HIGH);
    }
    if (command == 15) {
      digitalWrite(pinD5, HIGH);
    }
    if (command == 16) {
      digitalWrite(pinD6, HIGH);
    }
    if (command == 17) {
      digitalWrite(pinD7, HIGH);
    }
    
    if (command == 20) {
      sendDataHumedity(0);
    }
    
    
  }
  // If it's time to send a message, send it!  
  delay(100);
  
  while(contador == 100){
    sendDataHumedity(0);
    contador = 0;
  }
  contador = contador + 1;
}

void sendDataHumedity(int readData){
  Serial.print(F("Sending... "));
  double val;
  val = analogRead(readData);
  RF24NetworkHeader header(other_node);
  bool ok = network.write(header, &val, sizeof(val));
  Serial.println(ok ? F("ok.") : F("failed."));  
}

void sendDataLluvia(int readData){
  Serial.print(F("Sending... "));
  double val;
  val = analogRead(readData);
  RF24NetworkHeader header(other_node);
  bool ok = network.write(header, &val, sizeof(val));
  Serial.println(ok ? F("ok.") : F("failed."));  
}
