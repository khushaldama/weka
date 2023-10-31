#list=[12,45,67,88,90,43,54,17,9,11,33,18]
list=[]
n=int(input("how many element you want "))
for i in range(n):
    r=int(input("enter your  element"))
    list.append(r)
list.sort()
min=list[0]
max=list[len(list)-1]
#print(list)
#print(min)
#print(max)
bing=int((max-min)/len(list))
print(bing)
mainlist=[]
num_item=int(len(list)/bing)
print(num_item)
start_index=0
lastindex=num_item
for j in range(bing):
    l1=list[start_index:lastindex]
    mainlist.append(l1)
    start_index=start_index+2
    lastindex=lastindex+2
#print(mainlist)
meanlist=[]
for q in mainlist:
    sum = 0
    for w in q:
        sum=sum+w
    mean=int(sum/len(q))
    meanlist.append(mean)
#print(meanlist)
for x in range(0,len(mainlist)):
    change_val=meanlist[x]
    for y in range(0,len(mainlist[x])):
        mainlist[x][y]=change_val
print(mainlist)
print(meanlist)








# min=[]
# min.append(list[:6])
# print(min)