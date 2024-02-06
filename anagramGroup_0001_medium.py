from collections import defaultdict
import collections
import typing

'''
Ques. Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''
# 79 MS RUNTIME
# by me
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        ans = []
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in map:
                ans[map[sorted_str]].append(i)
            else:
                map[sorted_str] = len(ans)
                ans.append([i])
        
        return ans

# learn by other soluntions
# 70 MS RUNTIME
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for word in strs:
          sorted_word = "".join(sorted(word))
          a[sorted_word].append(word)
        return list(a.values())    
        
# 76 MS RUNTIME
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dict = collections.defaultdict(list)

    for str in strs:
      key = ''.join(sorted(str))
      dict[key].append(str)

    return dict.values()
