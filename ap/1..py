import operator
from builtins import print
from collections import Counter



# f=[['a','c','d'],['b','c','e'],['a','b','c','e'],['b','e'],['a','f','g'],['b','d','e']]

f=[['l', 't', 'p', 'h'],['p', 'm', 't'], ['l', 'p', 't', 'h'],['l', 'm', 't', 'h'], ['p', 'm', 't', 'h'],['p', 't', 'h'],['m', 'h'],['l', 'p', 'm'],['l', 't', 'h'],['p', 't']]
# for i in range(n):
#     p=[]
#     f.append(p)
#     t = int(input("how many element inside list"))
#     for y in range(t):
#         r=input("enter your first element")
#         p.append(r)
#

# print(f)
p=()
d1={}
for x in f:
    p+=tuple(i for i in x)
    d1=dict(Counter(p))
print(d1)
apryori=[]
l2=[]
l3=[]
sorted_d = sorted(d1.items(), key=operator.itemgetter(1))
sorted_d = dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)
for k,v in sorted_d.items():
    if (v>1):
        support=v/len(f)
        l2.append(k)
        a=[k,v,support]
        apryori.append(a)
for a in range(0,len(l2)):
    s1=l2[a]
    for b in range(a+1,len(l2)):
        s2=s1+l2[b]
        l3.append(s2)

count=0
second_le={}
print(l2)
print(l3)
con=[]
for i in range(0,len(l3)):
    q=l3[i]
    w=tuple(q)
    mf=w[0]
    for z in f:
        if(mf in z):
            if(w[1] in z):
                count=count+1
    if(count>1):
        bb=d1[w[0]]
        second_le[w[0]+w[1]]=count
        config=count/bb
        cose=[w[0]+w[1],count,config]
        con.append(cose)
    count=0
main_third_le=l3[0]
l7=[]
# print(sorted_d)
# print(second_le)
for x in range(1,len(l3)):
    w=tuple(l3[x])
    if(main_third_le[0]==w[0]):
        l7.append(main_third_le+w[1])
        if(main_third_le[1]==w[0]):
            l7.append(main_third_le + w[0])
tc=0
third_le={}
for ax in l7:
    dd=tuple(ax)
    for z in f:
        if (main_third_le[0] in z):
            if (main_third_le[1] in z):
                if (dd[2]in z):
                    tc=tc+1
    if(tc>1):
        third_le[main_third_le+dd[2]]=tc
    tc=0
# print(third_le)
print(sorted_d)
print(second_le)
print(third_le)
print(apryori)
print(con)













