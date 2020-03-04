#best 2 marks out of 3 marks
a = input().split()
sorted(a)
sum = 0
for i in a[1:]:
    sum = sum + int(i)
print(sum)
