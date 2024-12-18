matrix = [
    [0,1,0,0,1],
    [1,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,1],
    [1,0,0,1,0]
]

print(matrix)
print(matrix[0])
print(len(matrix))

m = len(matrix)
n = len(matrix[0])
print(m,n)

d = dict()
l = list()
for i in range(len(matrix)):
    l = list()
    for j in range(len(matrix[0])):
         if(matrix[i][j] != 0):
           l.append(j)

    d.update({i:l})

print(d)