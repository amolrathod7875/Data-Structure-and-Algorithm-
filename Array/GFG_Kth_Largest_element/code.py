def findkthlargest(nums, k):
    nums.sort()
    return nums[-k]

if __name__== "__main__":
    nums = [3,2,1,5,6,4]
    print(findkthlargest(nums, 2))