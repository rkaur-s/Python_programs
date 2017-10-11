
def find_duplicates(l):
	'''sorted the list and checked if the next element is same '''
	sorted_l = sorted(l)
	dup = []
	for i in range(len(sorted_l)-1):
		if sorted_l[i] not in dup:
			if sorted_l[i] == sorted_l[i+1]:
				dup.append(sorted_l[i])

	return dup

def find_duplicates_1(l):
	from collections import Counter
	
	new_l = Counter(l)
	return [key for key, val in new_l.items() if val > 1 ]


l = [1,2,3,4,1,2,2,2,2]
print(find_duplicates_1(l))