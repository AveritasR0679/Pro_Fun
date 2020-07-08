from typing import *
def add(s):
    result = ''
    for i in range(len(s)):
        if i != len(s) - 1:
            result += s[i] + '_'
    return result

def all_fluffy(s):
    string = 'fluffy'
    for i in s:
        if i not in string:
            return False
    return True

def count_uppercase(s):
    num = 0
    for i in s:
        if i.upper():
            num += 1
    return num

def find_letter_n_times(s, letter, n):
    i = 0
    count = 0
    while count != n and i < len(s):
        if s[i] == letter:
            count += 1
        i += 1
    return s[:i]

def count_collatz_steps(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    return count

def count_not_num(s):
    i = 0
    while i < len(s) and s[i] not in '0123456789':
        i += 1
    return i

def collect_underperformers(nums, threshold):
    new = []
    for i in range(len(nums)):
        if nums[i] < threshold:
            new.append(nums[i])
    return new

def greatest_diff(nums1, nums2):
    diff = []
    for i in range(len(nums1)):
        diff.append(abs(nums1[i] - nums2[i]))
    return max(diff)

# callable
def compare_nums(n1: int, n2: int,
                 comp: Callable[[int, int], bool]) -> int:
    if comp(n1, n2):
        return n1
    else:
        return n2

def is_twice_as_big(n1: Union[int, float], n2: Union[int, float]) -> bool:
    return n1 >= 2* n2

if __name__ == '__main__':
    compare_nums(10, 3, is_twice_as_big)
    compare_nums(10,6, is_twice_as_big)

if __name__ == '__main__':
    nested_list = []
    input_file = ["hello", "blah"]
    for line in input_file:
        line_list = [] 
        for char in line: 
            line_list.append(char) 
        nested_list.append(line_list)

def contains_items(L,s):
	for item in L:
		if item == s:
			return True
		else:
			return False

import func_gcd as fg
print(fg.gcd(100,20))
