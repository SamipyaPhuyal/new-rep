def index():
    nums = [1,3,5,6]
    target = 5
    if(target<nums[0]):
            return 0
    for i in range(len(nums)-1):
        if(target<nums[0]):
            return 0
        if(nums[i]==target):
            return i
            break
        elif(target not in nums):
            if(target>nums[i] and target<nums[i+1]):
                return (i+1)
                break
            elif target>nums[(len(nums)-1)]:
                return (len(nums))
                break
print(index())
#nums[1]
#target =0
