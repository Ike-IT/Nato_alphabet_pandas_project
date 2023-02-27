import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (letter, row) in data.iterrows()}  # Here a dict comprehension was used to loop tru a file.


def generate_phonetic():
    word = input("Enter a letter: ").upper()
    try:  # Here the exception handling starts
        output_list = [phonetic_dict[letter] for letter in word]  # Here a list comprehension was used to loop through a dict.
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
