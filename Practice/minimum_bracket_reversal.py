#MIN BRACKET REVERSAL:the question is from coding ninja assignment


#easy dry run dont confuse
def min_bracket_reversal(expression):
    #if the length of the expression is odd it cant be balanced
    if len(expression)%2!=0:
        return -1
    stack=[]
    for bracket in expression:
        if bracket == "{":
            stack.append(bracket)
            #if it is an "}" bracket then
        else:
            #this condition is for "}"
    #in that also checking another condition stack and stack last element is "{" then pop it
            if stack and stack[-1] == "{":
                stack.pop()
            #if the above condition fails then 
            else:
                stack.append(bracket)
    
    unbalanced_opening=0
    while stack and stack[-1]== '{':
        #if stacks last is {  the pop it
        stack.pop()
        unbalanced_opening+=1

#minimum reversals required
    return(len(stack)//2) + (unbalanced_opening // 2)

expression=input().strip()
result=min_bracket_reversal(expression)
print(result)
