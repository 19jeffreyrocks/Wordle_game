import random

def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the secret word
    """
    file = open("words.txt", 'r')
    data = file.readlines()
    list1 = [x.replace('\n', '') for x in data]
    # random.randint(0, 5) will generate an integer between 0 and 5 (inclusive)
    # this is then used to select a value from the list.
    wordPosition = random.randint(0, len(list1) - 1)
    return list1[wordPosition]

used_word = []
def checkLetters(secretWord, userWord, used_word):
    """
    This function checks the letters guessed by the user against the secret
    word and informs the user as to which letters are in the correct location,
    which letters are in the word but not in the correct location and which
    letters are not in the word.
    Paramters:   secretWord, userWord - strings
    Returns:  None
    """
    letter_list = []
    unique_letters=[]
    for i in range(min(len(userWord), len(secretWord))):  # loop as many times as the length of the secretWord and ignore the extra length in userWord(ex. secret word is water and userWord is waffle, it ignores the "e", last letter )
        if userWord[i].lower() == secretWord[i].lower():  # if the letter of userword is at the same position as secretword
            print(userWord[i], "- in correct place")
        elif userWord[i] in secretWord:  # else if the letter of userword is a part of the secret word but in the wrong position
            print(userWord[i], "- not in correct place")
        else:
            print(userWord[i], "not in word")  # else the letter of userword is not part of secret word
            letter_list.append(userWord[i])
    used_word.append(letter_list)
    for i in range(len(used_word)):
        for j in used_word[i]:
            if j not in unique_letters:
                unique_letters+=j


    print("Letter that are not in the word are:", unique_letters)


def checkForDuplicates(userWord):
    """
    This function checks the user's word for duplicate letters.
    If there are duplicate letters, the function returns True, otherwise, False.
    Parameters:  userWord - string
    Return:  Boolean
    """
    for i in range(len(userWord)):  # loop length of userword times
        for j in range(len(userWord)):  # loop length of userword times
            if j == i:
                continue
            if userWord[i] == userWord[j]:  # if there are duplicate letters
                return True
    return False


def play(secretWord):
    """
    This function allows the user to play the game, entering up to 6 words to
    try to guess the secret word. When the correct word is guessed, the play
    stops and the user is congratulated.
    Parameters: string representing the secretWord
    Return Value:  None
    """
    userWord = str(
        input("Hello! Please guess a " + str(len(secretWord)) + " letter word:"))  # takes in the input for userword
    userWord = userWord.replace(" ", "")
    for i in range(6):  # loop 6 times
        if checkForDuplicates(userWord) == True:  # if there are duplicate letters
            userWord = str(input("Sorry, your word has duplicate letters.  Enter a word with no duplicates: "))
        elif not userWord.isalpha():
            userWord = str(input("Sorry, your input contains character that are not letters. Enter a word without only letters:"))
        elif secretWord != userWord:  # if the secretword is not the user input word
            checkLetters(secretWord, userWord, used_word)
            userWord = str(input("Please enter another word: "))
        elif secretWord == userWord:  # if the secretword is the userinput(user got it right)
            print("YOU WIN!")
            break  # stop the loop
        if i == 5 and secretWord != userWord:
            print("you lost")


def main():
    """
    This implements the user interface for the program.
    """
    # print("This program doesn't do anything -- fill in the details of each function to make it work")
    word = chooseWord()
    print("The secret word is", word)
    # choose a word & print it on the screen -- you will need to save the word in a variable
    # start the play
    play(word)


main()
