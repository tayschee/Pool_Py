def text_analyzer(string):
    i = 0
    up = 0
    lo = 0
    sp = 0
    pun = 0
    if (str(string) == int(0)) :
        print("What is the text to analyse?")
    else :
        for l in string:
            if (ord(l) == 32):
                sp = sp + 1        
            elif (ord(l) >= ord('a') and ord(l) <= ord('z')):
                lo = lo + 1
            elif (ord(l) >= ord('A') and ord(l) <= ord('Z')):
                up = up + 1
            for punct in "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~":
                if (punct == l):
                    pun = punct + 1
            i = i + 1
    print("The text contains", i,  "characters:\n-", up, "upper letters\n-", lo, "lower letters\n-", pun, "punctuation marks\n-", sp, " spaces")
