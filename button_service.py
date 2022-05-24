
from gpiozero import Button
from dotenv import load_dotenv
import datetime
import os
import requests


load_dotenv()
API_KEY = os.getenv('API_KEY')
LONG_PRESS_TIMEOUT = int(os.getenv('LONG_PRESS_TIMEOUT'))
LIGHT_BUTTON_GPIO = int(os.getenv('LIGHT_BUTTON_GPIO'))

time = {"last": datetime.datetime.now()}
long_click_timeout = LONG_PRESS_TIMEOUT

headers = {"X-Api-Key": API_KEY}


def long_click():
    os.system('sudo shutdown -h now')


def short_click():
    result = requests.get(
        'http://192.168.0.33:5000/plugin/enclosure/outputs/1',  headers=headers)

    result = requests.patch(
        'http://192.168.0.33:5000/plugin/enclosure/outputs/1', json={
            "status": not result.json()["current_value"]
        },  headers=headers)


def pressed():
    time["last"] = datetime.datetime.now()




def released():
    if ((datetime.datetime.now() - time["last"]).total_seconds() > long_click_timeout):
        long_click()
    else:
        short_click()


# Initialisierung von GPIO27 als Button (Eingang)
button = Button(LIGHT_BUTTON_GPIO)

# if button pressed 
button.when_pressed = pressed

# if button released  
button.when_released = released

while True:
    button.wait_for_press()
