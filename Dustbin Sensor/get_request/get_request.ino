//=============================================================================================Smart Waste Management System==================================================================================
//
//Team memebers:- 
//Ashesh Shrestha
//Wachas Arya
//Alaka Shrestha
//Sweta Singh
//===============================================================================================================================================================================================================

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
 
const char* ssid = "vianet_ashesh";
const char* password = "Pointbreak";

// defines pins numbers
const int trigPin = 2;  //D4
const int echoPin = 0;  //D3

// defines variables
long duration;
int distance,getdistance;

//Dustbin number

String dustbin_no="1";


void setup () {
 
Serial.begin(115200);
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
WiFi.begin(ssid, password);
 
while (WiFi.status() != WL_CONNECTED) {
 
delay(1000);
Serial.print("Connecting..");
 
}
 
}
 
void loop() {
if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
HTTPClient http;  //Declare an object of class HTTPClient
//===========================================================================================================================
 getdistance = depth();

//====================================================================================================
 
http.begin("http://192.168.1.11:8080/bin_update/"+dustbin_no+"/"+getdistance);  //Specify request destination
int httpCode = http.GET();                //Send the request
 
if (httpCode > 0) { //Check the returning code
 
String payload = http.getString();   //Get the request response payload
Serial.println(payload);                     //Print the response payload
 
}
 
http.end();   //Close connection
 
}
 
delay(3000);    //Send a request every 30 seconds
 
}

int depth()
{
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
//=======================
return(distance);
}

