#include <HX711.h>
#define DOUT 3
#define CLK 2
#define Vcc 5v
HX711 scale;
float calibration_factor =199750; //201400,193500,197600, 206600; -7050 worked for 440lb max scale setup
void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);
  scale.set_scale();
  scale.tare(); //Reset the scale to 0

  long zero_factor = scale.read_average(); //Get a baseline reading
  
 
}

void loop() {
  scale.set_scale(calibration_factor); //Adjust to this calibration factor
  Serial.print(9.8* 0.453592 * scale.get_units() , 10);
  Serial.println();

 // if(Serial.available())
  //{
   // char temp = Serial.read();
    //if(temp == '+' || temp == 'a')
     // calibration_factor += 10;
    //else if(temp == '-' || temp == 'z')
     // calibration_factor -= 10;
  //}
}