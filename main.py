from PIL import Image, ImageGrab
import pyautogui, time

GROUND_OBSTACLE = [763, 390, 770, 395]


def key_press(key):
    pyautogui.keyDown(key)

def collision(data):
    for x in range(GROUND_OBSTACLE[0], GROUND_OBSTACLE[2]):
        for y in range(GROUND_OBSTACLE[1], GROUND_OBSTACLE[3]):
            if data[x, y] < 100:
                key_press("up")
                return
    

while True:
    image = ImageGrab.grab().convert('L')  
    data = image.load()
    collision(data)