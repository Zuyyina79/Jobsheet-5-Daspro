# In[8]:

foo = ["Belajar", "Python", "di", "Duniailkom"]
bar = [100, 200, 300, 400]
baz = ["Python", 200, 6.99, True]
  
print(foo)
print(bar)
print(baz)


# In[9]:

foo = ["Belajar", "Python", "di", "Duniailkom"]
bar = [100, 200, 300, 400]
baz = ["Python", 200, 6.99, True]
 
print(type(foo))
print(type(bar))
print(type(baz))


# In[10]:

foo = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(foo)
  
foo[0] = 'Belajar'
foo[3] = False
print(foo)


# In[13]:

foo = ["Belajar", "Python", "di", "Duniailkom"]
print(type(foo))
foo = ("Belajar", "Python", "di", "Duniailkom")
print(type(foo))
