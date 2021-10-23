# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
nums = input("Nums = ")
num_list = list(nums)
target = int(input("Target = "))
num_length = len(num_list)
got_target = True
for first_num in range(0, num_length):
    for second_num in range(0, num_length):
        if int(num_list[first_num]) == int(num_list[second_num]):
            pass
        elif int(num_list[first_num]) + int(num_list[second_num]) == target:
            print([first_num, second_num])
            break
    if int(num_list[first_num]) + int(num_list[second_num]) == target:
        break










