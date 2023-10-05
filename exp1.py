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


# In[ ]:




