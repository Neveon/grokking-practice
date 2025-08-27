"""
HARD

Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

-----------
Example 1:
-----------
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

-----------
Example 2:
-----------
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""

"""
Walk through of algorithm

1. Track character frequency of the pattern in a HashMap by traversing pattern and adding count of chars to a dict
2. As window expands, if the character is found in the HashMap decrement the count of the character. If count is 0, we have a match of a character.
3. If the window size (window_end - window_start + 1) > len(pattern) increment the window_start. Increment any character found in HashMap and decrement match.
4. If match == len(pattern) then record the window_start index in anagram_indices
"""

def string_anagrams(string, pattern):
    window_start = 0
    char_freq = dict()
    matched = 0
    anagram_indices = []

    # Step 1 - build character frequency HashMap of the pattern
    for c in pattern:
        if c not in char_freq:
            char_freq[c] = 0
        char_freq[c] += 1

    # Step 2 - Expand window, decrement char freq if character found, add to match if char_freq[right_char] == 0
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        # Step 3 - Shrink window if the size of the window is too large for the pattern
        if window_end - window_start + 1 > len(pattern):
            left_char = string[window_start]
            # Check if left char is part of the pattern and increment char_freq
            if left_char in char_freq:
                # If char_freq was a match previously, then we have to decrement it as we shrink the window to remove this character
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1
            # shrink window
            window_start += 1
                
        # Step 4
        if matched == len(pattern):
            anagram_indices.append(window_start)

    return anagram_indices

# Time Complexity O(N + M) traverse the string and build the pattern HashMap, respectively
# Space Complexity O(M) worse case the pattern could have all distinct characters, 
#   it could also be O(N) in the case the pattern is one character and equals the one character pattern
