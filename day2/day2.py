safe = 0

def is_safe(nums):
    if nums != sorted(nums) and nums != sorted(nums, reverse=True):
        return False
    is_safe = True
    for i in range(len(nums) - 1):
        if not (1 <= abs(nums[i] - nums[i+1]) <= 3):
            is_safe = False
            break
    if is_safe:
        return True
    return False

with open("input.txt", "r") as file:
    for line in file:
        nums_str = line.split()
        nums = [int(s) for s in nums_str]

        if is_safe(nums):
            safe += 1
        else:
            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i+1:]
                if is_safe(new_nums):
                    safe += 1
                    break

    
print("Safe: ", safe) 


