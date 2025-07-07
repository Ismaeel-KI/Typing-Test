from tkinter import *
from sentence_pickup import random_pick
import time

random_text = random_pick()
text_to_display = random_text

user_line = ''
count = 0
errors = 0
start_time = None

def display_text(text_to_display):
    text_to_type.config(text= text_to_display)
    text_to_type.pack(pady=20)


def wpm_calculate():
    pass

def check_letters(sentence, original_text):
    global errors, typing_area

    errors = 0
    typing_area.tag_remove("wrong", "1.0", END)
    typing_area.tag_remove("correct", "1.0", END)


    result_frame = Frame(window, name="result_frame", bg="black")
    result_frame.pack(pady=10)

    result_display = Text(result_frame, height=1, font=("Helvetica", 14), bg="black", bd=0)
    result_display.tag_config("correct", foreground="green")
    result_display.tag_config("wrong", foreground="red")

    for i in range(len(sentence)):
        char = sentence[i]
        if i < len(original_text) and char == original_text[i]:
            result_display.insert(END, char, "correct")
        else:
            errors += 1
            result_display.insert(END, char, "wrong")

    result_display.config(state="disabled")
    result_display.pack(side='left', padx=20)

    error_label = Label(result_frame, text=f"Errors: {errors}", font=("Helvetica", 14), bg="black", fg="white")
    error_label.pack(side='left', padx=20)

    print("Errors:", errors)

def start_checking(event):
    global user_line, text_to_display, count, start_time

    if start_time is None:
        start_time = time.time()

    if time.time() - start_time >= 100000:
        print("Time's Up")
        print(user_line)
        check_letters(user_line, text_to_display)
        return

    if len(user_line) >= len(text_to_display):
        print('Sentence finished')
        print(user_line)
        check_letters(user_line, text_to_display)
        user_line = ''
        typing_area.delete('1.0', END)
        next_text = random_pick()
        while text_to_display == next_text:
            next_text = random_pick()
        text_to_display = next_text
        display_text(text_to_display)


    elif event.keysym == 'BackSpace':
        user_line = user_line[:-1]
        count -= 1

    elif len(event.char) == 1:
        user_line += event.char
        count += 1

def reset_text_area():
    global typing_area, user_line,start_time, count, errors

    typing_area.delete('1.0', END)
    user_line = ''
    start_time = None
    errors = 0
    count = 0


BG = 'light blue'
FG = 'white'

heading = "SPEED CHECK !"
instruction = "TEST STARTS WHEN YOU ENTER THE WORD"

window = Tk()

window.title('Type Writing Speed Test')
window.config(bg=BG)

heading_box = Label(window, text=heading, font=('Helvetica', 16), bg=BG , fg=FG)
instruction_box = Label(window, text=instruction, font=('Helvetica', 14), bg=BG ,fg=FG)

typing_area = Text(window, font=('arial', 14), bg='white', fg='black' ,wrap='w', padx=20, pady=5, highlightthickness=4)
typing_area.bind('<KeyPress>', start_checking)

reset_btn = Button(window, text='Reset', width=125, command= reset_text_area ,highlightthickness=1 , highlightcolor='black')

heading_box.pack(pady=23)
instruction_box.pack(pady=23)
text_to_type = Label(window, font=('Helvetica', 14), bg=BG, fg='blue')
display_text(text_to_display)
typing_area.pack()
reset_btn.pack(pady=23)

window.mainloop()