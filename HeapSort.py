'''
This algorithms restructures array in a binary tree format such that for each node, its value sis greater than his left and right child.
After that, we know that max value would be at the top, we will then replace the first and last value so that max value will be last.
And then apply the heapify method on the remaining array (of length -1 and so on) to get the max value out of the remaining values at the top


Time Complexity: O(nlog(n))
Space Complexity: O(n), auxilary O(1)

for more: https://en.wikipedia.org/wiki/Heapsort

'''
#method to get max value at the top index
def heapify(arr,i,l):
    max_i= i
    left,right = 2*i + 1, 2*i + 2
    if left<l and arr[left]>arr[max_i]: max_i=left
    if right<l and arr[right]>arr[max_i]: max_i=right
    if max_i != i:
        arr[max_i],arr[i] = arr[i], arr[max_i]
        heapify(arr,max_i,l)


def heapSort(arr):
    l=len(arr)
    # call the heapify from middle of array as latter would be children
    for i in range(l//2 -1 , -1, -1): heapify(arr,i,l)
    for i in range(l-1,-1,-1):
        #take top value at index 0 to the last 
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr,0,i)
    return arr
    
#Let's check with example:
print(heapSort([7,4,8,6,2,15,5])