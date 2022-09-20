'''
Find the longest substring with the non-repeating characters.
Input: abcabcdbb
Output: abcd

'''

class String_Of_Chars:
    def __init__(self,string_to_eval):
        self.string_to_eval = string_to_eval
    
    @property
    def longestSubstring(self):
        #dictionary of substrings + its index, key = letter, value = index, SEEN LETTERS
        sub_index = {}

        #most receent substring
        tmp_str = ''

        #first index of last unique substring
        ndx_start = 0
        
        #longest
        longest_str = ''
        for ndx,letter in enumerate(self.string_to_eval):
            
            if letter in sub_index and sub_index[letter] >= ndx_start:
                ndx_start = sub_index[letter] + 1
                tmp_str = self.string_to_eval[ndx_start:ndx + 1]
                sub_index[letter] = ndx
            else:
                tmp_str = tmp_str + letter
                sub_index[letter] = ndx

            if len(tmp_str) > len(longest_str):
                longest_str = tmp_str            
        return longest_str

print(String_Of_Chars(string_to_eval='abcabcdbb').longestSubstring)
