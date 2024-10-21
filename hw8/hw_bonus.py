"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:
    # write your code here
    num_set = set(my_list)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            cur_num = num
            cur_streak = 1
            while cur_num + 1 in num_set:
                cur_num += 1
                cur_streak += 1
            longest = max(longest, cur_streak)    
    return longest

"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    # write your code here
    for i in range(0, len(my_list)):
        if my_list[i] > 1:
            if my_list[i] - 1 != my_list[i-1]:
                return my_list[i] - 1
    return None

"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    # write your code here
    from collections import Counter
    return Counter(my_list).most_common(1)[0][0]

"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    # write your code here
    from collections import defaultdict
    anagram_map = defaultdict(list)
    for word in words:
        anagram_map[''.join(sorted(word))].append(word)
    return list(anagram_map.values())
