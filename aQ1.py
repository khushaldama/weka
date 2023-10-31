list = []
temp = []
cluster = []
n = input("Enter Number of Values you want: ")
n= int(n)
for i in range(n):
    t = int(input("Enter the values: "))
    temp.append(t)

n = int(input("Enter How many Cluters You want: "))
no = len(temp)/n;

for i in range(n):
    s1 = int(input("Starting Boundary of Your Cluster 1:  "))
    e1 = int(input("Ending Boundary of Your Cluster 1:  "))
    boundaries = []
    boundaries.append(s1)
    boundaries.append(e1)
    cluster.append(boundaries)
        
if((i+1)%no==0):
    list.append(temp)
    temp = []
print(list)
print(cluster)

#_________________________________________________Having Issues!!__________________
newlist = []
newCluster = []
temp_1 = []
temp_2 = []
for i in list:
    for j in i:
        for a in range(len(cluster)):
            if(j > a[0] and j <= a[1]):
                temp_1.append(j)
            if(j > a[0] and j <= a[1]):
                temp_2.append(j)
newlist.append(temp_1)
newlist.append(temp_2)
print(newlist)
#_________________________________________________Having Issues!!__________________
