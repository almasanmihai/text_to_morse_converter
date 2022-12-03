from alphabet import MORSE_ALPHABETH

print('Please enter only basic Latin letters and Arabic numerals')
words_to_convert = input('Input message to convert to morse: ').lower()
conversion = ''
try:
    for char in words_to_convert:
        conversion += MORSE_ALPHABETH[char]
except KeyError:
    print('No valid characters entered.')
print(conversion)
