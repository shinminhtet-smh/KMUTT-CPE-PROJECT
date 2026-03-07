/*
  Water Level ALARM System (Passive Buzzer Fix)
  For High School Arduino Project
*/

int sensorPin = A0; 
int sensorValue = 0; 

// Define our output pins
int ledPin = 8;     
int buzzerPin = 9;  

void setup() {
  Serial.begin(9600);
  
  pinMode(ledPin, OUTPUT);    
  pinMode(buzzerPin, OUTPUT);
  
  Serial.println("Starting Water Alarm System...");
}

void loop() {
  sensorValue = analogRead(sensorPin);
  
  Serial.print("Sensor Value: ");
  Serial.print(sensorValue);
  
  if (sensorValue < 50) {
    Serial.println("  --> Status: Completely Dry");
    digitalWrite(ledPin, LOW);    // Turn LED OFF
    noTone(buzzerPin);            // Silence the buzzer
  } 
  else if (sensorValue >= 50 && sensorValue < 400) {
    Serial.println("  --> Status: Damp (Warning)");
    digitalWrite(ledPin, HIGH);   // Turn LED ON 
    noTone(buzzerPin);            // Keep buzzer quiet
  } 
  else {
    Serial.println("  --> Status: Very Wet (ALARM!)");
    digitalWrite(ledPin, HIGH);   // Keep LED ON
    tone(buzzerPin, 1000);        // Play a 1000 Hz alarm tone!
  }

  // Wait 1 second before taking the next reading
  delay(1000); 
}
