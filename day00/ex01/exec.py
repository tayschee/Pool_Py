import sys

liste_word = []


for arg in sys.argv[1:]:
    for letter in arg:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = chr(ord(letter) - 32)
        elif ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            letter = chr(ord(letter) + 32)
        liste_word.append(letter)
txt = ''.join(reversed(liste_word))
print(txt)
