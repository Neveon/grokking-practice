"""
HARD

Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

-----------
Example 1:
-----------
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

-----------
Example 2:
-----------
Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

-----------
Example 3:
-----------
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""

"""
Algorithm Walkthrough

1. Build a char_freq HashMap to keep count of the pattern's characters
2. Expand window. If right_char is in char_freq, decrement the HashMap. If the char_freq[right_char] is 0, increment match count
3. If we have a match == len(pattern), continously decrement the window to find smallest substring. If left_char in char_freq, check if 0 & increase match.
    Then increment it char_freq and increment window_start pointer.
4. If matched == len(pattern) & the window size is smaller than the current output (as long as output is not empty), save as new output

"""

def smallest_window_containing_substring(string, pattern):
    window_start = 0
    matched = 0
    substr_start = 0
    min_substr_length = len(string) + 1
    char_freq = dict()

    # Step 1
    for c in pattern:
        if c not in char_freq:
            char_freq[c] = 0
        char_freq[c] += 1

    # Step 2
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] >= 0: # count every matching char
                matched += 1

        # Step 3
        while matched == len(pattern):
            # Check if current substr is smallest
            if min_substr_length > window_end - window_start + 1:
                min_substr_length = window_end - window_start + 1
                substr_start = window_start

            left_char = string[window_start]
            window_start += 1
            if left_char in char_freq:
                # We could have redundant matching characters, therefore we decrement the
                # matched count only when a useful occurrence of a matched char is going out of the window
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

    if min_substr_length > len(string):
        return ""

    return string[substr_start:substr_start + min_substr_length]

# Time Complexity O(N + M)
#   where N and M are the number of characters in the string and pattern, respectively
# Space Complexity O(M)
#   worst case, whole pattern has distinct characters in the HashMap
#   we also need O(N) space for the substring only if string == permutation of the pattern
