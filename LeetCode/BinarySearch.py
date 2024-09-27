def BinarySearch(nums, target):
    
    end = len(nums)-1
    start = 0
    
    for _ in range(len(nums)):
        
        middle = (start + end) //2
        
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            end = middle -1
        else:
            start = middle + 1
        
        if start > end:
            break   
    return -1
         

nums = [-1,0,3,5,9,12]
target = 9        

print(BinarySearch(nums, target))              