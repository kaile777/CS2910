

def merge_sort(list, comparator):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        merge_sort(left_half, comparator)
        merge_sort(right_half, comparator)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if comparator(left_half[i]) < comparator(right_half[j]):
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1

    return list

