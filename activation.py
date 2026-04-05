from clap_detector import listen_for_claps
from voice_activation import listen_for_command
import threading

activated_event = threading.Event()

def ativar_por_palma():
    listen_for_claps()
    if not activated_event.is_set():
        print("Ativado por palma!")
        activated_event.set()

def ativar_por_voz():
    listen_for_command()
    if not activated_event.is_set():
        print("Ativado por voz!")
        activated_event.set()

def aguardar_ativacao():
    t1 = threading.Thread(target=ativar_por_palma, daemon=True)
    t2 = threading.Thread(target=ativar_por_voz, daemon=True)

    t1.start()
    t2.start()

    
    activated_event.wait()

    return True