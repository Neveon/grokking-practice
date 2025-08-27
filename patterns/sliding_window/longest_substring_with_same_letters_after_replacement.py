"""
HARD

-----------------
Problem Statement
-----------------
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
find the length of the longest substring having the same letters after replacement.

-----------------
Example 1:
-----------------
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

-----------------
Example 2:
-----------------
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
-----------------
Example 3:
-----------------
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

def longest_substring_with_same_letters_after_replacement(string, k):
    window_start = 0
    max_length = 0
    char_freq = dict()
    max_repeating_char_count = 0
    
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        # Check if newest character in window has the highest freq count
        max_repeating_char_count = max(max_repeating_char_count, char_freq[right_char])

        # Size of window - max_repeating_char_count = 0 if all characters are the same
        # If not all characters are the same, then the result is the count of different characters
        # if size of window - max_repeating_char_count > k then we MUST shrink the window
        if window_end - window_start + 1 - max_repeating_char_count > k:
            left_char = string[window_start]
            char_freq[left_char] -= 1
            window_start += 1


        max_length = max(max_length, window_end - window_start + 1)

    return max_length

# Time Complexity O(N)
# Space Complexity O(26) => O(1) in the case we only have lowercase english alphabet as input
