class Stack:
    def __init__(self):
        #declaring a private array so we gave to underscores __
        self.__data=[]
        #here took item because we are inserting some items so item is taken
    def push(self,item):
        #we are inserting into the item
        self.__data.append(item)
    def pop(self):
        #if our self values are empty then print it
        if self.isEmpty():
            print("hey stack is empty")
            return
            #removes the last value of the array
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("hey stack is empty")
            return
            #taking length of array and -1 because len index starts from 1,2....,but array index is from 0,1,2...
        return self.__data[len(self.__data)-1]

    def size(self):
        #in order to get size get its length
        return len(self.__data)

    def isEmpty(self):
        #if length is zero then the array is empty and return true else false
        return self.size()==0
