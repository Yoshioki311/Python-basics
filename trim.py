# Trims a given word with extra spaces
def trim(s):
    if s == '':
        return s
    else:
        i = 0
        j = len(s) - 1
        while s[i] == ' ' and i < len(s) - 1:
            i += 1
        while s[j] == ' ' and j > 0:
            j -= 1
        j += 1
        s = s[i:j]
        return s