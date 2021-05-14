'''
This is one of the more expensive algorithms time wise, but constant base. 
We keep on sending maximum value to the last by comparing adjucent elements   


Time Complexity: O(n^2)
Space Complexity: O(1)

for more: https://en.wikipedia.org/wiki/Bubble_sort

'''
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

#Let's check with example:
print(bubbleSort([7,4,8,6,2,15,5])