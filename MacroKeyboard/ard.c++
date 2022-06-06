#include "Keyboard.h"
#define BNum 10
int BPinA = 2;
int BPinB = 3;
int BPinC = 4;
int BPinD = 5;
int BPinE = 6;
int BPinF = 7;
int BPinG = 8;
int BPinH = 9;
int BPinI = 10;
int BPinJ = 11;

int BPins[BNum] = {BPinA, BPinB ,BPinC, BPinD, BPinE, BPinF, BPinG, BPinH, BPinI, BPinJ};
int strLen[BNum][10];
String strArr[BNum][10];
int strArrNum[BNum];

void setup() {
  for (int N=0; N<BNum; N++){
  strLen[N][0] = {-1};
  strArr[N][0] = {"032"};
  strArrNum[N] = 1;
  pinMode(BPins[N],INPUT_PULLUP);
  }
  Serial.begin(115200);
}

void loop(){
  if (Serial.available()){
    int BTN = Serial.read()-65;
    String ASCII = Serial.readStringUntil('\n');
    int indexNum=0;
    for (int i=1; i<10; i ++){
      int index = ASCII.indexOf("+",indexNum);
      if (index==-1){
        strLen[BTN][i]=ASCII.length();
        strArrNum[BTN] = i;
        break;
        }
      strLen[BTN][i] = index;
      indexNum = index+1;
      }
   delay(100);
   for (int j=0; j<strArrNum[BTN]; j++){
   strArr[BTN][j] = ASCII.substring(strLen[BTN][j]+1, strLen[BTN][j+1]);
   }
  }
   //KeyBotton('A');
  //KeyBotton('B');
  KeyBotton('C');
  //KeyBotton('D');
  //KeyBotton('E');
  //KeyBotton('F');
  //KeyBotton('G');
  //KeyBotton('H');
  //KeyBotton('I');
  //KeyBotton('J');
}

void KeyBotton(char Alphabet){
   int Num = Alphabet-65;
   if (digitalRead(BPins[Num])==HIGH){
     for (int i=0; i<strArrNum[Num]; i++){
     Keyboard.press(strArr[Num][i].toInt());
     }
     delay(100);
     Keyboard.releaseAll();
     unsigned long mp = millis();
     while(digitalRead(BPins[Num])==HIGH){
      unsigned long mc = millis();
      if (mc-mp>5000){
        Serial.println(Alphabet);
        while(digitalRead(BPins[Num])==HIGH){}
        break;
      }
    }
  }
}