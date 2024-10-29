
#include <Servo.h>

Servo motor1;
Servo motor2;
Servo motor3;
Servo motor4;

void setup() {
  Serial.begin(9600);
  motor1.attach(9);
  motor2.attach(10);
  motor3.attach(11);
  motor4.attach(12);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readString();
    if (command.startsWith("takeoff")) {
      takeoff();
    } else if (command.startsWith("land")) {
      land();
    } else if (command.startsWith("adjust")) {
      adjust(command);
    }
  }
}

void takeoff() {
  motor1.write(1500); // Adjust speed for VTOL takeoff
  motor2.write(1500);
  motor3.write(1500);
  motor4.write(1500);
}

void land() {
  motor1.write(1000); // Lower speed for landing
  motor2.write(1000);
  motor3.write(1000);
  motor4.write(1000);
}

void adjust(String command) {
  // Basic parsing example, adjust as needed
  int motor = command.substring(7, 8).toInt();
  int speed = command.substring(9).toInt();
  switch (motor) {
    case 1: motor1.write(speed); break;
    case 2: motor2.write(speed); break;
    case 3: motor3.write(speed); break;
    case 4: motor4.write(speed); break;
  }
}
