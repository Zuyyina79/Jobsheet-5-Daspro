# coding: utf-8

# In[7]:

#Python program to demonstrate
#Creation of Array

#importing "array" for array creations
import array as arr

#creating an array with integer type
a = arr.array('i',[1,2,3])

#printing original array 
print ("The new created array is : ", end="")
for i in range (0,3):
    print (a[i], end="")
print()

#creating an array with float type
b = arr.array('d', [2.5,  3.2,  3.3])

#printing original array
print ("The new created array is : ", end ="")
for i in range (0, 3):
    print (b[i], end ="")


# In[2]:

#Python program to demonstrate
#Adding Elements to a Array
#importing "array" for array creations
import array as arr

#array with int type
a = arr.array('i', [1,2,3])

print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()

#inserting array using
#insert() function
a.insert(1,4)

print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()

#array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print ("Array before insertion :", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print()

#adding an element using append()
b.append(4.4)

print ("Array after insertion : ", end =" ")
for i in (b):
    print (i, end =" ")
print(i)


# In[4]:

#Python program to demonstrate
#accessing of element from list

#importing array module
import array as arr

#array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

#accessing element of array
print("Access element is: ", a[3])

#array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

#accessing element of array
print("Access element is: ", b[1])

#accessing elemet of array
print("Aceess element is: ", b[2])



# In[6]:

#Python program to demonstrate
#Removal of elements in a Array

#importing "array" for array operations
import array

#initializing array with array values
#initializes array with signed integers
arr = array.array('i', [1,2,3,1,5])

#printing original array
print ("The new created array is : ", end ="")
for i in range (0, 5):
    print (arr[i], end =" ")

print ("\r")

#using pop() to remove element at 2nd position
print ("The popped element is : ", end ="")
print (arr.pop(2))

#printing array after popping
print ("The array after popping is : ", end ="")
for i in range (0, 4):
    print (arr[i], end =" ")
    
print("\r")

#using remove() to remove 1st occurence of 1
arr.remove(1)

#printing array after removing
print ("The array after removing is : ", end ="")
for i in range (0, 3):
    print (arr[i], end =" ")
    


# In[7]:

#Python program to demonstrate
#slicing of elements in a Array

#importing array module
import array as arr

#creating a list
l = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end =" ")
    
#Print elements of a range 
#using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

#Print elements from a
#pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)

#Printing elements from
#beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)
