from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("text to speech")
        self.geometry("350x300")
        self.configure(bg="white")

        self.msg_var = StringVar()

        self.create_widgets()

    def TextToSpeech(self):
        msg = self.text_field.get()
        speech = gTTS(text = msg)
        speech.save("test.mp3")
        playsound("test.mp3")
        os.remove("test.mp3")

    def Reset(self):
        self.msg_var.set("")

    def Exit(self):
        self.destroy()

    def create_widgets(self):
        window_title = Label(self, text = "Bryan's text to speech", font = "Helvetica 18")
        window_title.pack()

        textbox_label = Label (self, text = "Please enter text", font = "Helvetica 15")
        textbox_label.place(x = 20, y = 60)

        self.text_field = Entry(self, textvariable = self.msg_var, width = "50")
        self.text_field.place(x = 20, y = 100)

        read_button = Button(self, text = "read text", font = "Helvetica 15", command = self.TextToSpeech, width = "8")
        read_button.place(x = 25, y = 140)

        reset_button = Button(self, text = "reset", font = "Helvetica 15", command = self.Reset, width = "4")
        reset_button.place(x = 135, y = 140)

        exit_button = Button(self, text = "exit", font = "Helvetica 15", command = self.Exit, width = "4", bg = "red")
        exit_button.place(x = 200, y = 140)


if __name__ == "__main__":
    app = App()
    app.mainloop()