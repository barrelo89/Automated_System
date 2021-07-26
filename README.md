# Automated System with Pytyon
This is the python script that automatically runs and  captures a series of keyword search in Chrome browser.

## Prerequisite
1. Python 3
2. The following packages are required to run: numpy cv2 selenium pyautogui
```
pip install numpy python-opencv pyautogui selenium
apt-get install python3-opencv
```
3. Run the following script
```
python3 auto_search.py
```

## How it works
1. First import all the required packages

```
import os #to create a base directory
import cv2 #to write a screen-capture into an image
import time #to hold the process for a pre-defined duration
import pyautogui #to screen-capture
import numpy as np #preprocess the screen-capture before writing it into an image

from selenium import webdriver #automatic browser control
from selenium.webdriver.chrome.options import Options #to give options to the automated browser control
from malicious_word import * #malicious keyword already defined in 'malicious_word.py'
```

2. Set the 'sleep' time for screen-capture \& Create a directory to have all the screen-captures
```
sleep_time = 0.5
save_base_path = 'imgs'
if not os.path.exists(save_base_path):
    os.makedirs(save_base_path)
```
```
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
```
