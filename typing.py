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

def check_letters(sentence, orginal_text):
    global errors, user_line, typing_area

    errors = 0  # Reset error count every check
    typing_area.tag_remove("wrong", "1.0", END)
    typing_area.tag_remove("correct", "1.0", END)

    for i in range(min(len(sentence), len(orginal_text))):
        index = f"1.{i}"
        next_index = f"1.{i + 1}"

        if sentence[i] == orginal_text[i]:
            typing_area.tag_add("correct", index, next_index)
        else:
            errors += 1
            typing_area.delete(index, next_index)
            typing_area.insert(index, sentence[i])
            typing_area.tag_add("wrong", index, f"1.{i + 1}")

    typing_area.tag_config("correct", foreground="green")
    typing_area.tag_config("wrong", foreground="red")
    print("Errors:", errors)

def start_checking(event):
    global user_line, text_to_display, count, start_time

    if start_time is None:
        start_time = time.time()

    if time.time() - start_time >= 30:
        print("Time's Up")
        check_letters(user_line, text_to_display)
        return

    if len(user_line) >= len(text_to_display):
        print('Sentence finished')
        check_letters(user_line, text_to_display)
        user_line = ''
        next_text = random_pick()
        while text_to_display != next_text:
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


"""

1. Display the window
"""
heading = "SPEED CHECK !"
instruction = "TEST STARTS WHEN YOU ENTER THE WORD"

window = Tk()

window.title('Type Writing Speed Test')
window.config(bg='black')

heading_box = Label(window, text=heading, font=('Helvetica', 20), bg='black', fg='blue')
instruction_box = Label(window, text=instruction, font=('Helvetica', 20), bg='black',fg='blue')

typing_area = Text(window, font=('arial', 14), bg='white', fg='black',wrap='w', padx=5, pady=5, highlightthickness=4)
typing_area.bind('<KeyPress>', start_checking)

reset_btn = Button(window, text='Reset', width=125, command= reset_text_area ,highlightthickness=1 , highlightcolor='black')

heading_box.pack(pady=23)
instruction_box.pack(pady=23)
text_to_type = Label(window, font=('Helvetica', 20), bg='black', fg='blue', highlightthickness=4, highlightcolor='blue', border=3)
display_text(text_to_display)
typing_area.pack()
reset_btn.pack(pady=23)

window.mainloop()