a = [1,2,2,3,4,4,4,4,5,6,7,7,7,8,9,9,9,10,11,11]

i = 1
j = len(a)-1
ele = 0
while i<=j:
  if a[i]==a[i-1]:
    ele = a.pop(i-1)
    a.append(ele)
    j-=1
  else:
    i+=1

print(a)
print(j)