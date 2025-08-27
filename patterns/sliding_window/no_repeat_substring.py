"""
HARD

-----------------
Problem Statement
-----------------
Given a string, find the length of the longest substring which has no repeating characters.

-----------------
Example 1:
-----------------
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

-----------------
Example 2:
-----------------
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

-----------------
Example 3:
-----------------
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""

def no_repeat_substring(string):
    window_start = 0
    chars = set()
    max_length = 0

    # Expand window
    for window_end in range(len(string)):
        right_char = string[window_end]
        # If we find this char already in the set, we need to shrink the window
        while right_char in chars:
            left_char = string[window_start]
            if left_char in chars:
                chars.remove(left_char)
            # Shrink window
            window_start += 1
        chars.add(right_char)

        # Verify newest max length
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

# Time Complexity O(N)
# Space Complexity O(K) where K is the number of distinct characters in the string.
# But if we have a limited amount of characters (26 letters in english) then we can argue we have O(1) space
