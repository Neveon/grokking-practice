"""
Problem Statement
Given a string, find the length of the longest substring in it with no more than K distinct characters.

----------
Example 1:
----------
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

----------
Example 2:
----------
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

----------
Example 3:
----------
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

# Time Complexity O(N)
# Space Complexity O(K) since the hash map stores up to K characters
def longest_substring_with_K_distinct_chars(string, k):
    char_frequency = dict()
    window_start = 0
    longest_substring = 0

    for window_end in range(len(string)):
        right_char = string[window_end]
        # If char does not exist in dict, init it in char_frequency with 0 count
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        # For each char we find, add to frequency counter
        char_frequency[right_char] += 1

        # If we have >k distinct chars, shrink the window until we are left with 'k' distinct characters
        while len(char_frequency) > k:
            left_char = string[window_start]
            char_frequency[left_char] -= 1
            # Delete from dict if there are no more characters found in the window
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1 # shrink the window
        # Check for longest substring
        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring
