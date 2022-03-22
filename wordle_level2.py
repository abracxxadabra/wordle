import random
import tkinter as tk

NUM_GUESSES = 6
WORD_LENGTH = 5

def main():
    print("Your task is the implementation of the checkGuess(...) function. The function describes the core logic of wordle by determining and displaying the colouring hint for each letter of a guess. \n First, find the '???' symbols and substitute them with valid python code. Second, remove the comment symbol '#' on each line of checkGuess(...) as well as the 'pass' statement in order to complete the code.")
    #Harry Potter words with 5 characters
    words = ['accio','magic','harry','giant','ghoul','curse']
    secret = random.choice(words)

    #Create graphical user interface
    window = tk.Tk()
    window.title("WORDLE")
    input_fields = [[createEntry(window,row,col) for col in range(WORD_LENGTH)] for row in range(NUM_GUESSES)]
    label = tk.Label(window, text = "WORDLE")
    label.grid(row=7, column=0, columnspan=6, sticky='EW')
    awaitGuess(secret, input_fields, label, 0)
    window.mainloop()

def checkGuess(event, secret, input_fields, label, row):
    pass
#    guess = chainChars(input_fields[row])
#    label.config(text="")
#    if len(???) != WORD_LENGTH:
#        label.config(text="Please enter a word with 5 letters!")
#    else:
#        disableRow(input_fields,row)
#        if guess == ???:
#            for col in range(WORD_LENGTH):
#                input_fields[row][col].config(disabledbackground='green')
#            label.config(text="Congrats! You solved the WORDLE!")
#        else:
#            for i in range(len(guess)):
#                if guess[i] is ???[i]: input_fields[row][i].config(disabledbackground='green')
#                elif guess[i] in ???: input_fields[row][i].config(disabledbackground='???')
#            awaitGuess(secret,input_fields,label,row+1)

#takes a list 'chars' of entry fields and transfers it into a string
def chainChars(chars):
    word = ""
    for i in range(len(chars)):
        char = chars[i].get()
        word = word + char
    return word

#returns true if the user input P is valid, meaning, either none or a single letter
#returns false, otherwise
def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isalpha():
        return True
    else:
        return False
    return True

#returns a nicely configured entry field
def createEntry(window, row, col):
    e = tk.Entry(window, width=2, font = 'Helvetica 20 bold', justify='center', state='disabled', validate="key", validatecommand=(window.register(validate),'%P'))
    e.grid(row=row, column=col, sticky='EW')
    return e

#activates all entry fields in a specified row to allow user input
def enableRow(input_fields, row):
    for col in range(WORD_LENGTH):
        input_fields[row][col].config(state='normal')
    input_fields[row][0].focus()

#deactivates all entry fields in a specified row to detain user input
def disableRow(input_fields,row):
    for col in range(WORD_LENGTH):
        input_fields[row][col].config(state='disable')

#read in guess on enter 
def awaitGuess(secret, input_fields, label, row):
    for col in range(WORD_LENGTH):
        input_fields[row][col].bind("<Return>", lambda event: checkGuess(event, secret, input_fields, label, row))
    enableRow(input_fields, row)

if __name__ == "__main__":
    main()
