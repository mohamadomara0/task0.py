from tkinter import *
from tkinter import ttk
import pyttsx3  


text_to_speech_engine = pyttsx3.init()


def play_text():
    user_text = text_enter.get()
    text_to_speech_engine.say(user_text)
    text_to_speech_engine.runAndWait()

def set_text():
    text_enter.delete(0, END)

def exit_app():
    root.destroy()

root = Tk()
root.title("Text To Speech")
root.geometry("500x400")

title_label = Label(
    root, 
    text="Text To Speech", 
    font="Tahoma 30 bold"
)


instruction_label = Label(
    root, 
    text="Enter Your Text", 
    font="Tahoma 15 bold", 
    pady=30
)


text_enter = Entry(
    root, 
    width=50
)


play_button = Button(
    root, 
    text="Play", 
    command=play_text, 
    bg="green", 
    fg="white", 
    font="Tahoma 12 bold"
)
set_button = Button(
    root, 
    text="Set", 
    command=set_text, 
    bg="blue", 
    fg="white", 
    font="Tahoma 12 bold"
)
exit_button = Button(
    root, 
    text="Exit", 
    command=exit_app, 
    bg="red", 
    fg="white", 
    font="Tahoma 12 bold"
)


title_label.pack()
instruction_label.pack()
text_enter.pack(pady=10)
play_button.pack(side=TOP, pady=15)
set_button.pack(side=TOP, pady=15)
exit_button.pack(side=TOP, pady=15)


root.mainloop()
