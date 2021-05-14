'''
This is one of the more expensive algorithms time wise, but constant base. 
We insert a value at the correct index of already sorted array (left to right)  


Time Complexity: O(n^2)
Space Complexity: O(1)

for more: https://en.wikipedia.org/wiki/Insertion_sort

'''
def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j] #swap until you find the correct position
            j-=1
    return arr

#Let's check with example:
print(insertionSort([7,4,8,6,2,15,5])