'''
This algorithms has two main functions : 
1. find partition point such that all the values left to it are less than  and values right to it are greater than the partition value
2. Recurssively call the quickSort method on left and right sub arrays 


Time Complexity: O(nlog(n)) , worst case: o(n^2)
Space Complexity: O(log(n)) because of the recurssion stack

for more : https://en.wikipedia.org/wiki/Quicksort
'''
#get partition index
def partition(arr,start,end):
    l=arr[end]
    i=start-1
    for j in range(start,end):
        if arr[j]<l:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1


def quickSort(arr,start,end):
    if start<end:
        p=partition(arr,start,end)
        #call quicksort on left and right subarrays
        quickSort(arr,start,p-1)
        quickSort(arr,p+1,end)
    
#Let's check with example:
arr=[7,4,8,6,2,15,5]
quickSort(arr)
print(arr)