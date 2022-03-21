import random
import tkinter as tk

NUM_GUESSES = 6
WORD_LENGTH = 5

def main():
    #Harry Potter words with 5 characters
    words = ['accio','magic','harry','giant','ghoul','curse']
    secret = random.choice(words)

    #Create graphical user interface
    window = tk.Tk()
    window.title("WORDLE")
    input_fields = [[createEntry(window,row,col) for col in range(WORD_LENGTH)] for row in range(NUM_GUESSES)]
    label = tk.Label(window,text = "WORDLE")
    label.grid(row=7,column=0,columnspan=6,sticky='EW')
    awaitGuess(secret,input_fields,label,0)
    window.mainloop()

def checkGuess(event, secret, input_fields, label, row):
    guess = chainChars(input_fields[row])
    label.config(text="")
    if len(guess) != WORD_LENGTH:
        label.config(text="Please enter a word with 5 letters!")
    else:
        disableRow(input_fields,row)
        if guess == secret:
            for col in range(WORD_LENGTH):
                input_fields[row][col].config(disabledbackground='green')
            label.config(text="Congrats! You solved the WORDLE!")
        else:
            for i in range(len(guess)):
                if guess[i] is secret[i]: input_fields[row][i].config(disabledbackground='green')
                elif guess[i] in secret: input_fields[row][i].config(disabledbackground='yellow')
            awaitGuess(secret,input_fields,label,row+1)

def chainChars(chars):
    word = ""
    for i in range(len(chars)):
        char = chars[i].get()
        word = word + char
    return word

def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isalpha():
        return True
    else:
        return False
    return True

def createEntry(window,row,col):
    e = tk.Entry(window, width=2, font = 'Helvetica 20 bold', justify='center',state='disabled', validate="key", validatecommand=(window.register(validate),'%P'))
    e.grid(row=row,column=col,sticky='EW')
    return e

def enableRow(input_fields,row):
    for col in range(WORD_LENGTH):
        input_fields[row][col].config(state='normal')
    input_fields[row][0].focus()

def disableRow(input_fields,row):
    for col in range(WORD_LENGTH):
        input_fields[row][col].config(state='disable')

def awaitGuess(secret,input_fields,label,row):
    for col in range(WORD_LENGTH):
        input_fields[row][col].bind("<Return>", lambda event: checkGuess(event, secret, input_fields, label,row))
    enableRow(input_fields,row)

if __name__ == "__main__":
    main()
