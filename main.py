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
CURRENT_STATE = {
    "Timer": GREEN,
    "Work": GREEN,
    "Break": RED,
}

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# labels
top_text = Label()

top_text.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
top_text.grid(column=1, row=0)

tick_mark = Label(text=TICK_MARK, bg=YELLOW, fg=GREEN)
tick_mark.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", activebackground=GREEN, bg="white", bd=0, font=(FONT_NAME, 10, "normal"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", activebackground=GREEN, bg="white", bd=0, font=(FONT_NAME, 10, "normal"))
reset_button.grid(column=2, row=2)

window.mainloop()
