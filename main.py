from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TICK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

phase = 0
time_started = False
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)

    top_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(time_canvas, text="00:00")
    tick_mark.config(text="")

    global phase, time_started
    phase = 0
    time_started = False


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer_once():
    global time_started

    if not time_started:
        start_timer()
        time_started = True


def start_timer():
    global phase

    phase += 1

    if phase % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        top_text.config(text="Break", fg=RED)
    elif phase % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        top_text.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        top_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    # format time to display in mins and seconds e.g. "04:22"

    minutes = count // 60
    seconds = count % 60

    # use dynamic typing to format time

    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(time_canvas, text=f"{minutes}:{seconds}")
    if count > 0:
        # assign window.after to variable to be able to stop the timer with reset
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if phase % 2 == 0:
            current_text = tick_mark.cget("text")
            tick_mark.config(text=current_text + TICK_MARK)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
time_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# labels
top_text = Label()

top_text.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
top_text.grid(column=1, row=0)

tick_mark = Label(bg=YELLOW, fg=GREEN)
tick_mark.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", activebackground=GREEN, bg="white", bd=0, font=(FONT_NAME, 10, "normal"))
start_button.config(command=start_timer_once)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", activebackground=GREEN, bg="white", bd=0, font=(FONT_NAME, 10, "normal"))
reset_button.config(command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
