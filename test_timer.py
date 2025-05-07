from logic.timer import PomodoroTimer

def done():
    print("Timer finished!")

timer = PomodoroTimer(5, done)  # 5 seconds
timer.start()
