from stack_using_array_code import Stack

s=Stack()
s.push(12)
s.push(13)
s.push(15)

while s.isEmpty is False:
    print(s.pop())

s.top()


#the output be like from this 2 files i.e stackusingarraycode and this current file 
#15
#13
#12
#Hey! Stack is Empty!!