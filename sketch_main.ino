int previousPin = -1; 

void setup() {
  Serial.begin(9600); 
  pinMode(14, OUTPUT);
  pinMode(15, OUTPUT);
  pinMode(16, OUTPUT);
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) { 
    int pinNumber = Serial.read(); 
    
    if (previousPin != -1) { 
      digitalWrite(previousPin, LOW); 
    }
    
    digitalWrite(pinNumber, HIGH); 
    Serial.println("LED turned on"); 
    previousPin = pinNumber; 
    delay(50); 
  }
}
