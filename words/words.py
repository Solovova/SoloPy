in_letter = "кизиатр"
in_mask = "**и"

def CheckCompatible(word, letterSet):
    for letter in word:
        ind = letterSet.find(letter)
        if (ind == -1):
            return False
        else:
            letterSet = letterSet[0 : ind : ] + letterSet[ind + 1 : :]
    return True

def CheckMask(word, mask):
    for ind in range(0,len(mask)):
        if (mask[ind] != '*') and (mask[ind] != word[ind]):
            return False
    return True

with open("D:\\Programming\\ukrwords1.txt") as f:
    for line in f:
        word = line.strip()
        if len(word) == len(in_mask) and CheckCompatible(word,in_letter) and CheckMask(word,in_mask):
            print(word)        