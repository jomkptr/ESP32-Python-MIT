import network
import time
from machine import Pin

LED1 = Pin(25,Pin.OUT)
LED2 = Pin(26,Pin.OUT)
LED3 = Pin(27,Pin.OUT)
LED4 = Pin(21,Pin.OUT)
Buzzer = Pin(22,Pin.OUT)

print("Start Connection")
sta = network.WLAN(network.STA_IF)
sta.active(True)
wifiname = sta.scan()

for i in range(len(wifiname)):
    print(wifiname[i][0])
    
wifi_username = 'Appleroom1@SJTwifi'
wifi_password = 'apple420504'
print('connecting to:', wifi_username)

if not sta.isconnected():
    print('connecting to network ...')
    sta.connect(wifi_username,wifi_password)
    while not sta.connected():
        pass
    
print('Connection is:', sta.isconnected())
print('network config:', sta.ifconfig())

import socket
s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80)) #free server port
s.listen(5)
print('Socket established')

#to check if mit connect to socket
while(True):
    conn, addr = s.accept()
    time.sleep(0.5)
    print('APP connection success')
    
    request = conn.recv(1024)
    request = str(request)
    Data = []
    Data = request.split('/')
    
    if Data[1] == "on":
        print ("Operation is on.")
        LED1.on()
        time.sleep(0.5)
        LED1.off()
        time.sleep(0.5)
        LED2.on()
        time.sleep(0.5)
        LED2.off()
        time.sleep(0.5)
        LED3.on()
        time.sleep(0.5)
        LED3.off()
        time.sleep(0.5)
        LED4.on()
        time.sleep(0.5)
        LED4.off()
        time.sleep(0.5)
        Buzzer.on()
        time.sleep(1)
        Buzzer.off()
        time.sleep(0.5)
    else :
        print ("Opertaion is off.")
    
    time.sleep(0.5)
    conn.close