def KLargest(arr, k):
    arr.sort()
    return arr[-k : ][:: -1]

if __name__ == "__main__":
    nums =  [1, 23, 12, 9, 30, 2, 50]
    print(KLargest(nums, 3))