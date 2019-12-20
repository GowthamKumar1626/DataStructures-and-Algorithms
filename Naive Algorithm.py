#Basic Algorithm for string matching
#It's complexity is too high. It is not suitable for pattern matching for long strings like GENOME

def naiveAlgorithm(text, pat):
    textLength = len(text)
    patLength = len(pat)
    match = 0
    for i in range(textLength-patLength+1):
        j = 0
        while j<patLength and text[i+j] == pat[j]:
            j += 1
            if j == patLength:
                match = 1
                print("Pattren is found at position "+str(i+1))
    if match!=1:
            print("Pattern is Not Found")

text = "AGTAGTTTGACAGT"
pat = "AGT"
naiveAlgorithm(text, pat)

