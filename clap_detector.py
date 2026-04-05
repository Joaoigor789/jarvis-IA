import sounddevice as sd
import numpy as np
import time

THRESHOLD = 0.7
CLAPS_REQUIRED = 2

clap_count = 0
last_clap_time = 0

def detect_clap(indata, frames, time_info, status):
    global clap_count, last_clap_time

    volume_norm = np.linalg.norm(indata)
    current_time = time.time()

    # evita múltiplas leituras seguidas
    if volume_norm > THRESHOLD and (current_time - last_clap_time > 0.8):
        clap_count += 1
        last_clap_time = current_time
        print(f"👏 Palma detectada! ({clap_count})")

def listen_for_claps():
    global clap_count

    clap_count = 0

    print("Sistema de escuta ativo...")

    with sd.InputStream(callback=detect_clap):
        while clap_count < CLAPS_REQUIRED:
            sd.sleep(100)

    print("Jarvis ativado!")