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

  for(int i=0; i<=8; i++){
    pinMode(i, OUTPUT);
  }

}

void loop() {
  network.update();  // Check the network regularly
  while (network.available()) {  // Is there anything ready for us?
    RF24NetworkHeader header;  // If so, grab it and print it out
    
    int len = 0;  
    len = radio.getDynamicPayloadSize();
    Serial.println("len:" + String(len)); 
    char buf[len] = "";
    //radio.read(&gotmsg, len);
    network.read(header, &buf, len); //sizeof(data));
    
    //char myChar = 'char';
    String data = String(buf); 
    data.trim();                        // remove any \r \n whitespace at the end of the String
    
    Serial.println("node: " + String(header.from_node));
    Serial.println("data: " + String(data)); 
    
    /*
    float data;
    network.read(header, &data, sizeof(data));
    Serial.print(F("data nodo = "));
    Serial.println(header.from_node);
    Serial.print(F("humedad = "));
    Serial.println(data);   
    */
  }
  
  //------------------------------------------------------------
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    //while (Serial.available() == 0) {}     //wait for data available
    String input = Serial.readString();  //read until timeout
    input.trim();                        // remove any \r \n whitespace at the end of the String
    
    Serial.println(input);

    String nodo1 = getValue(input, "nodo");
    String pin1 = getValue(input, "pin");
    String command1 = getValue(input, "command");


    


    Serial.println("new: " + nodo1 + "," + pin1 + "," + command1);

    //String nodo = nodo1;
    //char buf[];
    //nodo1.toCharArray(buf, sizeof(nodo1));
    
    //char buf[2];
    //nodo1.toCharArray(buf, 2);
  
    //int nodo = nodo1.toInt(); //getValue(buf);
    String nodo = nodo1;
    String pin = pin1;
    String command = command1;

    
    
    /*
    DynamicJsonDocument doc(1024);
  
    deserializeJson(doc, input);
    JsonObject obj = doc.as<JsonObject>();
  
    // You can use a String to get an element of a JsonObject
    // No duplication is done.
    int nodo = obj[String("nodo")];
    String pin = obj[String("pin")];
    String command = obj[String("command")];
    */
    
    Serial.println("Nodo: " + String(nodo));
    Serial.println("Pin: " + pin);
    Serial.println("Command: " + command);
    
  
    String pin_type = pin.substring(0, 1);
    int pin_number = pin.substring(1).toInt();
  
    if (pin_type.equals("D")) {
      if (nodo == this_node){
        Serial.println("Command: " + command + ", " + String(pin_number));
        digitalWrite(pin_number, (command == "ON" ? HIGH : LOW));
      }
      else{
        sendData(nodo, (command == "ON" ? 1 : 0), input);
      }
    }
    
    if (pin_type == String("A")) {
      if (nodo == this_node){
        int value = analogRead(pin_number);
        Serial.println("Analog value: " + String(value));
      }
      else{
        sendData(nodo, 2, input);
      }
    }
  }
  //--- end Serial ---
}


String getValue(String input, String key){
  int p1 = input.indexOf(key);
  int p2 = input.indexOf(":", p1);
  int p3 = input.indexOf(",", p2);
  if (p3 < 0){
    p3 = input.indexOf("}", p2);  
  }
  
  String object = input.substring(p2+1, p3);
  object.replace("\"", "");

  return object;
}


//void sendData(uint16_t output_node, int command, String input){
void sendData(String node, int command, String input){

  String hexa = "0x" + node;
  // we use .c_str() to access the underlying C string
  int16_t output_node = strtol(hexa.c_str(), NULL, 0);
  //Serial.println(hexa);
  //Serial.print(node02);
  //Serial.print(" = ");
  Serial.println(output_node);
  
  /*
  uint16_t output_node;
  if (node == 1){
    output_node = node01;  
  }
  if (node == 2){
    output_node = node02;  
  }
  */
  
  RF24NetworkHeader header(output_node);
  //bool ok = network.write(header, &command, sizeof(command));
   

  //char hello[] = input;
  //https://forum.arduino.cc/t/nrf24l01-how-to-send-a-string-with-rf24-library/329672/4
  char hello[sizeof(input)];
  input.toCharArray(hello, strlen(hello));
  
  //radio.write(&hello,strlen(hello) );
  bool ok = network.write(header, &hello, sizeof(hello));
  
  Serial.println(ok ? F("ok.") : F("failed.")); 
    
}
