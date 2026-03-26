nums = [1,5,2,7,4]                      # nums = list("15274")
print(nums)

# To add an element to list
nums.append(8)

# To loop through all elements
for num in nums:
    print(num)

# To loop through index, element
for index, value in enumerate(nums):
    print(index,value)

if (10 in nums):
    print("Given value is exist in the list")
else:
    print("Give value is not exist in the list")

nums.sort()
print(nums)