import tkinter as tk
from tkvideo import tkvideo
from logic.timer import PomodoroTimer

class PomodoroUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close) 

        self.video_label = tk.Label(root)
        self.video_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 32), bg="black", fg="white")
        self.timer_label.place(relx=0.5, rely=0.3, anchor="center")

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.place(relx=0.5, rely=0.7, anchor="center")
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.place(relx=0.3, rely=0.7, anchor="e")
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.place(relx=0.7, rely=0.7, anchor="w")

        
        self.timer = PomodoroTimer(25 * 60, self.timer_done)

    def start_timer(self):
        self.timer.start()
        self.player = tkvideo("assets/bg_vid.mp4", self.video_label, loop=1, size=(300, 200))
        self.player.play()

    def pause_timer(self):
        self.timer.pause()

    def reset_timer(self):
        self.timer.reset()

    def timer_done(self):
        print("You're out of time! I hope you finished what you were doing....or else O_o")
        self.timer_label.config(text="Done!")

    def on_close(self):
        print("Closing the app...")

        if hasattr(self, 'timer'):
            self.timer.pause()
            self.root.destroy()
