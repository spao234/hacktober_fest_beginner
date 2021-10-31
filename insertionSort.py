# Insertion Sort 
def insertion_sort(unsortedList):  
  
        # Outer loop to traverse through 1 to len(unsortedList)  
        for i in range(1, len(unsortedList)):  
  
            value = unsortedList[i]  
  
            # Move elements of unsortedList[0..i-1], that are  
            # greater than value, to one position ahead  
            # of their current position  
            j = i - 1  
            while j >= 0 and value < unsortedList[j]:  
                unsortedList[j + 1] = unsortedList[j]  
                j -= 1  
            unsortedList[j + 1] = value  
        return unsortedList  
            # Driver code to test above  
  
exampleList = [10, 5, 13, 8, 2]  
print("The unsorted list is:", exampleList)  
  
print("The sorted list is:", insertion_sort(exampleList))  
