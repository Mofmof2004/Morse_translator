
morse_code = {".-": "a",
              "-...": "b",
              "-.-.": "c",
              "-..": "d",
              ".": "e",
              "..-.": "f",
              "--.": "g",
              "....": "h",
              "..": "i",
              ".---": "j",
              "-.-": "k",
              ".-..": "l",
              "--": "m",
              "-.": "n",
              "---": "o",
              ".--.": "p",
              "--.-": "q",
              ".-.": "r",
              "...": "s",
              "-": "t",
              "..-": "u",
              "...-": "v",
              ".--": "w",
              "-..-": "x",
              "-.--": "y",
              "--..": "z",

              }

test = "..  .-.. --- ...- .  ..-"

#########################################################################################
import time


# Variables
letter = []
word = []

# Input of morse
phrase = list(input("Enter your phrase: "))

# function for clearing var: letter and print the working out


def save():
    letter.clear()
    time.sleep(0.5)
    print(word)

# loop for translation


# --> Splitting input between letters and words
for i in range(len(phrase)):
    time.sleep(0.5)

    # Finding out the letter
    if phrase[0] in morse_code:
        letter.append(phrase[0])
        phrase.remove(phrase[0])
    # if there is a new letter
    elif phrase[0] == " " and phrase[1] != " ":
        word.append(morse_code.get("".join(letter)))
        save()
        phrase.remove(phrase[0])
        # adding space in the list
        if None in word:
            word.remove(None)
            word.append(" ")
    # if there is a new word
    elif phrase[0] == " " and phrase[1] == " ":
        word.append(morse_code.get("".join(letter)))
        phrase.remove(phrase[0 + 1])
        save()


word.append(morse_code.get("".join(letter)))
letter.clear()

# making the list a string
listToStr = ' '.join(map(str, word))

# printing out the full translation
time.sleep(1)
print("Full translation:")
time.sleep(0.5)
print(listToStr)




