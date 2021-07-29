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

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    start_button["state"] = "disabled"
    start_button["disabledforeground"] = start_button["foreground"]
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(work_sec)
        reps += 1
        title_label.config(text="Work", fg=GREEN)
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(short_break_sec)
        reps += 1
        title_label.config(text="Short Break", fg=PINK)
    elif reps == 7:
        count_down(long_break_sec)
        reps = 0
        title_label.config(text="Long Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = count // 60
    count_seconds = f"{count % 60:02d}"  # Show leading zeros.

    canvas.itemconfig(timer, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Setup window:
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, )

# Setup canvas:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Setup the labels:
title_label = Label(text="Timer", width=11 ,font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.config(padx=20, pady=20)
title_label.grid(column=1, row=0)

check_mark_label = Label(text=" ✔", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.config(padx=20, pady=20)
check_mark_label.grid(column=1, row=3)

# Setup the buttons
start_button = Button(text="Start", width=5, height=1, command=start_timer)
start_button.config(padx=10, pady=10)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", width=5, height=1)
reset_button.config(padx=10, pady=10)
reset_button.grid(column=3, row=3)

# The end.
window.mainloop()
