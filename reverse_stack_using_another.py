# #Reverse a stack using another stack
# def reverseStack(s1,s2):

#     #base case if len of s1<=1 no need to do anything simply return empty
#     if(len(s1)<=1):
#         return


#     #moving n-1 elements from s1 to s2
#     while(len(s1)!=1):
#         #keep on appending from s1 to s2
#         ele=s1.pop()
#         s2.append(ele)
#     #saving last element
#     lastelement=s1.pop()
#     #again moving s2 elements into s1 again
#     while(len(s2)!=0):
#         #removing elements from s2 
#         ele=s2.pop()
#         #appending elements into s1
#         s1.append(ele)
#     reverseStack(s1,s2)
#     #again appending saved element into s1
#     s1.append(lastelement)


# #here it is showing error but it is not a problem
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input("enter no of elements please"))
# s1=[int(ele) for ele in input().split()]
# s2=[]
# reverseStack(s1,s2)
# while(len(s1)!=0):
#     print(s1.pop(),end=' ')



#     #Note:the output first ask no of elements then add it
#     #ex:4
#     #1 2 3 4 this way stack is inserted first with 1,next 2...so onnn
#     #then output also 1 2 3 4 after printing

# sys. setrecursionlimit(limit): Set the maximum depth of the Python interpreter stack to limit. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.