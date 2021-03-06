#include <Adafruit_INA219.h>
#include<Wire.h>

Adafruit_INA219 ina219_A;
Adafruit_INA219 ina219_B(0x41);


#include <HX711.h>
#define DOUT 3
#define CLK 2
#define Vcc 5v
HX711 scale;

// Loop Timing
//int start_time=millis();
//int end_time=start_time;

int count=0;
float calibration_factor =199750; //201400,193500,197600, 206600; -7050 worked for 440lb max scale setup
float force=0;
float shuntvoltage_A = 0;
float busvoltage_A = 0;
float current_mA_A = 0;
float loadvoltage_A = 0;
float shuntvoltage_B = 0;
float busvoltage_B = 0;
float current_mA_B = 0;
float loadvoltage_B = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor); //Adjust to this calibration factor
  scale.tare();
  uint32_t currentFrequency;
  ina219_A.begin();
  ina219_B.begin();
  force=(9.8* 0.453592 )*((scale.read()-scale.get_offset())/scale.get_scale());
  // Loop Timing
  //start_time=millis();
}


void loop() {
  // Loop Timing
  //if (count==100){
   // end_time=millis();
  //  Serial.println("HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEEEE");
  //  Serial.println(end_time-start_time);
  //  }

  shuntvoltage_A = ina219_A.getShuntVoltage_mV(); 
  busvoltage_A = ina219_A.getBusVoltage_V();
  current_mA_A = -1*ina219_A.getCurrent_mA();
  loadvoltage_A = busvoltage_A + (shuntvoltage_A / 1000);
  shuntvoltage_B = ina219_B.getShuntVoltage_mV(); 
  busvoltage_B = ina219_B.getBusVoltage_V();
  current_mA_B = 1*ina219_B.getCurrent_mA();
  loadvoltage_B = busvoltage_B + (shuntvoltage_B / 1000);
  if (count % 5==0){
    force=(9.8* 0.453592 )*((scale.read()-scale.get_offset())/scale.get_scale());
    count=0;
  }
  Serial.print(current_mA_A);
  Serial.print(" ");
  Serial.print(current_mA_B);
  Serial.print(" ");
  Serial.print(loadvoltage_A);
  Serial.print(" ");
  Serial.print(loadvoltage_B);
  Serial.print(" ");
  Serial.print(force);
  Serial.println();

  count++;
}
