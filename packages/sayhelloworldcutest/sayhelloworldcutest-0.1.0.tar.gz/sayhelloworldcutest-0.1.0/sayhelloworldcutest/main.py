import os
import platform
import subprocess

def detect_os():
    os_name = platform.system()
    return os_name.lower()

def open_terminal():
    os_name = detect_os()

    try:
        if os_name == "windows":
            subprocess.run(["cmd", "/k", "echo Hello, World!"])
        elif os_name == "linux":
            subprocess.run(["x-terminal-emulator", "-e", "echo Hello, World! && bash"])
        elif os_name == "darwin":  # MacOS
            subprocess.run(["osascript", "-e", 'tell application "Terminal" to do script "echo Hello, World!"'])
        else:
            print("no comment")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    open_terminal()