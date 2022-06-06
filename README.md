#  Macro Keyboard
## 개요 
atmel chip 32u4 를 사용하는 아두이노 보드를 USB포트를 통해 PC와 연결해서 또 하나의 keyboard로 사용

## macrokeyboard architecture 
 1. PC UI 소프트웨어 - 사용자가 Macro key값을 정의하도록 해주는 S/W
 2. F/W on Arduino Micro - PC UI 소프트웨어와 통신하며 사용자 UI를 지원하는 기능 + Macro keyboard 값을 설정 하고 읽을수 있는 기능 ( read/write )
 3. hard coded : 변수값이 결정되어 있는 코드
    → 키 값에 대한 실제 보내는 키보드 값은 모두 hard coded 되어 있음
 
