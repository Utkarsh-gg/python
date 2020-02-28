small = None
print(small)
for x in [12,0,21,-3,48,5,2]:
    if small == None or x<small:
        small = x
    print (x,small)
print (small)
