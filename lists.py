# -*- coding: utf-8 -*-

mylist = [1, 'two', 3,1]
print(len(mylist)) # число элементов в списке
print (mylist[0]) # печать первого елемента

mylist.append("new")

print ("added", mylist)

mylist.pop(0)

print ("deleted", mylist)