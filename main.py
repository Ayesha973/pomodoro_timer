from data.db import init_db
from ui.layout import PomodoroUI
import tkinter as tk

def main():
    init_db()
    root = tk.Tk()
    app = PomodoroUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


