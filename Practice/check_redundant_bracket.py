
#For better understanding please look into the Notes:
#check redundant bracket problem
def check_redundant_brackets(expression):
    stack = []
    for character in expression:
        #checks the current character is not a closing bracket
        if character != ')':
            #if it is  not a closing character then it appends into the stack
            stack.append(character)
        #enters into the block if the closing character is ")"
        else:
            #initialise a variable found to keep  track of wheather an operator is found between brackets
            #first initializing found =false first
            found = False
            #enters a while loop if the stack is not empty,and the top of the stack is not an opening bracket
            while stack and stack[-1] != '(':
                #checks if the poped character is an operator,if so sets found =True
                if stack.pop() in ['+', '-', '*', '/']:
                    found = True
                #pops the opening bracket "(" from the stack
            stack.pop()  # popping '('
            #checks if found is still false meaning no operator was found between the brackets
            if not found:
                #if no operator found between the brackets,it returns true indicating that redundant bracket is found
                return True  # Redundant bracket found
    #if the loop completes and no redundant brackets are found,it returns false 
    return False  # No redundant bracket found


    #a big note if it founds a "(" then again it restarts the checking and sets found = "False "
    #as well

# Example usage:
expression =input("please enter the expression")
result = check_redundant_brackets(expression)
if result:
    print("Redundant brackets found")
      #ex:((a+b)) here brackets are not necessary so redundant ,True
else:
    print("No redundant brackets")
          #(a+(b*c)),(a+b) here brackets are necessary to show operations like * and +so it is not redundant so it is False
