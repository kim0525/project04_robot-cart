#include "DualMC33926MotorShield.h"
 
DualMC33926MotorShield md;
 int pwm = 100;
 void forward(void);
 void brake(void);
 void backward(void);
 void turnleft(void);
 void turnright(void);
 
void setup()
{
  Serial.begin(9600);
  Serial.println("Dual MC33926 Motor Shield");
  md.init();
  {
    forward();
    delay(3000);
    brake();
    turnleft();
    delay(3000);
    brake();
    backward();
    delay(3000);
    brake();
    turnright();
    delay(3000);
    brake();
  }
}    
void loop(){
/* 
  if(Serial.available()>0){
    char ch = Serial.read();
    if(ch== 'w'){
      forward();
    }
    else if(ch== 's'){
      backward();
    }
    else if(ch== 'a'){
      rotate_left();
    }
    }
    
  } 
*/
}
 void forward(){
    md.setM1Speed(pwm);
    md.setM2Speed(-pwm);
 }
 void backward(){
    md.setM1Speed(-pwm);
    md.setM2Speed(pwm);
 }
  void brake(){
    md.setM1Speed(0); md.setM2Speed(0);
 }
  void turnleft(){
    md.setM1Speed(pwm-7.5);
    md.setM2Speed(pwm-7.5);
  }
  void turnright(){
    md.setM1Speed(-(pwm-7.5));
    md.setM2Speed(-(pwm-7.5));
  }
 
