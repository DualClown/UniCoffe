#include <Servo.h>

Servo servo1;
int input = 0;

void setup() {
        servo1.attach(13);
        Serial.begin(9600);
}

void loop() {
        servo1.write(0);
        if ( Serial.available() > 0 ) {

                input = Serial.read();
                if ( input == 48) {
                        servo1.write(180);
                        delay(500);
                        servo1.write(0);
                        delay(500);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(500);
                        servo1.write(0);
                        delay(500);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(100);
                        servo1.write(0);
                        delay(100);
                        servo1.write(180);
                        delay(500);
                        servo1.write(0);
                        delay(500);


                        Serial.println(input);
                        delay(1000);
                }
        }
}
