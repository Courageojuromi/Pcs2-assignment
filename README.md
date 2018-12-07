# Pcs2-assignment
 This is a bench analysis of algoirthm or function defined as QuickSort and MergeSort.
 QuickSort is an efficient sorting algorithm,serving as a method for placing the elements of an array in order(it can be about two or three times faster than its main competitors, MergeSort).QuickSort is an excellent general purpose sort  although the 3-way partitioning version should always be used instead.Pivot element can be any element from the array, it can be the first element, the last element or any random element.
How QuickSort works select am element as pivot defined as arr[high]
The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
takes a string and seperates  i = (low - 1)  
# index of smaller element If current element is smaller than or
 # equal to pivot
   if arr[j] <= pivot:
            # increment index of smaller element 
            and return (i = i + 1)
   #function to do the QuickSort # pi is partitioning index, arr[p] is now # at right place
   you define the MeasureThis function and create a list and use the for loop to iterate all values 
 
 
 MergeSort is a divide and conquer algorithm,it divides input array into two halves calls itself for the two halves and than merges the two sorted halves. The merge() function is used for combining two halves .
In Merge Sort, the given unsorted array with n elements, is divided into n subarrays, each having one element, because a single element is always sorted in itself. Then, it repeatedly merges these subarrays, to produce new sorted subarrays, and in the end, one complete sorted array is produced.
Using this steps 
We take a variable x and store the starting index of our array in this. And we take another variable  l and store the last index of array in it.
Then we find the middle of the array using the formula len(x)//2 and mark the middle index as L, and break the array into two subarrays, from L to R and from x + 1 to l index.
Then we divide these 2 subarrays again, just like we divided our main array and this continues.Once we have divided the main array into subarrays with single elements, then we start merging the subarrays.
Merge Sort is quite fast, and has a time complexity of O(n*log n). It is also a stable sort, which means the "equal" elements are ordered in the same order in the sorted list.
  
Import the time.it function implenting it on the qicksort and mergesort, what the time.it ? to check how fast the functions are and in this two functions we see that Quicksort is faster than the Mergesort
