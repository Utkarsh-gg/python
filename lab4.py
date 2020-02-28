#display palindrome present in word
a = input().split(' ')
for i in a:
    if(i == i[::-1]):
        print(i)
