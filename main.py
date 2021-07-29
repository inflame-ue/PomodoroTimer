from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# TIMER RESET
def reset_timer():
    global reps
    reps = 0

    # Reset all labels
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_start, text="00:00")
    check_mark_label.config(text="")

    # Enable start button
    start_button["state"] = "active"


# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1

    start_button["state"] = "disabled"
    start_button["disabledforeground"] = start_button["foreground"]
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # To the front when countdown is over:
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


# COUNTDOWN MECHANISM
def count_down(count):
    count_minutes = count // 60
    count_seconds = f"{count % 60:02d}"  # Show leading zeros.

    canvas.itemconfig(timer_start, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        marks = ""
        for mark in range(reps // 2):
            marks += "✔"
        check_mark_label.config(text=marks)


# UI SETUP
# Setup window:
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Setup canvas:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_start = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Setup the labels:
title_label = Label(text="Timer", width=11, font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.config(padx=20, pady=20)
title_label.grid(column=1, row=0)

check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.config(padx=20, pady=20)
check_mark_label.grid(column=1, row=3)

# Setup the buttons
start_button = Button(text="Start", width=5, height=1, command=start_timer)
start_button.config(padx=10, pady=10)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", width=5, height=1, command=reset_timer)
reset_button.config(padx=10, pady=10)
reset_button.grid(column=3, row=3)

# The end.
window.mainloop()
