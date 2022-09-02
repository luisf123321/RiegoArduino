/*
  Arduino Wireless Network - Multiple NRF24L01 Tutorial
        == Node 02 (Child of Master node 00) ==
*/
/*
  Arduino Wireless Network - Multiple NRF24L01 Tutorial
        == Node 02 (Child of Master node 00) ==    
*/

#include <RF24Network.h>
#include <RF24.h>
#include <SPI.h>


//Declaremos los pines CE y el CSN
#define CE_PIN 9
#define CSN_PIN 10 

//creamos el objeto radio (NRF24L01)
RF24 radio(CE_PIN, CSN_PIN);   // nRF24L01 (CE,CSN)
RF24Network network(radio);      // Include the radio in the network
const uint16_t this_node = 02;   // Address of our node in Octal format ( 04,031, etc)
const uint16_t master00 = 00;    // Address of the other node in Octal format

#define led 13

void setup() {
  Serial.begin(9600);
  SPI.begin();
  radio.begin();
  network.begin(90, this_node);  //(channel, node address)
  radio.setDataRate(RF24_2MBPS);
}

void loop() {
  network.update();
  //===== Receiving =====//
  Serial.print( network.available());
  while ( network.available() ) {     // Is there any incoming data?
    RF24NetworkHeader header;
    unsigned long incomingData;
    network.read(header, &incomingData, sizeof(incomingData)); // Read the incoming data
    Serial.print(header.from_node);
    if (header.from_node == 0) {    // If data comes from Node 02
      if (incomingData == 10){
        digitalWrite(led, HIGH);  // Turn on or off the LED 02
      }
      if (incomingData == 20){
        digitalWrite(led, LOW);  // Turn on or off the LED 02
      }
    }
  }
  
  //===== Sending =====//
  unsigned long ledBrightness = 20;
  RF24NetworkHeader header(master00);   // (Address where the data is going)
  bool ok = network.write(header, &ledBrightness, sizeof(ledBrightness)); // Send the data
  Serial.print(ok);
  delay(5000);
    
 }
