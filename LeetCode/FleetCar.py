'''
There are n cars at given miles away from the starting mile 0, traveling to reach the
mile target.

You are given two integer array position and speed, both of length n, where position[i] 
is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed 
of the slower car.

A car fleet is a car or cars driving next to each other. The speed of the car fleet is 
the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as 
part of the car fleet.

Return the number of car fleets that will arrive at the destination.
'''


def carFleet(target, position, speed):
    
    timeArray =[]
    answer = []
    
    for i in range(len(position)):
        time =  (target - position[i]) / 2
        timeArray.append(time)
    
    stack = []
    for i in range(len(timeArray)):
        ctr = 1
        for j in range(i+1, len(timeArray)):
            if timeArray[i] == timeArray[j]:
                ctr +=1
                
        
    
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]                

carFleet(target, position, speed)