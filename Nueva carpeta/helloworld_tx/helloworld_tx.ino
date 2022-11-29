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

RF24 radio(8, 10);  // nRF24L01(+) radio attached using Getting Started board

RF24Network network(radio);  // Network uses that radio

const uint16_t this_node = 01;   // Address of our node in Octal format
const uint16_t other_node = 00;  // Address of the other node in Octal format

const unsigned long interval = 5000;  // How often (in ms) to send 'hello world' to the other unit

unsigned long last_sent;     // When did we last send?
unsigned long packets_sent;  // How many have we sent already

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
}

void loop() {

  network.update();  // Check the network regularly

  unsigned long now = millis();

  // If it's time to send a message, send it!
  if (now - last_sent >= interval) {
    last_sent = now;

    Serial.print(F("Sending... "));
    
    //radio.write(&hello,strlen(hello) );
    //char payload[512] = "{\"nodo\":02,\"pin\":\"D8\",\"command\":\"ON\"}";
    char payload[512] = "nodo 02";
    Serial.println(payload);
    
    RF24NetworkHeader header(/*to node*/ other_node);
    //bool ok = network.write(header, &payload, sizeof(payload));
    bool ok = network.write(header, &payload, strlen(payload));
    Serial.println(ok ? F("ok.") : F("failed."));
  }
}
