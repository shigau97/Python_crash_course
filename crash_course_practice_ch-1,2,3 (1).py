
# coding: utf-8

# In[1]:


print("Hello world!")


# In[3]:


message = "hello world"
print(message)


# In[4]:


name = "ada lovelace"
print(name.title())


# In[6]:


name = "Ada Lovelace"
print(name.upper())
print(name.lower())


# In[7]:


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


# In[10]:


first_name = "Shivani"
last_name = "gautam"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


# In[11]:


message = f"Hello, {full_name.title()}!"


# In[12]:


print(message)


# In[13]:


print("\tpython")


# In[14]:


print("shivani's python code \n python")


# In[15]:


0.2+0.1


# In[16]:


x, y, z = 0, 0, 0


# In[17]:


FAVORITE_NUMBER = 19


# In[18]:


# Its just a comment
#Let's see!


# In[20]:


import this


# In[21]:


bicycles =['trek','cannondale', 'redline', 'specialized']


# In[22]:


print(bicycles)


# In[23]:


print(bicycles[0])


# In[24]:


print(bicycles[0,1,2,3])


# In[25]:


bicycles.append('hero')
print(bicycles)


# In[26]:


del bicycles[4]


# In[27]:


print(bicycles)


# In[28]:


bicycles.remove('trek')


# In[29]:


print(bicycles)


# In[30]:


too_expensive = 'redline'
bicycles.remove(too_expensive)
print(bicycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# In[31]:


guests = ['v.k.sharma','goyals','dubeys','gautams']
print(f"\n {guests.title()}, you are invited for the dinner!")


# In[32]:


guests = ['v.k.sharma','goyals','dubeys','gautams']
print(f"\n {guests[0].title()}, you are invited for the dinner!")
print(f"\n {guests[1].title()}, you are invited for the dinner!")
print(f"\n {guests[2].title()}, you are invited for the dinner!")
print(f"\n {guests[3].title()}, you are invited for the dinner!")


# In[18]:


guests = ['v.k.sharma','goyals','dubeys','gautams']
print(f"\n {guests[0].title()}, you are invited for the dinner!")
print(f"\n {guests[1].title()}, you are invited for the dinner!")
print(f"\n {guests[2].title()}, you are invited for the dinner!")
print(f"\n {guests[3].title()}, you are invited for the dinner!")
print(f"\n Bad news! {guests.pop(2)} can't make it to dinner.\n")
print(guests)
guests.append('sharmas')
print(f"\nNew guests are included:\n{guests[3]}")
print(guests)


# In[45]:


guests.insert(4, 'vermas')
print(guests)


# In[1]:


cars = ['bmw', 'audi', 'toyata','subaru']
cars.sort()
print(cars)


# In[2]:


cars.sort(reverse=True)
print(cars)


# In[3]:


print(sorted(cars))


# In[4]:


print(cars)
cars.reverse()
print(cars)


# In[5]:


len(cars)


# In[8]:


places = ['america', 'australia', 'bali', 'singapore','dubai']
print('This is my original order of list of places i want to visit:\n')
print(places)
print('This is my sorted list of places: \n')
print(sorted(places))
print('My list is still in original order: \n')
print(places)


# In[11]:


places.reverse()


# In[13]:


print(places)


# In[16]:


places.sort()
print(places)
places.sort(reverse=True)
print(places)


# In[19]:


print(f"Number of people i am inviting to my dinner: \n {len(guests)}")


# In[20]:


magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(magician)


# In[21]:


for place in places:
    print(place)


# In[24]:


for place_sorted in places: #this is just trial not correct, trying. Thanks!
    print(sorted(place_sorted))


# In[26]:


for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print("Thank you! for putting up such a great show!")


# In[27]:


for value in range(1, 5):
    print(value)


# In[28]:


for value in range(6):
    print(value)


# In[29]:


numbers = list(range(1,6))
print(numbers)

