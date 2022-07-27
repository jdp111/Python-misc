def in_range(nums, lowest, highest):
    
    for i in range (len(nums)):
        if nums[i] <= highest and nums[i] >= lowest:
            print (nums[i],"fits")

    # YOUR CODE HERE


in_range([10, 20, 30, 40, 50], 15, 30)            
