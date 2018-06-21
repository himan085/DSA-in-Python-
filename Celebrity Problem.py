
M = ((0,1,0,0),
     (0,0,0,0),
     (0,1,0,0),
     (0,1,0,0))

print(M)

def knows(a,b):
    return M[a][b]


def function(n):
    s=[]

    for i in range(0,n):
        s.append(i)

    a = s.pop()
    b = s.pop()

    while(len(s)>1):
        if(knows(a,b)):
            a = s.pop()
        else:
            b = s.pop()

    c = s.pop()

    if(knows(c,b)):
        c = b

    if(knows(c,a)):
        c = a

    for i in range(0,n):
        if((i!=c) and (knows(c,i) or not(knows(i,c)))):
            return -1

    return c


n = 4
id = function(n)
if(id == -1):
    print('No Celeb')
else:
    print(id)

