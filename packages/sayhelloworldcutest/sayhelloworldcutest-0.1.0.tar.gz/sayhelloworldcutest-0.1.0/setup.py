from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import platform
import subprocess

def detect_os():
    return platform.system().lower()

def open_terminal():
    os_name = detect_os()

    try:
        if os_name == "windows":
            subprocess.run(["cmd", "/k", "echo Hello, World!"])
        elif os_name == "linux":
            subprocess.run(["x-terminal-emulator", "-e", "echo Hello, World! && bash"])
        elif os_name == "darwin":  # MacOS
            subprocess.run(["osascript", "-e", 'tell application "Terminal" to do script \"echo Hello, World!\"'])
        else:
            print("no commend")
    except Exception as e:
        print(f"error: {e}")

# 설치 후 자동 실행
class PostInstallCommand(install):
    def run(self):
        install.run(self)  # 원래 설치 과정 실행
        open_terminal()  # 설치 후 터미널 실행

setup(
    name="sayhelloworldcutest",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    cmdclass={"install": PostInstallCommand},  # 설치 후 실행
)