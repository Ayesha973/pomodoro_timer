# logic/timer.py
import threading
import time

class PomodoroTimer:
    def __init__(self, duration_seconds, on_finish_callback=None):
        self.duration = duration_seconds
        self.remaining = duration_seconds
        self.running = False
        self._thread = None
        self.on_finish = on_finish_callback

    def start(self):
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._run)
            self._thread.start()

    def _run(self):
        while self.running and self.remaining > 0:
            time.sleep(1)
            self.remaining -= 1
            print(f"Time left: {self.remaining}")  # Later: hook this to GUI
        if self.remaining == 0 and self.on_finish:
            self.on_finish()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.remaining = self.duration
