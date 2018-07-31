from tkinter import *
import random, time

class MyGame:
    def __init__(self):
        self.number_ = random.randint(0, 100)
        self.in_game_ = False
        self.spaces_ = (100 * ' ')
        self.my_font_ = ('courier new', 11)
        self.black_ = '#000000'
        self.white_ = '#ffffff'
        self.green_ = '#008800'
        self.score_ = 0

    def intro(self, title, window_size, version):
        tk_intro = Tk()
        
        tk_intro.title(title)
        tk_intro.geometry(window_size)
        tk_intro.resizable(0, 0)
        tk_intro.wm_attributes('-topmost', 1)
        tk_intro.update()

        def start():
            self.tk_x = tk_intro.winfo_x()
            self.tk_y = tk_intro.winfo_y()
            tk_intro.destroy()

        intro_line_1 = Label(tk_intro, text='Hello user!' + self.spaces_,
                             font=self.my_font_, fg=self.black_).place(x=10, y=10)
        
        intro_line_2 = Label(tk_intro, text='Welcome to the million dollar app,' + self.spaces_,
                             font=self.my_font_, fg=self.black_).place(x=10, y=35)
        
        intro_line_3 = Label(tk_intro, text=('NumGuess %s by Minh Le!' % version) + self.spaces_,
                             font=self.my_font_, fg=self.black_).place(x=10, y=60)
        
        intro_line_4 = Label(tk_intro, text='Try to guess a number between 1 and 100' + self.spaces_,
                             font=self.my_font_, fg=self.black_).place(x=10, y=85)
        
        intro_line_5 = Label(tk_intro, text='correctly 5 times as quickly' + self.spaces_,
                             font=self.my_font_, fg=self.black_).place(x=10, y=110)
        
        intro_line_6 = Label(tk_intro, text='as possible. Good luck and enjoy!' + self.spaces_,
                             font=self.my_font_, fg=self.black_).place(x=10, y=135)
        
        tk_intro.update()

        start_ = Button(tk_intro, text='Play', font=self.my_font_, fg=self.white_, bg=self.green_, command=start).place(x=230, y=165)


        tk_intro.mainloop()

    def play(self, title, window_size):
        tk_play = Tk()

        tk_play.title(title)
        tk_play.geometry('{}+{}+{}'.format(window_size, self.tk_x, self.tk_y))
        tk_play.resizable(0, 0)
        tk_play.wm_attributes('-topmost', 1)
        tk_play.update()

        play_text = Label(tk_play, text='Guess a number between 1 and 100:' + self.spaces_,
                          font=self.my_font_, fg=self.black_).place(x=10, y=85)

        guess = StringVar()
        user_guess = Entry(tk_play, textvariable=guess, width=30, bg=self.white_)
        user_guess.place(x=325, y=85)

        def check(event):
            try:
                converted_guess = int(guess.get())
                
                if converted_guess == self.number_:
                    self.score_ += 1
                    hint = Label(tk_play, text=('You guessed right! Your score is now %s!' % self.score_) + self.spaces_,
                                 font=self.my_font_, fg=self.black_).place(x=10, y=60)
                    
                    self.number_ = random.randint(0, 100)
                    user_guess.delete(0, 'end')
                    
                    if self.score_ == 5:
                        hint = Label(tk_play, text='You win!' + self.spaces_,
                                 font=self.my_font_, fg=self.black_).place(x=10, y=60)
                        tk_play.update()
                        
                        time.sleep(3)
                        tk_play.destroy()
                        
                elif converted_guess < self.number_:
                    hint = Label(tk_play, text='Guess higher' + self.spaces_,
                                 font=self.my_font_, fg=self.black_).place(x=10, y=60)
                    
                    user_guess.delete(0, 'end')
                    
                elif converted_guess > self.number_:
                    hint = Label(tk_play, text='Guess lower' + self.spaces_,
                                 font=self.my_font_, fg=self.black_).place(x=10, y=60)
                    
                    user_guess.delete(0, 'end')

            except ValueError:
                hint = Label(tk_play, text='Guess a NUMBER.' + self.spaces_,
                                 font=self.my_font_, fg=self.black_).place(x=10, y=60)
                
                user_guess.delete(0, 'end')

        user_guess.bind_all('<KeyPress-Return>', check)

g = MyGame()

g.intro('Million Dollar App', '525x200', 'v0.7')
g.play('Million Dollar App', '525x200')
