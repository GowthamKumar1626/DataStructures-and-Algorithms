#Pattren Matching with KMPAlgorithm
#In this Algorithm while pattern matching backtravking of text dosen't happens. It collects the repetion of characters in pattern and forms a LPS
def KMPCompute(text, pat):
    textLength = len(text)
    patLength = len(pat)
    i = 0
    j = 0
    lps = [0] * patLength
  
    lpsCompute(pat, lps) #Computing LPS
    while i < textLength:
        if pat[j] == text[i]:
            i += 1
            j += 1
        if j == patLength:
            print("Pattern is found at position " + str(i - j))
            j = lps[j - 1]
        elif i < textLength and pat[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

#LPS computation
def lpsCompute(pat, lps):
    patLength = len(pat)
    i = 0
    j = 1
    while j < patLength:
        if pat[i] == pat[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            lps[j] = 0
            j += 1


text = "ATCGACGATCTAGCATG"
pat = "GAC"
KMPCompute(text, pat)
