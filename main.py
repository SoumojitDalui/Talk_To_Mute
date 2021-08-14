import sys
import os
import pyaudio
import numpy as np
import pyautogui
import time
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
    
if __name__=='__main__':
    app = QApplication(sys.argv)

    main = MainApp()
    main.show()

    try:
        sys.exit(main.exec_())
    except SystemExit:
        print("Closing Window...")

def suppress_func():
    CHUNK = 2**11
    RATE = 48016
    bars = 0

    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        # print("I am called")
        data = np.fromstring(in_data, dtype=np.int16)
        peak = np.average(np.abs(data))*2
        bars = 100*peak/2**16
        if bars > 1:
            pyautogui.keyDown("NUM0")
            print('down')
        else:
            pyautogui.keyUp("NUM0")
            print('up')
        return (data, pyaudio.paContinue)


    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                output=False, stream_callback=callback, frames_per_buffer=CHUNK)

    stream.start_stream()
    
    while stream.is_active():
        if keyboard.is_pressed('q'):
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

# p=pyaudio.PyAudio()
# stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
#               frames_per_buffer=CHUNK)

# start = time.time()

# try:
#     while 1:
#         data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
#         peak=np.average(np.abs(data))*2
#         bars=100*peak/2**16
#         if bars>1:
#             pyautogui.keyDown("NUM0")
#             start = time.time()
#             print('down')

#         else:
#             pyautogui.keyUp("NUM0")
#             print('up')
#             if time.time() - start > 5:
#                 stream.stop_stream()
#                 stream.close()
#                 p.terminate()
#                 break

# except KeyboardInterrupt:
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#     print('Interrupted')
#     time.sleep(3)
#     clear = lambda: os.system('cls')
#     clear()
#     clear()
