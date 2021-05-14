'''
This is one of the more expensive algorithms time wise, but constant base. 
Basically we select the min value from the remaining array at each step, and replace it with current value  


Time Complexity: O(n^2)
Space Complexity: O(1)

for more: https://en.wikipedia.org/wiki/Selection_sort

'''
def selectionSort(arr):
    for i in range(len(arr)-1):
        minI=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minI]: minI=j # find index with min value
        if i!=minI: arr[i],arr[minI] = arr[minI], arr[i] 
    return arr

#Let's check with example:
print(selectionSort([7,4,8,6,2,15,5])