void setup() {
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps
}
void loop() {
  double val;
  val = analogRead(0); //connect sensor to Analog 0
  double porcentaje;
  double intervalo = 490 - 212;
  porcentaje = ((490 - val)/intervalo)*100;
  
  Serial.println(val); //print the value to serial port
  Serial.println("porcentaje:");
  Serial.println(porcentaje);
  delay(100);
}
