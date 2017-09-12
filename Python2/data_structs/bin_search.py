# our input_array has distinct arrays.
# we return position of value in list
def binary_search_recursive(input_array, value):
    res = -1
    size = len(input_array)
    size_half_1 = size/2

    half_1 = input_array[0:size_half_1]
    for v in half_1:
        if v==value:
            res = input_array.index(v)

    half_2 = input_array[size_half_1:size]
    for v in half_2:
        if v==value:
            res = input_array.index(v)
    if res == -1 and len(half_1)>1:
        res = binary_search_recursive(half_1,value)
        if res == -1 and len(half_2)>1:
            res = binary_search_recursive(half_2,value)
    return res

def binary_search_iterative(input_array, value):
    low = 0
    high = len(input_array)-1
    while (low<=high):
        mid = (low+high)/2
        if input_array[mid]==value:
            return mid
        elif  input_array[mid]<value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print "Iterative version"
print binary_search_iterative(test_list, test_val1)
print binary_search_iterative(test_list, test_val2)
print "recursive"
print binary_search_recursive(test_list, test_val1)
print binary_search_recursive(test_list, test_val2)
