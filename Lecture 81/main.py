morse_code_rules = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

user_input = input("What do you want to convert into Morse Code?\n").lower()
morse_output = []


def text_to_morse():
    for char in user_input:
        if char in morse_code_rules:
            morse_char = morse_code_rules.get(char)
            morse_output.append(morse_char)
        else:
            print("Please try again")


text_to_morse()

morse_string: str = ''.join(morse_output)

print(f'The Morse Code of {user_input} is {morse_string}')
