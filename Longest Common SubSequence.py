seq = "ABCDAF"
pat = "ACBCF"
cols, rows = (len(seq)+1,len(pat)+1)

mat = [[0 for i in range(cols)] for i in range(rows)]

# Matrix Building
for i in range(1,rows):
    for j in range(1,cols):
        if pat[i-1] == seq[j-1]:
            mat[i][j] = mat[i-1][j-1] + 1
        else:
            a = mat[i-1][j]
            b = mat[i][j-1]
            mat[i][j] = max(a,b)
print(mat)

#Back Tracking
lcs_index = []
lcs = []

def backtracking(i, j):
    if i!=0 and j!=0:
        if pat[i-1] == seq[j-1]:
            lcs.append(seq[j-1])
            backtracking(i-1, j-1)
        else:
            if mat[i][j] == mat[i][j-1]:
                backtracking(i, j-1)
            else:
                backtracking(i-1, j)
        
backtracking(len(pat), len(seq))
print(lcs)
