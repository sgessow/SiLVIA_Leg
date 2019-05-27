double fsrData;
double Rfsr;
double FORCE;
double FORCE1;
double fsrPin = A0;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  fsrData = analogRead(fsrPin);
  Rfsr = 10 * (5/(fsrData/1024*5)-1);
  FORCE1=pow((2.332-(log10(Rfsr))*0.744),10);
  FORCE = FORCE1/1000*9.8;
  Serial.println("FORCE=");
  Serial.println(FORCE);
  //delay (500);
  // put your main code here, to run repeatedly:

}
