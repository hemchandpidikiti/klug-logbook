#include <ESP8266WiFi.h>
#include <SPI.h>
#include <MFRC522.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h>
#define RST_PIN  D3           
#define SS_PIN  D8         

MFRC522 mfrc522(SS_PIN, RST_PIN);   
const int buzzer = D1;
String userid;
String payload;
HTTPClient http;  
void setup() 
{
  pinMode(buzzer, OUTPUT);
  WiFi.begin("wifi_ssid", "wifi_password");                   //WiFi connection
 ESP8266WebServer server(80);
  while (WiFi.status() != WL_CONNECTED) {                        //Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }
 
  Serial.begin(115200);  // Initialize serial
  SPI.begin();           // Init SPI bus
  mfrc522.PCD_Init();    // Init MFRC522 card
  mfrc522.PCD_DumpVersionToSerial();  // Show details of PCD - MFRC522 Card Reader details
  Serial.println(F("Scan your ID Card......................"));
  if (WiFi.status() == WL_CONNECTED) {
  http.begin("http://ip_address/auth/");
   
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");//Specify content-type header
    int httpCode = http.POST("username=xxxxx&password=xxxxx");
    
    Serial.print("http Status:\t");
    Serial.println(httpCode);                           //Print HTTP return code
    http.addHeader("Content-Type:","application/json");
    payload = http.getString();                  //Get the response payload
    Serial.print("authorization token:\t");
    Serial.println(payload);                            //Print request response payload

  http.end();
}
Serial.println(F("Scan your ID Card......................"));
}
void loop() 
{
  if (WiFi.status() == WL_CONNECTED) {                      //Check WiFi connection status
  //Serial.print("WIFI IP address: ");
  //Serial.println(WiFi.localIP()); 
  
  HTTPClient http;                    

  // Reset the loop, This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return ;
  }
 
 Serial.println("Scan card.............");
 printDec(mfrc522.uid.uidByte, mfrc522.uid.size);//user Defined Function
 //digitalWrite(buzzer,HIGH); // Send 1KHz sound signal...
// Allocate JsonBuffer
    // Use arduinojson.org/assistant to compute the capacity.
    const size_t capacity = JSON_OBJECT_SIZE(3) + JSON_ARRAY_SIZE(2) + 60;
    DynamicJsonBuffer jsonBuffer(capacity);
  
   // Parse JSON object
    JsonObject& root = jsonBuffer.parseObject(payload);
    if (!root.success()) {
      Serial.println(F("Parsing failed!"));
      return;
    }
 
    String root2=root["token"].as<char*>();
    String payload2="Token "+root2;
    
    
    http.begin("http://ip_address/api/master/mget/");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    http.addHeader("Authorization",payload2);
    int httpCode2 = http.POST("rfid_id="+userid);
    Serial.print("http status:\t");
    Serial.println(httpCode2);                           //Print HTTP return code
    http.addHeader("Content-Type:","application/json");
    String payload3 = http.getString();                  //Get the response payload
    Serial.print("attendance status:\t");
    Serial.println(payload3);                            //Print request response payload
    
    tone(buzzer,3000);
    delay(80);
    Serial.println("buzzer");
 //digitalWrite(buzzer,LOW);
    noTone(buzzer);
    delay(500);
    http.end();                                         //Close connection
    
    
                                          //Close connection
 } else {
 
    Serial.println("Error in WiFi connection");
 
  }

}

void printDec(byte *buffer, byte bufferSize) 
{
  Serial.print("rfid id:");
  userid="";
  for (byte i = 0; i < bufferSize; i++) 
  {
    
    Serial.print(buffer[i] < 0x10 ? "0" : "");
    Serial.print(buffer[i], DEC);
    userid += String(buffer[i] < 0x10 ? "0" : "");
    userid += String(buffer[i], DEC);
  }
  Serial.println();
  
}