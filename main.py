# The code should analyse the input and summarize the amount of character, vowel, and consonant
# Analyzing function
def analyze_string(words):
    # error message
    if not isinstance(words, str):
        return 'The word should only have letters.'
    for num in range(0, 10):
        if str(num) in words:
            return 'The word should only have letters.'
    
    # function
    no_spaces = words.replace(' ', '')
    vowel = 'aeiou'
    vowel_number = 0
    consonant_number = 0
    for char_check in list(no_spaces.lower()):
        if char_check.isalpha():
            if char_check in vowel:
                vowel_number += 1
            else:
                consonant_number += 1
    character_number = vowel_number + consonant_number
    char_label = 'character' if character_number in (1,0) else 'characters'
    vowel_label = 'vowel' if vowel_number in (1,0) else 'vowels'
    consonant_label = 'consonant' if consonant_number in (1,0) else 'consonants'
    return (f'''Result:
    The word {words} has:
    - {character_number} {char_label}
    - {vowel_number} {vowel_label}
    - {consonant_number} {consonant_label}''')

while True:
    user_word = input('What word would you like to analyze?  ').strip()
    if not user_word:
        print('Your input is needed.')
        continue
    break

print(analyze_string(user_word))