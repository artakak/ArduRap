import serial
import subprocess

ser = serial.Serial('COM3', 9600)
prc = None
prc1 = None

while 1:
    message = str(ser.readline())
    if 'but1' in message:
        print('KUKU1')
        if not prc:
            prc = subprocess.Popen('notepad')
        else:
            prc.kill()
            prc = None
    if 'but2' in message:
        print('KUKU2')
        if not prc1:
            prc1 = subprocess.Popen('notepad')
        else:
            prc1.kill()
            prc1 = None