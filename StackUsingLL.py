from Node import Node
class Stack:
    def __init__(self):
        #making this things as private because for user it is Stack but for us it is implementing using LL ,so user should not know about it .so am making this as private
        self.__head=None
        self.__count=0
    def push(self,item):
        newNode=Node(item)
        #Note:here the nodes are not creating in forward direction ,we are creating in backward direction like  3->2->1->None,thats why after new node head is pointing
        newNode.next=self.__head
        #again head pointing is changing like after creating of new node that new node will be our head pointer
        self.__head=newNode
        #for every addition  of new node the count get increased 
        self.__count=self.__count+1

    def pop(self):
        if self.isEmpty() is True:
            print("Hey the stack is Empty!")
            return
            #this data is comming from the Node file created,this data is pointing to first value
        data=self.__head.data
        #changing head position head's next value as head now 3->2->1->None 
        self.__head=self.__head.next
        #every time head position changes count value also getting reduced
        self.__count=self.__count-1
        #finally return the data
        return data
    def top(self):
        if self.isEmpty() is True:
            print("Hey the stack is Empty!")
            return
        data=self.__head.data
        return data

    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0