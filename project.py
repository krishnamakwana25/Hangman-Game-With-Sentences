from tkinter import *
from tkinter import messagebox
import random
import time

gui = Tk()
gui.title("Hangman Game - AI Project")
gui.geometry("850x550+400+50")
# gui.resizable(False, False)
hangmanPics = [PhotoImage(file='hangman6.png'), PhotoImage(file='hangman5.png'), PhotoImage(file='hangman4.png'),
               PhotoImage(file='hangman3.png'), PhotoImage(file='hangman2.png'), PhotoImage(file='hangman1.png'),
               PhotoImage(file='hangman0.png')]
img_lbl = Label(gui)
lblWord = StringVar()

Label(gui, textvariable=lblWord, font="Consolas 27 bold", bg="#f5ece7", foreground="black").place(x=20, y=400,
                                                                                                  height="40",
                                                                                                  width="810")
tries1 = StringVar()
guess_text = Entry(textvariable=tries1, font=("cooper ", 21), state="disabled", justify="center", relief="solid").place(
    x=260, y=260, height="40",
    width="160")
tries1.set(6)
b = StringVar()


def quit_btn():
    quit_redraw_window()


def check_btn():
    guess = b.get()
    if guess != "":
        guess_sentence(guess.upper())
        # word_text.delete(0, last=20)
    else:
        messagebox.showinfo("information Message", "Please Enter any letter or word..!")


# ======================================================================================================================
tries = 6
guessed_letters = []
guessed_words = []


def quit_redraw_window():
    que = messagebox.askquestion("Question Box", "Are you sure to quit this game ?")
    if que == "yes":
        gui.destroy()
    else:
        draw_window()
        word = get_word()
        play(word)
        gui.mainloop()


def redraw_window():
    que = messagebox.askquestion("Question Box", "Do you want to play again ?")
    if que == "yes":
        draw_window()
        word = get_word()
        play(word)
        gui.mainloop()
    else:
        gui.destroy()


def guess_sentence(guess):
    global tries
    global complete_word
    global word_as_list
    guessed = False
    word_as_list = list(complete_word)
    guess = guess.upper()
    if not guessed and tries > 0:
        if guess.isalpha():
            if len(guess) == 1:
                if guess in guessed_letters:
                    messagebox.showinfo("information Message", "You already guessed the letter : " + guess + "")
                elif guess not in randomword:
                    messagebox.showinfo("information Message", "" + guess + " is not the letter in the sentence")
                    tries = tries - 1  # decrease tries by 1 when user guesses wrong letter
                    guessed_letters.append(guess)
                else:
                    guessed_letters.append(guess)
                    indices = [i for i, letter in enumerate(randomword) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    complete_word = "".join(word_as_list)
                    lblWord.set(complete_word)
                    if "_" not in complete_word:
                        guessed = True
            elif len(guess) > 1:
                if guess in guessed_words:
                    messagebox.showinfo("information Message", "You already guessed the letter : " + guess + "")
                elif guess not in randomword:
                    messagebox.showinfo("information Message", "" + guess + " is not the word in the sentence")
                    tries -= 1  # decrease tries by 1 when user guesses wrong word
                    guessed_words.append(guess)
                else:
                    words = randomword.split()
                    for index, w in enumerate(words):
                        if guess in w:
                            index1 = randomword.find(guess)
                            temp = ""
                            index1_copy = index1
                            for j in range(10 + 1):
                                if randomword[index1] == " " or randomword[index1] == "\n":
                                    break
                                else:
                                    temp += randomword[index1]
                                index1 += 1

                            if len(temp) == len(guess):
                                for i in range(len(guess)):
                                    word_as_list[index1_copy] = guess[i]
                                    index1_copy += 1
                                guessed_words.append(guess)
                            else:
                                messagebox.showinfo("information Message",
                                                    "" + guess + " is not the word in the sentence")
                                tries -= 1  # decrease tries by 1 when user guesses wrong word
                                guessed_words.append(guess)
                    complete_word = "".join(word_as_list)
                    lblWord.set(complete_word)
                    if "_" not in complete_word:
                        guessed = True
            else:
                messagebox.showinfo("information Message", "Not a valid guess..!")
            img_lbl.config(image=hangmanPics[tries])
            tries1.set(tries)
            print(complete_word)
            print("Guessed letters : ", guessed_letters)
            print("Guessed word : ", guessed_words)
        else:
            messagebox.showinfo("information Message", "Please Enter only letter or word.")

    if "_" not in complete_word or tries == 0:
        guessed_letters.clear()
        guessed_words.clear()
        if guessed:
            tries = 6
            time.sleep(1);
            messagebox.showinfo("information Message",
                                "You correctly guessed the word \n" + randomword + "\n You won !")
            time.sleep(1);
            redraw_window()
        else:
            tries = 6
            time.sleep(1);
            messagebox.showerror("Message Box", "Sorry..! You run out the tries.\n The word was " + randomword + ".")
            time.sleep(1);
            redraw_window()


def get_word():
    file_data = open("projectdata.txt")
    data1 = file_data.readlines()
    data = random.choice(data1)
    length = len(data)  # - 1
    randomword = data[0:length]
    print("Random Word is :-", randomword)
    return randomword.upper()


def sent_into_hiddenlist(random_word):
    global complete_word
    complete_word = list("")
    for i in range(0, len(random_word) - 1):
        if random_word[i] != " ":
            complete_word += "_"
        else:
            complete_word += " "
    return complete_word


def play(random_word):
    global complete_word
    global randomword
    randomword = random_word
    complete_word = sent_into_hiddenlist(randomword)
    lblWord.set("".join(complete_word))


# ========================================== DESIGN ====================================================================
def draw_window():
    title_game = Label(text="HANGMAN GAME", font="cooper 30", bd=1, fg="white", relief="solid", bg="#996666").place(
        x=250,
        y=10,
        height="60",
        width="350")
    img_lbl.place(x=500, y=100, height="270", width="270")
    img_lbl.config(image=hangmanPics[6])
    entry_lbl = Label(text="Enter a Letter", relief=RAISED, font=("cooper ", 21), fg="white", bg="#808080").place(x=45,
                                                                                                                  y=120,
                                                                                                                  height="40",
                                                                                                                  width="190")
    word_text = Entry(textvariable=b, font=("cooper bold", 21), justify="center", relief="solid").place(x=250, y=120,
                                                                                                        height="40",
                                                                                                        width="200")
    check_btn1 = Button(text="Check", relief="solid", command=check_btn, fg="white", activebackground="black",
                        font=("cooper ", 21), activeforeground="white", bg=
                        "#4A708B").place(x=150, y=190, height="40", width="150")
    left_no = Label(text="No. of Guesses", relief=RAISED, font=("cooper ", 21), fg="white", bg="#808080").place(x=45,
                                                                                                                y=260,
                                                                                                                height="40",
                                                                                                                width="200")
    gui.configure(bg='#f5ece7')
    tries1.set(6)
    quit_btn1 = Button(text="Quit", relief="solid", command=quit_btn, fg="white", activebackground="black",
                       font=("cooper ", 21), activeforeground="white", bg="#4A708B").place(x=300, y=470, height="40",
                                                                                           width="130")


draw_window()
word = get_word()
play(word)
gui.mainloop()
