values = {'A':0, 'C':1, 'G':2, 'T':3}
def rabinKarpAlgorithm(text,pat):
	textLength = len(text)
	patLength = len(pat)
	k = textLength - patLength + 1
	patValue = weightOfString(pat,patLength,k)
	print("Weight of Pattern:"+str(patValue))
	index = computeT(text, k, patLength, patValue)

def weightOfString(pat,patLength,k):
	i = 0
	preValue = values[pat[i]]
	curValue = 0
	p = 0
	while( i != patLength-1):
		p = k*preValue
		curValue = values[pat[i+1]] + p
		preValue = curValue
		i += 1
	p += values[pat[len(pat)-1]]
	return p

def computeT(text, k, m, patValue):
	t = []
	patLength = m
	K = k
	match = False
	for i in range(len(text) - m + 1):
		s = text[i:i+m]
		if( i == 0):
			t.append(weightOfString(s,len(s),k))
			if patValue == t[i] :
				match = True
				print("String is found at position " + str(i+1))
		else:
			t.append(calculateTValues(text,patLength,K,t[i-1],i))
			if patValue == t[i] :
				match = True
				print("String is found at position " + str(i+1))
	if(match != True):
		print("Pattern is not found")
	
def calculateTValues(text,m,k,prevT,i):
	t = (prevT - (pow(k,m-1)*values[text[i-1]]))*k
	t += values[text[i+m-1]]
	return(t)

text = "ATTCCGTCCGTCCG"
pat = "TCCG"
rabinKarpAlgorithm(text,pat)
