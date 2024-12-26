import time
from tkinter import Tk, Label, Button, StringVar

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.work_duration = 25 * 60  # 25 minutes
        self.break_duration = 5 * 60  # 5 minutes
        self.timer_running = False
        self.remaining_time = self.work_duration

        self.timer_label = Label(root, text="Pomodoro Timer", font=("Helvetica", 20))
        self.timer_label.pack(pady=10)

        self.time_var = StringVar()
        self.time_var.set(self.format_time(self.remaining_time))
        self.time_display = Label(root, textvariable=self.time_var, font=("Helvetica", 36))
        self.time_display.pack(pady=20)

        self.start_button = Button(root, text="Start", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(side="left", padx=20, pady=20)

        self.pause_button = Button(root, text="Pause", command=self.pause_timer, font=("Helvetica", 14))
        self.pause_button.pack(side="left", padx=20, pady=20)

        self.reset_button = Button(root, text="Reset", command=self.reset_timer, font=("Helvetica", 14))
        self.reset_button.pack(side="left", padx=20, pady=20)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.remaining_time = self.work_duration
        self.time_var.set(self.format_time(self.remaining_time))

    def countdown(self):
        if self.timer_running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.time_var.set(self.format_time(self.remaining_time))
            self.root.after(1000, self.countdown)
        elif self.remaining_time == 0:
            self.timer_running = False
            self.notify()

    def notify(self):
        self.timer_label.config(text="Time's up! Take a break!")
        self.remaining_time = self.break_duration
        self.timer_running = True
        self.countdown()

if __name__ == "__main__":
    root = Tk()
    app = PomodoroTimer(root)
    root.mainloop()
