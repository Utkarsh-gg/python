for _ in range(int(input())):
    a,b = input().split()
    sol = int(a)-int(b);
    if(sol<0):
        print ("2 ",-sol,end=' ')
    else:
        print ("1 ", sol,end = ' ')
