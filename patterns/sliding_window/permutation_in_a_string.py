"""
HARD

-------------------
Problem Challenge 1
-------------------
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

If a string has ‘n’ distinct characters it will have n! permutations.
-----------------
Example 1:
-----------------
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

-----------------
Example 2:
-----------------
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

-----------------
Example 3:
-----------------
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

-----------------
Example 4:
-----------------
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""

"""
-----------------
SOLUTION
-----------------
This problem follows the Sliding Window pattern and we can use a similar sliding window strategy as discussed in Longest Substring with K Distinct Characters. 
We can use a HashMap to remember the frequencies of all characters in the given pattern. 
Our goal will be to match all the characters from this HashMap with a sliding window in the given string. 

Here are the steps of our algorithm:
1. Create a HashMap to calculate the frequencies of all characters in the pattern.
2. Iterate through the string, adding one character at a time in the sliding window.
3. If the character being added matches a character in the HashMap, decrement its frequency in the map. 
    If the character frequency becomes zero, we got a complete match.
4. If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the HashMap),
    we have gotten our required permutation.
5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the size of the pattern.
    At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.
"""

# The window is expanding until it reaches the len(pattern)
# Then it is stepping through the string
def permutation_in_a_string(string, pattern):
    window_start = 0
    matched = 0
    char_freq = dict()

    for c in pattern:
        if c not in char_freq:
            char_freq[c] = 0
        char_freq[c] += 1

    # our goal is to match all the characters from 'char_freq' with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_freq:
            # decrement the frequency of matched character
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        # Number of characters matched is same as pattern -> return true
        if matched == len(char_freq):
            return True
        
        # shrink the window by one character
        if window_end - window_start + 1 >= len(pattern):
            left_char = string[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

    return False
