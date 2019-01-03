from functools import reduce as re
mylist=[1,2,3,4,5,6]
print(mylist)
newlist=[x*3 for x in mylist]
print(newlist)
sum1=re(lambda x,y:x+y,mylist)
print(sum1)
sum2=re(lambda x,y:x+y,newlist)
print(sum2)
