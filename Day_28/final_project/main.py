import tkinter as tk
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer = None
current_count = None
is_paused = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label["text"] = "Timer"
    check_mark["text"] = ""
    start_button["state"] = "active"
    pause_button["state"] = "disabled"
    global reps
    reps = 0
    global is_paused
    is_paused = False

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global is_paused
    if(is_paused):
        is_paused = False
        pause_button["state"] = "active"
        start_button["state"] = "disabled"
        count_down(current_count)
    else:
        global reps
        reps += 1

        start_button["state"] = "disabled"
        pause_button["state"] = "active"

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            timer_label["text"] = "Break"
            timer_label["fg"] = RED
        elif reps % 2 == 0  :
            count_down(short_break_sec)
            timer_label["text"] = "Break"
            timer_label["fg"] = PINK
        else:
            count_down(work_sec)
            timer_label["text"] = "Work"
            timer_label["fg"] = GREEN

# ---------------------------- PAUSE MECHANISM ------------------------------- # 
def pause_timer():
    global is_paused
    window.after_cancel(timer)
    is_paused = True
    pause_button["state"] = "disabled"
    start_button["state"] = "active"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = floor(count/60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    time = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        global timer
        global current_count
        current_count = count
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = floor(reps/2)
        for _ in range(work_session):
            marks += CHECKMARK
        check_mark["text"] = marks



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Timer label
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

#Tomato image
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#start button
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

#reset button
reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

#checkmark
check_mark = tk.Label(font=(FONT_NAME, 15),fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

#pause button
pause_button = tk.Button(text="Pause", highlightthickness=0, state="disabled", command=pause_timer)
pause_button.grid(row=4, column=1)

window.mainloop()