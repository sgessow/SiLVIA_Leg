#include <Adafruit_INA219.h>
#include<Wire.h>

Adafruit_INA219 ina219_A;
Adafruit_INA219 ina219_B(0x41);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  uint32_t currentFrequency;
  ina219_A.begin();
  ina219_B.begin();

}

void loop() {
  // put your main code here, to run repeatedly:
  float shuntvoltage_A = 0;
  float busvoltage_A = 0;
  float current_mA_A = 0;
  float loadvoltage_A = 0;
  float shuntvoltage_B = 0;
  float busvoltage_B = 0;
  float current_mA_B = 0;
  float loadvoltage_B = 0;
  shuntvoltage_A = ina219_A.getShuntVoltage_mV(); 
  busvoltage_A = ina219_A.getBusVoltage_V();
  current_mA_A = ina219_A.getCurrent_mA();
  loadvoltage_A = busvoltage_A + (shuntvoltage_A / 1000);
  Serial.print("Current_A: "); 
  Serial.print(current_mA_A ); 
  Serial.println(" mA"); 
  shuntvoltage_B = ina219_B.getShuntVoltage_mV(); 
  busvoltage_B = ina219_B.getBusVoltage_V();
  current_mA_B = ina219_B.getCurrent_mA();
  loadvoltage_B = busvoltage_B + (shuntvoltage_B / 1000);
  Serial.print("Current_B: "); 
  Serial.print(current_mA_B); 
  Serial.println(" mA");  
  Serial.println("");
  delay(1000);

}
