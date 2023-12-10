#stock span code for question purpose please look into the notes 

def calculate_span(prices):
    n = len(prices)
    stack = []
    spans = [0] * n
#iterates till len of the given prices
    for i in range(n):
        #travels till end of the stack and current price is less than the last value of the stack
        while stack and prices[stack[-1]] < prices[i]:
            #it pops from the stack
            stack.pop()
#if stack is empty it assigns span as i+1,
#if stack is not empty it calculates the span as difference between the current day(i) and the index of the most recent day in the stack(stack[-1])
        spans[i] = i + 1 if not stack else i - stack[-1]
#finally appends to the stack
        stack.append(i)
#returns the spans
    return spans

# Reading input
n = int(input())
prices = list(map(int, input().split()))

# Calculating spans
result = calculate_span(prices)

# Printing the spans
print(*result)
