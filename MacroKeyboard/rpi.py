from pynput.keyboard import Key, Listener
import pandas as pd
from time import sleep
import serial

local = 'keyList.xlsx'
data = pd.read_excel(local, sheet_name="Sheet1", engine='openpyxl', index_col="button").astype(str)
s = serial.Serial('COM9', 115200)
print(data)
ASCIIs=[]

def keytoASCII(key):
    if len(str(key)) > 3:
        if key == Key.ctrl or key == Key.ctrl_l or key == Key.ctrl_r:
            key = '128'
        elif key == Key.shift or key == Key.shift_l or key == Key.shift_r:
            key = '129'
        elif key == Key.alt or key == Key.alt_l or key == Key.alt_r:
            key = '130'
        elif key == Key.tab:
            key = '179'
        elif key == Key.backspace:
            key = '178'
        elif key == Key.left:
            key = '216'
        elif key == Key.up:
            key = '218'
        elif key == Key.down:
            key = '217'
        elif key == Key.right:
            key = '215'
        elif key == Key.f1:
            key = '194'
        elif key == Key.f2:
            key = '195'
        elif key == Key.f3:
            key = '196'
        elif key == Key.f4:
            key = '197'
        elif key == Key.f5:
            key = '198'
        elif key == Key.f6:
            key = '199'
        elif key == Key.f7:
            key = '200'
        elif key == Key.f8:
            key = '201'
        elif key == Key.f9:
            key = '202'
        elif key == Key.f10:
            key = '203'
        elif key == Key.f11:
            key = '204'
        elif key == Key.f12:
            key = '205'
        elif key == Key.delete:
            key = '212'
        elif key == Key.end:
            key = '213'
        elif key == Key.page_down:
            key = '214'
        elif key == Key.page_up:
            key = '211'
        elif key == Key.home:
            key = '210'
        elif key == Key.insert:
            key = '209'
        elif key == Key.space:
            key = '032'
        elif key == Key.enter:
            key = 'mj'
        else:
            key ='0'   
    else : 
        key = str(ord(eval(str(key))))  
    key = key +','
    return key

def press(key):
    keyGet = keytoASCII(key)
    if keyGet=='mj,':
        return False
    else:
        ASCII = keyGet
        if ASCII in ASCIIs:
            pass
        else:
            ASCIIs.append(ASCII)
            if len(ASCIIs)>7:
                return False

def main():
    global ASCIIs
    dataVal = data['keyboard'].values.tolist()
    for i in range(10):
        setData = chr(65+i)+dataVal[i]
        s.write(setData.encode('utf-8'))
        sleep(1)

    while True:
        if s.readable():
            A = s.readline().decode().strip()
            print(A)
            ASCIIs=[]
            codes = ""
            codes += A
            with Listener(on_press=press) as listener:
                listener.join()
            for i in ASCIIs:
                codes += i
            data.at[codes[0:1],"keyboard"]=codes[1:-1]
            data.to_excel(local)
            serOut = codes[:-1]
            print(serOut)
            serOut = serOut.encode('utf-8')
            s.write(serOut)
            print(data)
            
if __name__ == "__main__":
    main()