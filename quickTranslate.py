import googletrans
import clipboard

import time

import win32gui
import win32con

# win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,500,200,0)

translator = googletrans.Translator()

origin = '---'
while(True):
	if origin != clipboard.paste():
		origin = clipboard.paste()
		results = translator.translate(origin,dest = 'zh-tw')
		print(results.text)
	time.sleep(1)
