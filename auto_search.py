import os
import cv2
import time
import pyautogui
import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from malicious_word import * #malicious keyword already defined in 'malicious_word.py'

sleep_time = 0.5
save_base_path = 'imgs'
if not os.path.exists(save_base_path):
    os.makedirs(save_base_path)

options = Options()
options.add_argument("--start-maximized")

chrome_path = r'/home/c405/Desktop/DUIN/Conatix/OCR/chromedriver'
browser = webdriver.Chrome(chrome_options=options, executable_path=chrome_path)

for key in data:

    malicious_word = data[key]

    search_string = malicious_word.replace(' ', '+')

    # Assigning the browser variable with chromedriver of Chrome.
    # Any other browser and its respective webdriver
    # like geckodriver for Mozilla Firefox can be used


    for i in range(1):
        matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
    time.sleep(sleep_time)

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    cv2.imwrite(os.path.join(save_base_path, malicious_word + '.png'), image)





















































#end
