def mergeSort(List, start, end, tempList):
    if start < end:
        mid = (start + end) // 2
        mergeSort(List, start, mid, tempList)
        mergeSort(List, mid + 1, end, tempList)
        merge(List, start, mid, end, tempList)

def merge(List, start, mid, end, tempList):
    leftIndex = start
    rightIndex = mid + 1
    sortedIndex = start

    # Compare elements from both halves and store in tempList
    while leftIndex <= mid and rightIndex <= end:
        if List[leftIndex] <= List[rightIndex]:
            tempList[sortedIndex] = List[leftIndex]
            leftIndex += 1
        else:
            tempList[sortedIndex] = List[rightIndex]
            rightIndex += 1
        sortedIndex += 1

    # Copy remaining elements from the left half
    while leftIndex <= mid:
        tempList[sortedIndex] = List[leftIndex]
        leftIndex += 1
        sortedIndex += 1

    # Copy remaining elements from the right half
    while rightIndex <= end:
        tempList[sortedIndex] = List[rightIndex]
        rightIndex += 1
        sortedIndex += 1

    # Copy sorted elements back to the original list
    for i in range(start, end + 1):
        List[i] = tempList[i]

# Example usage:
List = [38, 27, 43, 3, 9, 82, 10]
tempList = [0] * len(List)
mergeSort(List, 0, len(List) - 1, tempList)
print(List)
