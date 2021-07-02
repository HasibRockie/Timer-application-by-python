from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
i = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    top_lebel["text"] = "Timer"
    bottom_lebel["text"] = ''
    global i
    i = 0
    button1["text"] = 'Start'

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_execution():
    global i
    i += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if i%2 != 0:
        top_lebel['text'] = "Work Time"
        countdown(work_sec)
        # time.sleep(work_sec)
    elif i==2 or i==4 or i==6:
        top_lebel['text'] = "Short Break Time"
        top_lebel['fg'] = RED
        countdown(short_break_sec)
        # time.sleep(short_break_sec)
    else:
        top_lebel['text'] = "Long Break Time"
        top_lebel['fg'] = PINK
        countdown(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # formatted = count * 60
    minute = count // 60
    second = count % 60

    if second < 10:
        second = f"0{second}"
    if minute <10:
        minute = f"0{minute}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        button1["text"] = "Running"
        timer = window.after(1000, countdown, count - 1)
    else:
        button1["text"] = "Start"
        count_execution()
        if i%2==0:
            bottom_lebel["text"] += "✔\n"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=20, bg=YELLOW)
window.title("POMODORO")

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, 'bold'), fill="white")
canvas.grid(row=1, column=1)

# countdown(10)

button1 = Button(text="Start", highlightthickness=0, command=count_execution)
button1.grid(row=2, column=0)

button2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(row=2, column=2)

top_lebel = Label(text="Timer", font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
top_lebel.grid(row=0, column=1)

bottom_lebel = Label(text='', font=(FONT_NAME, 18, 'bold'), bg=YELLOW, fg=GREEN)
bottom_lebel.grid(row=3, column=1)


window.mainloop()
