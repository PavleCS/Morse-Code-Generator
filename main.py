import string


# lists with regular char
alphabet = list(string.ascii_lowercase)
numbers = []
for num in range(0, 10):
    numbers.append(num)
symbols = [".", ",", ":", "?", "'", "-"]


# lists with morse char
morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                  "-.", "---", ".--.", "--.-", ".-.", "...", "- ", "..-", "...-", ".--", "-..-", "-.--", "--.."]
morse_numbers = [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]
morse_symbols = [".-.-.-", "--..--", "---...", "..--..", ".----.", "-....-"]


# dictionaries that contain regular char as keys and morse char as values
alphabet_dict = dict(zip(alphabet, morse_alphabet))
numbers_dict = dict(zip(numbers, morse_numbers))
symbols_dict = dict(zip(symbols, morse_symbols))


# merging all dicts
def merge(dict_1, dict_2, dict_3):
    result = dict_1 | dict_2 | dict_3
    return result


all_char = merge(alphabet_dict, numbers_dict, symbols_dict)

# asking user for an input
user_input = input("Please enter your letter, word or a sentence: ").lower()

# converting input into morse
converted_char_list = [all_char[char] for char in user_input if char in all_char]

final_word_in_morse = ""

for i in converted_char_list:
    final_word_in_morse += f"{i}  "

# final result
print(final_word_in_morse)
