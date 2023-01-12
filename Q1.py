print("matin ghorbani\nporya.ghorbani10@gmail.come\n09021801386 ")

def Run(s=input("string: "),i=int(input("integer: "))):
    k=[]

    for a in s:

        k.append(a)
    
    m=i-len(k)
    
    n=0
    
    while m>n:
        k.append(k[n])
        n=n+1


    #print(k)
    for h in k:
        print(h,end='')
    
    print("\nlen of new string: "+str(len(k)))

    print("there are "+str(k.count('a'))+" 'a's in the new string.")

Run()