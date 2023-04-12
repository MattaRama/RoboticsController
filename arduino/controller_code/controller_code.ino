#include "Adafruit_LiquidCrystal.h"
#include <stdlib.h>

#define PACKET_LEN 256 

#define VAL_OFFSET 65

#define TYPE_PING VAL_OFFSET + 0 			// A
#define TYPE_SETCURSOR VAL_OFFSET + 1		// B
#define TYPE_PRINT VAL_OFFSET + 2			// C
#define TYPE_CLEAR VAL_OFFSET + 3			// D
#define TYPE_GETANALOG VAL_OFFSET + 4		// E
#define TYPE_GETDIGITAL VAL_OFFSET + 5		// F
#define TYPE_SETDIGITAL VAL_OFFSET + 6		// G
#define TYPE_SETPWM VAL_OFFSET + 7			// H

#define ANALOG_CHECK_COUNT 10
#define ANALOG_CHECK_DELAY 10

// pin definitions
int digitalPinOutputs[] = { 3, 5, 6, 7 };
int digitalPinInputs[] = { 2 };

// init displays
Adafruit_LiquidCrystal lcd1(0);

Adafruit_LiquidCrystal lcds[1] = {
  lcd1
};

struct Adafruit_LiquidCrystal getLCD(int i) {
  return lcds[i - VAL_OFFSET];
}

void readRequest(char* buff) {
  for (int i = 0; i < PACKET_LEN; i++) {
    while (Serial.available() == 0) {}
    char c = Serial.read();
    //Serial.print(c);
    buff[i] = c;
    if (c == ';') {
      //buff[i] = 0;
      break;
    }
  }
}

void setup()
{
  Serial.begin(9600);
  Serial.write("Begin;");
  
  // init digital inputs
  for (int i = 0; i < sizeof(digitalPinInputs) / sizeof(int); i++) {
    pinMode(digitalPinInputs[i], INPUT);
  }
  
  // init digital outputs
  for (int i = 0; i < sizeof(digitalPinOutputs) / sizeof(int); i++) {
    pinMode(digitalPinOutputs[i], OUTPUT);
  }
  
  // init liquidcrystals
  for (int i = 0; i < sizeof(lcds) / sizeof(Adafruit_LiquidCrystal); i++) {
    lcds[i].begin(16,2);
    lcds[i].setBacklight(HIGH);
    
    Serial.print("LCDInit ");
    Serial.print(i);
    Serial.print(";");
  }

  Serial.write("Init;");
}

void loop()
{
  char packet[PACKET_LEN];
  readRequest(packet);

  switch (packet[0]) {
    case TYPE_PING: {
      Serial.write("Pong;");
      break;
    }
    
    case TYPE_SETCURSOR: {
      Adafruit_LiquidCrystal lcd = getLCD(packet[1]);
	    lcd.setCursor(packet[2] - VAL_OFFSET, packet[3] - VAL_OFFSET);
      break;
    }
    
    case TYPE_PRINT: {
      Adafruit_LiquidCrystal lcd = getLCD(packet[1]);
      for (int i = 2; i < PACKET_LEN; i++) {
        if (packet[i] == ';') {
          break;
        }
        lcd.print(packet[i]);
      }

      break;
    }
    
    case TYPE_CLEAR: {
      Adafruit_LiquidCrystal lcd = getLCD(packet[1]);
      lcd.clear();
      break;
    }
    
    case TYPE_GETANALOG: {
      // get rolling average
      int analog = 0;
      for (int i = 0; i < ANALOG_CHECK_COUNT; i++) {
        analog += analogRead(packet[1] - VAL_OFFSET);
        delay(ANALOG_CHECK_DELAY);
      }

      analog /= ANALOG_CHECK_COUNT;
      Serial.write(TYPE_GETANALOG);
      Serial.print(analog);
      Serial.print(";");
      break;
    }
    
    case TYPE_GETDIGITAL: {
      bool digital = digitalRead(packet[1] - VAL_OFFSET);
      Serial.write(TYPE_GETDIGITAL);
      Serial.print(digital);
      Serial.print(";");
      break;
    }
    
    case TYPE_SETDIGITAL: {
      bool high = packet[2] == '1' ? true : false;
      digitalWrite(packet[1] - VAL_OFFSET, high);
      break;
    }
    
    case TYPE_SETPWM: {
      // construct string containing int
      char numStr[3];
      for (int i = 2; i < 5; i++) {
        if (packet[i] == ';') {
          break;
        }
        numStr[i - 2] = packet[i];
      }

      int pwmVal = atoi(numStr);
      analogWrite(packet[1] - VAL_OFFSET, pwmVal);
      break;
    }
  }

  // TODO: this should be removed once deployed
  //Serial.write("DONE;");
}