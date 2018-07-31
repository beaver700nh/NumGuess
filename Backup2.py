from tkinter import *
import random
import time

number = random.randint(0,100)

spaces = (50 * ' ')
my_font = 'Courier New'
score = 0
win = False
destroyed = False
t1 = None
t2 = None
first_time = True
in_game = False

tk = Tk()

def introduction():
    global spaces
    global my_font
    global in_game

    intro_line_1 = Label(tk, text='Hello user!' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=10)
    intro_line_2 = Label(tk, text='Welcome to the million dollar app,' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=35)
    intro_line_3 = Label(tk, text='NumGuess v2.0 by Minh Le!' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)
    intro_line_4 = Label(tk, text='Try to guess a number between 1 and 100' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=85)
    intro_line_5 = Label(tk, text='correctly 5 times as quickly' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=110)
    intro_line_6 = Label(tk, text='as possible. Good luck and enjoy!' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=135)
    tk.update()
        
def play():
    global spaces
    global my_font
    global score
    global win
    global number
    global destroyed
    global first_time
    
    try:
        if first_time == True:
            first_time = False
            t1 = int(time.time())
        
        if int(guess.get()) == number:########
            score += 1
            number = random.randint(0,100)
            hint = Label(tk, text=('Correct! Good job! Your score is now %s.' % score) + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)
            tk.update()
            if score == 5:
                t2 = int(time.time())
                time.sleep(3)
                yay = Label(tk, text=('Congratulations! You won in %s seconds!' % (t2-t1)) + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)
                tk.update()
                time.sleep(2)
                destroyed = True
        
        elif int(guess.get()) > 100:
            Error = Label(tk, text='Error: Your input is too high.' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)

        elif int(guess.get()) < 0:
            Error = Label(tk, text='Error: Your input is too low.' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)
            
        elif int(guess.get()) < number:
            hint = Label(tk, text='Higher!' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)
            
        elif int(guess.get()) > number:
            hint = Label(tk, text='Lower!' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)

        if destroyed == False:
            user_input.delete(0,"end")
        else:
            tk.destroy()
        
    except ValueError:
        if not bool(guess.get().strip()):
            Error = Label(tk, text='Error: You need to enter something.' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)

        else:
            Error = Label(tk, text='Error: Enter a NUMBER between 1 and 100.' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)
            
        user_input.delete(0,"end")

def game(event):
    if in_game:
        play()

def start_now():
    global in_game

    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=10)
    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=35)
    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=60)
    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=85)
    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=110)
    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=135)
    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=160)
    prep_for_starting = Label(tk, text=spaces + spaces + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=185)
    
    guess_a_number = Label(tk, text='Guess a number between 1 and 100: ' + spaces, font=(my_font, 11), fg='#000000').place(x=10, y=85)
    tk.update()
    guess = StringVar()##########
    user_input = Entry(tk, textvariable=guess, width=30, bg='#ffffff')
    user_input.place(x=325, y=85)
    user_input.bind_all('<KeyPress-Return>', game)
    
    in_game = True

tk.title('Million Dollar App')
tk.geometry('525x200')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
tk.update()

start_button = Button(tk, text='Play', fg='#ffffff', bg='#009900', command=start_now).place(x=230, y=165)

introduction()

tk.mainloop()
