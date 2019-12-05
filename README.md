# Smart-Irrigation-System

Connect the gnd of Soil sensor with gnd of Arduino.
Connect Vcc with 5v of Arduino.
Connect A0 with an analog pin(A0 here) of arduino here, if you need the value, else you may use the digital pin
Connect your ardino board with usb port of pi.
Install Arduino on your pi and compile the arduinofinal file.
The four motor pins are only for testing purpose in case you want to run a pump or motor if the water level falls below 40%(or any pre-defined value you wish to set. Just be sure to make changes in both the seria_port.py and the arduino file for the value).

For visual results, connect the four pins of stepper motor as in the code.





Select the board and port from Arduino.
Upload arduino code from Arduino.
Open seria_port.py on pi.
Fill in the parameters from way2sms for sms utility.

Run seria_test.py.

Dip your soil sensor(the two stick needle-like part) in the soil and test it for various moisture levels.)



The current system works for one soil sensor which will send you sms if the moisture level detected is less than 40%(or a set value by you). You may connect multiple soil sensors, each planted at a distance from each other and make this an overall system for detection. You may name each soil sensor wrt pins and send an sms accordingly.

The system may be expanded to one with multiple Pi(s) as well for a bigger garden. The accuracy of the soil sensor is moderately dependable.

Finally, you may connect a pump and irrigate the needed areas manually or autonomously through a motor driver,


