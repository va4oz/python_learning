# -*- coding: utf-8 -*-

mylist = [1, 'two', 3,1]
print(len(mylist)) # число элементов в списке
print (mylist[0]) # печать первого елемента

mylist.append("new")

print ("added", mylist)

mylist.pop(0)

print ("deleted", mylist)

superlist = [[1,2,3],[4,5,6]]
print superlist
print (superlist[0][1]) # получаем 2-й элемент из 1-го x списка