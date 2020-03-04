#display palindrome present in string
a = input().split(' ')
for i in a:
    if(i == i[::-1]):
        print(i)
