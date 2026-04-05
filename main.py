from voice_activation import listen_for_command
from activation import aguardar_ativacao
from playsound import playsound
import webbrowser
from flask import Flask, render_template
import threading
import pyttsx3
import queue


engine = pyttsx3.init()


voices = engine.getProperty('voices')

for voice in voices:
    if "david" in voice.name.lower() or "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)

# fila de fala (evita erro de thread)
fala_fila = queue.Queue()

def loop_fala():
    while True:
        texto = fala_fila.get()
        if texto is None:
            break
        engine.say(texto)
        engine.runAndWait()
        fala_fila.task_done()

threading.Thread(target=loop_fala, daemon=True).start()

def falar(texto):
    fala_fila.put(texto)


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template("index.html")

def start_server():
    app.run(port=5000)


def play_music():
    threading.Thread(target=lambda: playsound("back.mp3")).start()


if __name__ == "__main__":
    print("Iniciando Jarvis...")

    falar("Olá, senhor. Eu sou o Jarvis. Bata duas palmas ou diga Jarvis iniciar para ativar.")
    
    print("Aguardando palma OU comando de voz...")
    aguardar_ativacao()

    print("Jarvis ativado!")

    falar("Ativando sistema.")

    play_music()

    webbrowser.open("http://127.0.0.1:5000")

    start_server()