import sys
import os
import pyaudio
import numpy as np
import pyautogui
import time
import keyboard
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic

class SuppressAudio:
    CHUNK = 2**11
    RATE = 48016
    p = pyaudio.PyAudio()
    stream = None
    
    def start(self):
        def callback(in_data, frame_count, time_info, status):
            data = np.fromstring(in_data, dtype=np.int16)
            peak = np.average(np.abs(data))*2
            bars = 100*peak/2**16
            if bars > 1:
                pyautogui.keyDown("NUM0")
                print("Pressed 0")
            else:
                pyautogui.keyUp("NUM0")
                print("Released 0")
            return (data, pyaudio.paContinue)
        
        call.Display.setText("Started!")
        call.Display.setStyleSheet("background-color: red;")
        call.Display.setAlignment(QtCore.Qt.AlignCenter)
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.RATE, input=True,
                output=False, stream_callback=callback, frames_per_buffer=self.CHUNK)
        self.stream.start_stream()
    
    def stop(self):
        call.Display.setText("Not Started")
        call.Display.setStyleSheet("background-color: rgb(85, 255, 127);")
        call.Display.setAlignment(QtCore.Qt.AlignCenter)
        self.stream.stop_stream()
        pyautogui.keyUp("NUM0")
        print("Released 0")
    

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    call = uic.loadUi('gui.ui')

    sup_audio = SuppressAudio()

    call.Start.clicked.connect(sup_audio.start)
    call.Stop.clicked.connect(sup_audio.stop)

    call.show()
    app.exec()

# def suppress_func():
#     CHUNK = 2**11
#     RATE = 48016
#     bars = 0

#     p = pyaudio.PyAudio()

#     def callback(in_data, frame_count, time_info, status):
#         data = np.fromstring(in_data, dtype=np.int16)
#         peak = np.average(np.abs(data))*2
#         bars = 100*peak/2**16
#         if bars > 1:
#             pyautogui.keyDown("NUM0")
#             print('down')
#         else:
#             pyautogui.keyUp("NUM0")
#             print('up')
#         return (data, pyaudio.paContinue)


#     stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
#                 output=False, stream_callback=callback, frames_per_buffer=CHUNK)

#     stream.start_stream()
    
#     while stream.is_active():
#         if keyboard.is_pressed('q'):
#             break

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

# p=pyaudio.PyAudio()
# CHUNK = 2**11
# RATE = 48016
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
