"""
Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering
the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval
to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is
empty.

# pseudo code
1. create variables to hold start point, end point, found and index
    1.1 get the last item by using the len - 1
    1.2 set found to False and index to -1:
        - 1 because it means no index found
2. iterate through the list (while loop --personal preference)
3. get the mid item by using first+last item
4. check if the index of the mid-item is equal item
    4.1 if it equates then set found = True and change index to equal mid
    4.2 if it does equate
        4.2.1 check if item is less item from item_list[index]
            4.2.1.1 remove one from mid and assign it to last.
                    - This helps in searching towards left or/and right


"""
def binary_search(item_list, item ):
    first = 0
    last = len(item_list)-1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last)//2
        if item_list[mid] == item:
            found = True
            index = mid
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


print(binary_search([1,2,3,5,8], 1))