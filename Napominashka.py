from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None

music = False # Переменная для отслеживания проигрывания музыки

def set():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ(24-часовой формат)")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t = dt.timestamp()
            print(t)
            label.config(text=f"Напоминание установлено на:{hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            show_info()
            t = None
    window.after(10000, check)


def show_info():
    global t
    window.attributes('-topmost', 1)  # Raising root above all other windows
    window.attributes('-topmost', 0)
    msg = "Уже пора спать"
    mb.showinfo("Информация", msg)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("OffSp.mp3")
    pygame.mixer.music.play()


def stop_music():
    global music
    if music: pygame.mixer.music.stop()
    music = False
    label.config(text="Установить новое напоминание")

window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=5)

check()

window.mainloop()
