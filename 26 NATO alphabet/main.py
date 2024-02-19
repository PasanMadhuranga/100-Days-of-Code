import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in dataframe.iterrows()}


def nato_phonetic_generator():
    word = input("Enter a word: ").upper()
    try:
        nato_word = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_phonetic_generator()
    else:
        print(nato_word)

nato_phonetic_generator()


