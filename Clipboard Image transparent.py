# Enter script code
import os
from PIL import ImageGrab

import pgi
pgi.require_version('Notify', '0.7')
from pgi.repository import Notify
Notify.init('Test Notify')

os.chdir("/home/franz/Bilder/convert")

def func():
    result = os.system("xclip -o -selection clipboard -t TARGETS | grep 'image'")
    if not result == 0:
        print("Der Clipboard-Inhalt ist ein Text.")
        notification = Notify.Notification.new("Script Fehlgeschlagen", "kein Bild in der Zwischenablage", "action-unavailable").show()
        return
    # Bild speichern
    img = ImageGrab.grabclipboard()
    img.save("from_clipboard.png", "PNG")

    os.system(f'convert from_clipboard.png -transparent white -quality 100 transparent.png')

    os.system(f'xclip -selection clipboard -t image/png -i transparent.png')

    # save chnaged image to clipboard

    Notify.Notification.new("Bild transparent", "die Druchführung des scripts war erfolgreich", "dialog-info").show()

func()
Notify.uninit()