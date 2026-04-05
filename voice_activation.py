import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write
import tempfile

def gravar_audio(segundos=3, fs=44100):
    print(" Ouvindo...")

    audio = sd.rec(int(segundos * fs), samplerate=fs, channels=1)
    sd.wait()

    #  CONVERSÃO PARA PCM 16-BIT
    audio = (audio * 32767).astype(np.int16)

    return audio, fs

def listen_for_command():
    recognizer = sr.Recognizer()

    while True:
        try:
            audio_data, fs = gravar_audio()

            # salva temporariamente
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                write(f.name, fs, audio_data)
                caminho = f.name

            with sr.AudioFile(caminho) as source:
                audio = recognizer.record(source)

            comando = recognizer.recognize_google(audio, language="pt-BR")
            comando = comando.lower()

            print(f"Você disse: {comando}")

            if "jarvis" in comando and "iniciar" in comando:
                print("Comando reconhecido!")
                return True

        except sr.UnknownValueError:
            pass

        except Exception as e:
            print("Erro:", e)