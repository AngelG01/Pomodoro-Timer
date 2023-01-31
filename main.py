from tkinter import *
from math import floor

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


def reset_timer():
    global reps, WORK_MIN
    window.after_cancel(timer)
    title_label.config(text='Timer', fg=GREEN)
    WORK_MIN = 25
    canvas.itemconfig(timer_text, text=f'{WORK_MIN}:00')
    checkmark_label.config(text='')
    reps = 0


def add_checkmarks():
    mark = ''
    working_sessions = floor(reps / 2)
    for _ in range(working_sessions):
        mark += '✔'

    return mark


def start_timer():
    global reps
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text='Break!', fg=RED)
        reps = 0


    elif reps % 2 == 0:
        count_down(WORK_MIN * 60)
        title_label.config(text='Work!', fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text='Break!', fg=PINK)

    reps += 1


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min:02d}:{count_sec:02d}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark_label.config(text=add_checkmarks())


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(101, 112, image=tomato_image)
timer_text = canvas.create_text(102, 135, text=f'{WORK_MIN:02d}:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, 'bold'),
                      command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, 'bold'),
                      command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checkmark_label.grid(row=3, column=1)

window.mainloop()
