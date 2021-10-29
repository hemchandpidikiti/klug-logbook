#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           
#define SS_PIN          10          

MFRC522 mfrc522(SS_PIN, RST_PIN);   


void setup() 
{
  Serial.begin(9600);    // Initialize serial
  SPI.begin();           // Init SPI bus
  mfrc522.PCD_Init();    // Init MFRC522 card
}

void loop() 
{
  
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
 
printDec(mfrc522.uid.uidByte, mfrc522.uid.size); //user Defined Function
delay(100);
}

void printDec(byte *buffer, byte bufferSize) 
{
  for (byte i = 0; i < bufferSize; i++) 
  {
    Serial.print(buffer[i] < 0x10 ? " 0" : "");
    Serial.print(buffer[i], DEC);
  }
  Serial.println();
}
