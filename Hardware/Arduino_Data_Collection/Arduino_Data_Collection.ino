#include <Adafruit_INA219.h>
#include<Wire.h>

Adafruit_INA219 ina219_A;
Adafruit_INA219 ina219_B(0x41);


#include <HX711.h>
#define DOUT 3
#define CLK 2
#define Vcc 5v
HX711 scale;
float calibration_factor =199750; //201400,193500,197600, 206600; -7050 worked for 440lb max scale setup

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  scale.begin(DOUT, CLK);
  scale.set_scale();
  scale.tare(); //Reset the scale to 0
  long zero_factor = scale.read_average(); //Get a baseline reading
  uint32_t currentFrequency;
  ina219_A.begin();
  ina219_B.begin();

}
void loop() {
  // Scale Stuff
  //scale.set_scale(calibration_factor); //Adjust to this calibration factor
  // put your main code here, to run repeatedly:
  float shuntvoltage_A = 0;
  float busvoltage_A = 0;
  float current_mA_A = 0;
  float loadvoltage_A = 0;
  float shuntvoltage_B = 0;
  float busvoltage_B = 0;
  float current_mA_B = 0;
  float loadvoltage_B = 0;
  //shuntvoltage_A = ina219_A.getShuntVoltage_mV(); 
  //busvoltage_A = ina219_A.getBusVoltage_V();
  current_mA_A = ina219_A.getCurrent_mA();
  //loadvoltage_A = busvoltage_A + (shuntvoltage_A / 1000);
  //shuntvoltage_B = ina219_B.getShuntVoltage_mV(); 
  //busvoltage_B = ina219_B.getBusVoltage_V();
  current_mA_B = ina219_B.getCurrent_mA();
  //loadvoltage_B = busvoltage_B + (shuntvoltage_B / 1000);
  
  float force=9.8* 0.453592 * scale.get_units();
  Serial.print(current_mA_A);
  Serial.print(" ");
  Serial.print(current_mA_B);
  Serial.print(" ");
  Serial.print(force);
  Serial.println();
  
  //delay(.0001);
}
