#!/usr/bin/env python
# coding: utf-8

# # my own reduce()

# In[3]:


def myredu(anyfunc,s):
    r=s[0]
    for i in s:
        r=anyfunc(r,i)
    return r
def mul(x,y):
    return x*y
print(str(myredu(mul,[1,2,3,4])))


# # my own filter 

# In[2]:


def myfil(any,s):
    r=[]
    for i in s:
        if any(i):
            r.append(i)
    return r
def pos(a):
    if(a>0):
        return True
    else:
        return False
print(str(myfil(pos,[0,-1,5,6,-8,111])))


# # list comprehension

# In[1]:


word = "ACADGILD"
print(list(word))
input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))
input_list = ['x','y','z']
li=[]
for i in input_list:
    for j in range(1,5):
        a=i*j
        li.append(a)
print(li)
input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))
input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))
input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# # longestword()

# In[6]:


from functools import reduce
list_words = ["This","is","a","beautiful","morning"]

def longestWord(list_words):
 return reduce( (lambda x,y:y if len(y) > len(x) else x), list_words )

print ('Longest word in array ["This","is","a","beautiful","morning"] => ' + longestWord(list_words) )


# # task 2: area

# In[7]:


class Triangle:
 def __init__(self, side1, side2, side3):
  self.side1 = side1
  self.side2 = side2
  self.side3 = side3
  print ("Initialised Triagle super class [" +  str(side1) + "," + str(side2) + "," + str(side3) + "]")

class Triangle_Utilities(Triangle):
 
 def __init__(self, side1, side2, side3):
  print ("Initialised Utils Child class" )
  super(Triangle_Utilities, self).__init__(side1, side2, side3)

 def get_area(self):
  s = (self.side1 + self.side2 + self.side3)/2
  print (str(s))
  return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5

instance = Triangle_Utilities(3,4,5)
print ("Area of triangle = " + str(instance.get_area()) )


# # filter_long_words()

# In[8]:


class list_Utilities:
 def __init__(self, wordlist):
  self.wordlist = wordlist
  print ("Initialised list_Utilities object")

 def filter_long_words(self, n):
  return list(filter(lambda x:len(x) > n, self.wordlist))

instance = list_Utilities(["This","is","a","beautiful","day"])
print ("New List of Words  => " + str(instance.filter_long_words(3)) ) 
 


# # map list of words into list of integers representing lengths

# In[9]:


wordlist = ["This", "is", "a", "beautiful", "day"]

def wordlength(wordlist):
 return list(map(lambda x: len(x), wordlist))

print ("word lengths in array => " + str(wordlength(wordlist)))


# # vowel check

# In[10]:


def vowel_check(char):
 if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
  return True
 else:
  return False
char = input("Enter character: ");
if (char.isalpha() == False):
 exit();
if (vowel_check(char)):
 print(char, "is a vowel.");
else:
 print(char, "is not a vowel."); 


# In[ ]:




