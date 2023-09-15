#include <Servo.h>
Servo servox;
char x = 1;
int xgo = 90;
void setup() {
  
 servox.attach(6);
 Serial.begin(9600);
 servox.write(90);
 
}

void loop() {
  
  if (Serial.available() > 0) {
    
    x = Serial.read();
    Serial.println(x);
    while(x == 76  || x == 82 && xgo >=0 && xgo <=180){
    if (Serial.available() > 0) {
    
    x = Serial.read();
    Serial.println(x);
    
    }
    
    if(x == 76){
      xgo = xgo - 1;
      
    }
    else if(x == 82){
      xgo = xgo + 1;
      
    }
    
    servox.write(xgo);    
    delay(40);
    
    }
    
    
    }
    


}
