# Rabin Karp Algorithm works on finding a hashcode value for the given pattern and matches in text with substr of same hashcode value
# Here hashcodevalue cane be find through different methods 
# In this code we calculated hashcodevalue by using ascii values of charachters
def RabinKarpAlgorithm(text, pat):
    textLength = len(text)
    patLength = len(pat)
    pathashValue = hashValue(pat)
    match = 0
    for i in range(textLength):
        substr = text[i:i + patLength]
        substrHashValue = hashValue(substr)
        j = 0
        if pathashValue == substrHashValue:
            while j < patLength and text[i + j] == pat[j]:
                j += 1
                if j == patLength:
                    match = 1
                    print("Pattren is found at position " + str(i + 1))
    if match != 1:
        print("Pattern is Not Found")


def hashValue(seq):
    value = 0
    for i in range(len(seq)):
        p = seq[i:i + 1]
        value += ord(p)
    return value / 10


text = "ATGCATATGCCAGCATCATGCTCATGCAGCTAACAGAACTACG"
pat = "ATGC"
RabinKarpAlgorithm(text, pat)
