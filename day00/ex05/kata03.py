import sys

phrase = "une phrase aux hasard"
i = 42 - len(phrase)
while (i != 0):
    print("-", end="")
    i = i - 1
print(phrase, end="")


