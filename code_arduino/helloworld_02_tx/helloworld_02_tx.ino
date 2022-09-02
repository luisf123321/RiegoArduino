/**
 * Copyright (C) 2012 James Coliz, Jr. <maniacbug@ymail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * version 2 as published by the Free Software Foundation.
 *
 * Update 2014 - TMRh20
 */

/**
 * Simplest possible example of using RF24Network
 *
 * TRANSMITTER NODE
 * Every 2 seconds, send a payload to the receiver node.
 */

#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>

//Declaremos los pines CE y el CSN
#define CE_PIN 9
#define CSN_PIN 10 

//creamos el objeto radio (NRF24L01)
RF24 radio(CE_PIN, CSN_PIN);   // nRF24L01 (CE,CSN)rd

RF24Network network(radio);  // Network uses that radio

const uint16_t this_node = 02;   // Address of our node in Octal format
const uint16_t other_node = 00;  // Address of the other node in Octal format


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
  network.begin(/*node address*/ this_node);
  pinMode(ledPin, OUTPUT);
}

void loop() {

  network.update();  // Check the network regularly
  while (network.available()) {  // Is there anything ready for us?

    RF24NetworkHeader header;  // If so, grab it and print it out
    unsigned long  data;
    network.read(header, &data, sizeof(data));
    Serial.print(F("data nodo00 = "));
    Serial.print(data);
    Serial.println("");
    if (data == 1) {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (data == 0) {
      digitalWrite(ledPin, LOW);
    }
    
  }

  unsigned long now = millis();

  // If it's time to send a message, send it!  
  delay(100);
  while(contador == 50){
    Serial.print(F("Sending... "));
    float dataSend = 32.5;
    RF24NetworkHeader header(other_node);
    bool ok = network.write(header, &dataSend, sizeof(dataSend));
    Serial.println(ok ? F("ok.") : F("failed."));
    contador = 0;
  }
  contador = contador + 1;
}
