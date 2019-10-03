const int trigPin = 2;  //D4
const int echoPin = 0;  //D3
long duration;
int distance;
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
}

void loop() {
  // put your main code here, to run repeatedly:
 digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
Serial.println("Distance: ");
Serial.print(distance);

delay(3000);
}
