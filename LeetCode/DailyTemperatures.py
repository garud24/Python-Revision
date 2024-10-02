'''
Stack Content: The stack should store indices of temperatures, not the actual temperatures. 
This is because you want to calculate the difference in days between the current day and the day with a warmer 
temperature.
Approach:

1. Iterate from Left to Right: As you traverse the list, for each day:

- Compare the current temperature with the temperature at the index stored at the top of the stack.
If the current temperature is warmer than the temperature at the index stored at the top of the stack, 
it means you've found the next warmer day for that stored index.
- Pop the index off the stack and calculate the difference between the current index and the popped index.
- Keep popping the stack while the current temperature is greater than the temperature at the indices in the stack.
- If the current temperature is not warmer, push the current index onto the stack to check later.'''


def dailyTemperatures(temperatures):
    answer = [0]*len(temperatures)
    stack = []
    
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            answer[stackIndex] = i - stackIndex
        stack.append([t,i])
    
    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))        

#Answer should be : [1,1,4,2,1,1,0,0]

