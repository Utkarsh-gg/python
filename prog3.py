big = None
print(big)
for x in [12,0,21,-3,48,5,2]:
    if big == None or x>big:
        big = x
    print (x,big)
print (big)
