import os
import subprocess
import sys
from pynput import keyboard

# ... (начало скрипта)

STEAM_PATH = r"C:\Program Files (x86)\Steam\steam.exe"

# Находим путь динамически через систему
LOCAL_APP_DATA = os.environ.get('LOCALAPPDATA') 
VSCODE_PATH = r"C:\Users\timof\AppData\Local\Programs\Microsoft VS Code\Code.exe"

APPS = {
    "steam": STEAM_PATH,
    "vscode": VSCODE_PATH
}

# ... (дальше проверка и остальной код)

print("=== ПРОВЕРКА ПУТЕЙ ===")
for app, path in APPS.items():
    if os.path.exists(path):
        print(f"✅ {app}: НАЙДЕН")
    else:
        print(f"❌ {app}: НЕ НАЙДЕН (проверь путь: {path})")
print("======================\n")

buffer = []

def launch(name):
    print(f"\n[!] Магия! Запускаю {name}...")
    try:
        subprocess.Popen(APPS[name])
    except Exception as e:
        print(f"Ошибка при запуске: {e}")

def on_press(key):
    global buffer
    try:
        if hasattr(key, 'char') and key.char:
            char = key.char.lower()
            buffer.append(char)
            if len(buffer) > 10: buffer.pop(0)
            
            combined = "".join(buffer)
            for app_name in APPS:
                if combined.endswith(app_name):
                    launch(app_name)
                    buffer.clear()
    except: pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()