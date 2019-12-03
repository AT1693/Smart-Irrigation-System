
const int sensor_pin = A0;  /* Soil moisture sensor O/P pin */
//#define IN1  8
//#define IN2  5
//#define IN3  11
//#define IN4  13
#include <Stepper.h>

const int stepsPerRevolution = 100;  // change this to fit the number of steps per revolution
// for your motor
Stepper myStepper(stepsPerRevolution, 8,5,11,13);
int Steps = 4096; //4096 or 768
int cstep = 0;

void setup() {
  Serial.begin(9600); /* Define baud rate for serial communication */
  //pinMode(IN1, OUTPUT); 
  //pinMode(IN2, OUTPUT); 
  //pinMode(IN3, OUTPUT); 
  //pinMode(IN4, OUTPUT); 
   // set the speed at 60 rpm:
    myStepper.setSpeed(200);
  // initialize the serial port:
    Serial.begin(9600);
}

void loop() {
  float moisture_percentage;
  int sensor_analog;
  sensor_analog = analogRead(sensor_pin);
  moisture_percentage = ( 100 - ( (sensor_analog/1023.00) * 100 ) );
 // Serial.print("Moisture Percentage = ");
  Serial.print(moisture_percentage);
  Serial.print("\n");
  if (moisture_percentage < 40.0)
  {
    // step one revolution  in one direction:
  Serial.println("clockwise");
  myStepper.step(stepsPerRevolution);
  //delay(500)
  }
 
  delay(1000);
}
