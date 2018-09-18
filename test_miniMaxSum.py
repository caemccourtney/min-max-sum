import miniMaxSum

def test_quicksort_sorted_array():
	assert miniMaxSum.quicksort([1,2,3]) == [1,2,3]

def test_quicksort_simple_array():
	assert miniMaxSum.quicksort([3,2,1]) == [1,2,3]

def test_minMaxSum_simple_array():
	assert miniMaxSum.miniMaxSum([1,2,3,4,5]) == (10,14)

