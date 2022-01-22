Is valid Anagram:


Algorithm
Make counter for each string
Check all the counts are same
compare len(s_count) and len(t_count) and iterate only in s_count
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        
        if(len(s_count) != len(t_count)):
            return False
        
        for letter in s_count:
            if letter not in t_count:
                return False
            elif s_count[letter] != t_count[letter]:
                return False
            
        return True
        
        
        or

def validAnagram(word1, word2):
	return sorted(word1) == sorted(word2)
  
    or
    
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
######################3
Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

rom collections import defaultdict, Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
		 
        """
        l = 0 
        rtn = [] 
        original_ht = Counter(list(p))
        curr_ht = defaultdict(int)
        for r in range(len(s)): 
            curr_ht[s[r]] += 1
            while l < r and r - l + 1 > len(p): 
                curr_ht[s[l]] -= 1
                if curr_ht[s[l]] == 0:
                    # need to make sure the 0 values are being deleted 
                    del curr_ht[s[l]]
                l += 1 
            # hash-table comparision compares the values so this is valid 
            if curr_ht == original_ht: 
                rtn.append(l) 
        
        return rtn 





    
