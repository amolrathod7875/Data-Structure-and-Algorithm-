class Solution:
	def mergeOverlap(self, arr):
	    if not arr :
	        return []
	        
	    arr.sort(key=lambda x:x[0])
	    result= [] 
	    prev_interval = arr[0]
	    
	    for i in range(1, len(arr)):
	        if arr[i][0] <= prev_interval[1]:
	            prev_interval[1] = max(prev_interval[1], arr[i][1])
	        else:
	           result.append(prev_interval)
	           prev_interval = arr[i]
	           
	    result.append(prev_interval)
	    return result
