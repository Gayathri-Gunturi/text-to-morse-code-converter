
print("Welcome to Text to Morse code converter\n")
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'  # space for word separator in Morse
}

x = input("Enter a string to convert into Morse code: ").upper()  # convert all lower cases to upper case
print("You entered:", x)

print("Morse code:\n")
# Convert each character to Morse code
for i in x:
    if i in morse_dict:
        print(morse_dict[i], end=' ')  # Print Morse code with a space between each code
