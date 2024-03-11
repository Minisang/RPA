import pyautogui
import time
import pyperclip

#while True :
#    print(pyautogui.position())
#    time.sleep(0.1)

pyautogui.moveTo(142,185)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("부산 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

#이미지 캡쳐
start_x = 102
start_y = 101
end_x = 200
end_y = 300

pyautogui.screenshot(r'부산날씨3.png',region=(start_x, start_y, end_x,end_y))