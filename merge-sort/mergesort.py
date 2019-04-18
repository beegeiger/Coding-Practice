"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""



def merge(lst1, lst2):
	merge_out = []
	while len(lst1) > 0 and len(lst2) > 0:
		if len(lst1) == 0:
			merge_out.append(lst2.pop(0))
		elif len(lst2) == 0:
			merge_out.append(lst1.pop(0))
		elif lst1[0] < lst2[0]:
			merge_out.append(lst1.pop(0))
		elif lst2[0] >= lst1[0]:
			merge_out.append(lst2.pop(0))
	# print('Merge out:', merge_out)
	return merge_out

def merge_sort(lst):
	"""Divide and conquer: reduce to lists of 0-1 items, then recombine."""
	if lst == []:
		return

	if len(lst) == 1:
		return lst

	inde = int(len(lst) // 2)
	left = merge_sort(lst[:inde])
	right = merge_sort(lst[inde:])

	return merge(left,right)






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")
