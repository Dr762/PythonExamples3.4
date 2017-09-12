def quicksort(array):
    pivot = array[-1]
    less = []
    greater = []
    equal = []

    if (len(array)>1):
        for i in array:
            if i<pivot:
                less.append(i)
            if i==pivot:
                equal.append(i)
            if i>pivot:
                greater.append(i)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
