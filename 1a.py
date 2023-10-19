#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=5
print(a)
print(type(a))
b=6.7
print(b)
print(type(b))
c=complex(2,5)
print(c)
print(type(c))


# In[12]:


c='beautiful'
d='flower'
print(c)
print(type(c))
print(c[0])
print(c[2:5])
print(c[2:])
print(c+" "+d)
print(c*2)


# In[13]:


a=True
b=False
print(type(a))
print(type(b))


# In[38]:


list=["apple","orange","cherry","banana"]
list2=["monkey","tiger"]
print(list)
print(list[0])
print(list[1:-1])
print(list[2:])
for i in range(0,2):
    print(list)
print(list+list2)


# In[39]:


tuple=("carrot","pomegranate","brinjal","onion")
tuple1=("chilly","tomato")
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple*2)
print(tuple+tuple1)


# In[36]:


dict={
    "one":"Bus",
    "Two":"car",
    "Three":"Train"
}
print(dict)
print(dict["one"])
print(dict["Two"])
print(dict.keys())
print(dict.values())


# In[31]:



a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter a  decimal number:"))
print("Addition: ",a+b)
print("Difference:",a-b)
print("Product:",a*b)
print("Quotient:",a/b)
print("Modulus:",a%b)
print("Floor:",math.floor(c))
print("Exponent:",a,"^",b,"=",a**b)


# In[33]:


a=input("Enter the first string:")
b=input("Enter the second string:")
c=a+" "+b
print("after concatenation:",c)


# In[37]:


str1=input("Enter a String :")
print("Length:",len(str1))


# In[ ]:


str1=input("Enter a string in lower case:")
print(str1.upper())


# In[44]:


str1=input("Enter a string in Upper case:")
print(str1.lower())


# 

# In[43]:


str1=input("Enter a String:")
print(str1.capitalize())


# In[55]:


str1=input("enter a string:")
str2=input("Enter a substring:")
c=str1.index(str2)
print(c)


# In[54]:


str1="hello$world"
c=str1.split("$")
print(c)


# In[56]:


str1=input("Enter a String:")
str2=input("Enter the string to be replaced")
str3=input("enter the sting to replace:")
c=str1.replace(str2,str3)
print(c)


# In[64]:


a=10
b=8
print(a>9 and b>1)
print(a>5 and b>9)
print(a>11 and b>7)
print(a>20 and b>67)


# In[68]:


a=25
b=30
print(a>20 or b>10)
print(a>10 or b>35)
print(a>30 or b>20)
print(a>30 or b>40)


# In[73]:


print(not True)
print(not False)


# In[74]:


a=5
if a%2==0:
    print("Even")
else:
    print("Odd number")


# In[75]:


a=4
b=2
c=9
if(a>b and a>c):
    print(a," is the Largest number")
elif(b>a and b>c):
    print(b," is the Largest number")
else:
    print(c," is the Largest number")


# In[2]:


limit=int(input("Enter a limit:"))
Sum=0
for i in range(1,limit+1):
    if i%2!=0:
        Sum=Sum+i
print(Sum)


# In[1]:


l=int(input("Enter a limit: "))
for i in range(1,l+1):
    print(i)


# In[11]:


a=int(input("Enter a number:"))
Sum=0
while(a>0):
    rem=a%10
    Sum=Sum+rem
    a=a//10
print(Sum)


# In[39]:


n=int(input("Enter a limit:"))
for i in range(1,n+1):
    odd=False
    if(i%2!=0):
        odd=True
    if odd:
        print(i)
        
        
        


# In[41]:


l1=[1,3.5,'a','b',True]
print(l1)
l1.append("c")
print(l1)


# In[42]:


print(l1.pop())


# In[49]:


l1.insert(3,"o")
print(l1)


# In[50]:


l1.remove("a")
print(l1)


# In[51]:


l1=[2,3,'a']
l2=[1,'b']
l1.append(l2)
print(l1)


# In[52]:


l1.remove(l2)
print(l1)


# In[54]:


l1.extend(l2)
print(l1)


# In[56]:


a=[5,8,1,10,67,3,4]
a.sort()
print(a)


# In[67]:


num=[1,2,3,4,5]
sq=[]
for i in num:
    sq.append(pow(i,2))
print(sq)
    


# In[68]:


numbers=[0,1,2,3,4,5,6,7,8,9,10]
print(numbers[1],numbers[-1])


# In[69]:


sliced=numbers[5:11]
print(sliced)


# In[71]:


slice1=numbers[5:]
print(slice1)


# In[72]:


sliced=numbers[:7]
print(sliced)


# In[73]:


slice2=numbers[-2:]
print(slice2)


# In[77]:


numbers=[*range(1,8)]
print(numbers)


# In[78]:


square=[x**2 for x in numbers]
print(square)


# In[80]:


odd_square=[x**2 for x in numbers if x%2!=0]
print(odd_square)


# In[81]:


A=[4,6,8,9]
AxA=[(a,b) for a in A for b in A if a!=b ]
print(AxA)


# In[85]:


student={'name':'swetha','age':22}
print(student['name'])


# In[86]:


print('name' in student)


# In[88]:


print('class' in student)


# In[89]:


student['class']="MCA"
print(student)


# In[90]:


for item in student:
    print(item,student[item])


# In[96]:


for(key,value) in student.items():
    print(key.capitalize(),'\t:\t',value)
print(student.keys())


# In[97]:


def square(number):
    return pow(number,2)
s=square(5)
print(s)


# In[98]:


def isPrime(number):
    for factor in range(2, (number//2)+1):
        if number%factor == 0:
            return False
        return True

number = int(input('Enter the number '))
print(isPrime(number))


# In[100]:


def printPrimes(llimit, ulimit):
    for num in range(llimit,ulimit+1):
        if isPrime(num)==True:
            print(num,end=' ')
printPrimes(5,20)


# In[101]:


def swap(x,y):
    t=x
    x=y
    y=t
    return x,y
a=5
b=7
a,b=swap(a,b)
print(a,b)


# In[ ]:




