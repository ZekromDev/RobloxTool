# pylint: disable=import-error
import tkinter as tk
from tkinter import ttk, simpledialog
import pyautogui
import threading
import time
from PIL import Image, ImageTk
import requests
from io import BytesIO
from webbrowser import open_new_tab
import getpass
import keyboard

class RobloxTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Roblox Tool github.com/ZekromDev")
        self.master.geometry("500x300")
        self.master.configure(bg='#007acc')

        username = getpass.getuser()
        print(f"Bonjour, {username}!")

        self.auto_click_btn = ttk.Button(self.master, text="Auto Click", command=self.auto_click, style='Black.TButton')
        self.auto_click_btn.pack(pady=10, ipadx=5, ipady=5)

        self.anti_afk_btn = ttk.Button(self.master, text="Anti AFK", command=self.anti_afk, style='Black.TButton')
        self.anti_afk_btn.pack(pady=10, ipadx=5, ipady=5)

        self.send_message_btn = ttk.Button(self.master, text="Send Message", command=self.send_message, style='Black.TButton')
        self.send_message_btn.pack(pady=10, ipadx=5, ipady=5)

        self.speed_advanced_btn = ttk.Button(self.master, text="Speed Advanced", command=self.speed_advanced, style='Black.TButton')
        self.speed_advanced_btn.pack(pady=10, ipadx=5, ipady=5)

        github_icon_url = "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
        github_icon = self.load_image_from_url(github_icon_url)
        github_icon = self.resize_image(github_icon, (9, 9))  # Redimensionne l'image

        github_button = ttk.Button(self.master, image=github_icon, command=self.open_github, style='IconButton.TButton')
        github_button.photo = github_icon
        github_button.pack(side='bottom', pady=10, ipadx=5, ipady=5)

        style = ttk.Style()
        style.configure('Black.TButton', foreground='black', background='#000000', width=15)
        style.configure('IconButton.TButton', background='#007acc')

        self.auto_click_active = False
        self.anti_afk_active = False
        self.speed_advanced_active = False

    def load_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img)
        return img

    def resize_image(self, img, size):
        img = img._PhotoImage__photo.subsample(size[0] // 10, size[1] // 10)  
        return img

    def open_github(self):
        open_new_tab("https://github.com/ZekromDev")

    def auto_click(self):
        self.auto_click_active = not self.auto_click_active

        def click():
            while self.auto_click_active:
                pyautogui.mouseDown()
                time.sleep(1)  
                pyautogui.mouseUp()

        auto_click_thread = threading.Thread(target=click)
        auto_click_thread.start()

    def anti_afk(self):
        self.anti_afk_active = not self.anti_afk_active

        def afk():
            keys = ['up', 'down', 'left', 'right']
            while self.anti_afk_active:
                for key in keys:
                    pyautogui.keyDown(key)
                    time.sleep(1) 
                    time.sleep(0.1)

        anti_afk_thread = threading.Thread(target=afk)
        anti_afk_thread.start()

    def speed_advanced(self):
        if not self.speed_advanced_active:
            self.speed_advanced_active = True
            pyautogui.keyDown('z')
            time.sleep(1)
        else:
            self.speed_advanced_active = False
            pyautogui.keyUp('z')
            time.sleep(1)

    def send_message(self):
        message = simpledialog.askstring("Send Message", "Quel message veux-tu envoyer?")
        if message:
            pyautogui.press('/')
            time.sleep(0.5)  
            pyautogui.typewrite(message)
            pyautogui.press('enter')
            print(f"Message envoyé par {getpass.getuser()}: {message}")

def main():
    root = tk.Tk()
    app = RobloxTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
