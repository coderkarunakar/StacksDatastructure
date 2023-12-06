
#Stack is similar to Dynamic Array/List(it follows the LIFO)
#Note:what ever happens in list it also happens in Stack as well
#Note:For Queue we can not use List(we can but that will not be efficient which takes O(n)Times)
#so we should not use Queue as a list in python,we have a inbuild library Queue from Python 3 on wards,we can use queue class from this library

import queue

#inbuilt stack as a list
s=[1,2,3]
s.append(4)
s.append(5)

#This gives which element is getting poped
print(s.pop())
print(s.pop())


#inbuild queue

#we have made an object of that class(queue)
q=queue.Queue()
#we have funcitonlity like put get empty and etc
#lets say i want to enque elements like queue
q.put(1)
q.put(2)
q.put(3)
q.put(4)

#we have functionality called .empty
while not q.empty():
    #keep on removing elements
    #.get deques(remove) the element and it prints the element which was dequed
    print(q.get())


#Queue follows FIFO property first in first out 