#1

number=[1,5,6,9,0]
for i in range(len(number)):
  for j in range(i+1,len(number)):
    if number[i]<number[j]:
      number[i],number[j]=number[j],number[i]
print(number)

#2 

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print new_list

# 3

l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print l
