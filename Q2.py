print("matin ghorbani\nporya.ghorbani10@gmail.come\n09021801386 ")

def Run(s=input("string: ")):
    k=[]

    for a in s:
        k.append(a)

    l=[k[0]]
    i=0
    m=len(k)
    while i<m:
        if k[i]!=l[-1]:
            l.append(k[i])
        
        i=i+1
    h=len(k)-len(l)
    print(l)
    print(h)

Run()