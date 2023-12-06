#Balanced paranthesis logic pls look note book so you can easily grasp concept
#Taking strin as  a input
def isBalanced(string):

#have to go to each character of that string,maintain a stack,match the paranthesis for (),{},[]
#and after iterating the whole string the stack should become empty,if the stack also doesnt become empty then also we need to return false

#maintain a stack like a list
    s=[]

#iterate on each character on this string
    for char in string:
        if char in '({[':
            #append that into the stack
            s.append(char)
        elif char == ')':
            #stack should not be empty,and it should end with () this pair
            #this below 2 condition should  be in order ,because if we do ulta it gives array index out of order


            #here -1 refers to last element of the stack
            if (not s or s[-1]!='('):
                return False
            #else will pop  the element from the stack
            s.pop()

#if the character is this "}"
        elif char == '}':
            if(not s  or s[-1]!='{'):
                return False
            s.pop()
        elif char == ']':
            if(not s or s[-1]!='['):
                return False
            s.pop()


    #after checking each character of the string i need to have stack should be empty
    if(not s):
        return True
    return False
            



string=input( "please enter string")
ans=isBalanced(string)
print(ans)