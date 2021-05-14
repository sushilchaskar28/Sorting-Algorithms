'''
This algorithms has divide and conquer technique.
Go on dividing array till there is only one element. Then recursively start creating subarrays in ascending order 
Recurssion concept is effective in this algorithm

Time Complexity: O(nlog(n)) 
Space Complexity: O(n)

For more: https://en.wikipedia.org/wiki/Merge_sort

'''

def mergeSort(arr):
    if len(arr)>1:
    m=len(arr)//2
    l=mergeSort(arr[:m]) #Divide and merge to get left sorted array
    r=mergeSort(arr[m:]) # Divide and merge to get right sorted array
    
    # merge two subarrays 
    i,j,k=0,0,0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
        arr[k]=l[i]
        i+=1
        else:
        arr[k]=r[j]
        j+=1
        k+=1
    while i<len(l):
        arr[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        arr[k]=r[j]
        j+=1
        k+=1
    return arr
    
#Let's check with example:
print(mergeSort([7,4,8,6,2,15,5])