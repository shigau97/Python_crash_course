#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted!"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Shivani','gautam')
print(musician)


# In[3]:


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted!"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Shivani','sharma','gautam')
print(musician)


# In[4]:


def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted!"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Shivani','sharma','gautam')
print(musician)

musician = get_formatted_name('Shivani','Gautam')
print(musician)


# In[5]:


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("\nEnter 'q' to exit")
    
    f_name = input("first_name: ")
    if f_name == 'q':
        break
    l_name = input("last_name:")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    
    
    
    


# In[14]:


def city_country(city_name, country_name):
    """Return the city and country of that city!"""
    combi = f"{city_name.title()}, {country_name.title()}"
    return combi.title()
cite = city_country('Karnal','india')
print(cite)


# In[19]:


def greet_users(names):
    """Print a simple greeting to each user in the list!"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
        
usernames = ['mike','saumya','hannah']
greet_users(usernames)


# In[22]:


#Stating with some designs we want to print 
unprinted_designs = ['phone','pendant','box']
completed_design = []

#simulate printing of each design until none are left
#moving each design to completed design after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_design.append(current_design)

#display alll completed models.
print("\nThe following models have been printed:")
for completed_designs in completed_design:
    print(completed_designs)


# In[32]:


def print_models(unprinted_design, completed_design):
    """Simulating and printing each design, untilll all are done, moving each to completed"""
    
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_design.append(current_design)
        
def show_completed_design(completed_design):
    """showing all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_designs in completed_design:
        print(completed_designs)
        
unprinted_design = ['shoe','socks','box','phone']
completed_design = []

print_models(unprinted_design[:], completed_design)
show_completed_design(completed_design)

print(f"\n{unprinted_design}")


# In[35]:


def show_messages(container_messages):
    """prints the messages"""
    for container_message in container_messages:
        print(f"\nThe messages are: {container_message}")
        
container_messages = ['this is cool', 'make things better', 'damn, that happens!']
empty_container = []

show_messages(container_messages)


# In[41]:


def send_messages(container_messages, empty_container):
    while container_messages:
        current_messages = container_messages.pop()
        print(f"Printing message: {current_messages}")
        empty_container.append(current_messages)        
        
def show_messages(container_messages):
    """prints the messages"""
    for container_message in container_messages:
        print(f"\nThe messages are: {container_message}")
        
container_messages = ['this is cool', 'make things better', 'damn, that happens!']
empty_container = []

send_messages(container_messages[:], empty_container)
show_messages(container_messages)


# In[42]:


def make_pizza(*toppings): #Arbitrary number of arguments can be added into it
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza('pepperoni')
make_pizza('onion','green peppers', 'extra cheese')


# In[43]:


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('shivani','gautam', location = 'Mankato')
print(user_profile)


# In[ ]:




