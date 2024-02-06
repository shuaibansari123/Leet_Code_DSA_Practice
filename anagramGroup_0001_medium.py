# I am starting this from name of ALLAH
# Bismillahir rahmanir rahim
# allah mujhe himmat,takat,akal,dimag,shifa ata farma or nek amal karne ki or galat amal se bachne ki tahfik ata farma
# me bs koshish kr sakta hu or me sirf tujhse hi ummed rakhta hu or tujhi se mangta or sirf tere aage sir jhukata hu

# AGAIN start DSA from 06-02-2024
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


































# MONOTONIC stack will be use for next/previous item comparision (time-complex : O(n)) : by Fraz
  

# use leet-code everyday like my social media   --->                              IN SHAH ALLAH
# follow watch hindi youtube channel for advance dsa   --> Anuj bhaiya dsa        IN SHAH ALLAH 
# after some time switch english youtube channel       --> Fraz                   IN SHAH ALLAH  
# push everyday on github even little solution                                    IN SHAH ALLAH
# after sometime try to contribute in Open-Source (start from easyToGo issues)    IN SHAH ALLAH                      
# build network/community by github, leet-code, LinkedIn                          IN SHAH ALLAH  
  
# in my third year of bcs i have good in dsa so go to Development with project              IN SHAH ALLAH                   
# (React.js, FastApi, Express.js, Postgres, Go lang(grpc), Java(springboot), Cloud, Nginx)  IN SHAH ALLAH                          
# after stable FullStack(pro in backend) dev designation. become pro APP DEV after this follow my passion          IN SHAH ALLAH                            
# on IoT, ML, AI, BlockChain                                                                IN SHAH ALLAH

# bca 2 year dsa, Reactjs(Next.js), Fastapi(GraphQL), Express.js WHILE doing current job    IN SHAH ALLAH                   
# bca 3 year as FullStack dev IN SHAH ALLAH                                                 IN SHAH ALLAH
  
## AAMEEN
# git init
# git remote add origin https://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@github.com/shuaibansari123/Leet_Code_DSA_Practice.git
# git remote set-url origin https://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@github.com/shuaibansari123/Leet_Code_DSA_Practice.git
# git push -u origin main
  






# I am starting this from name of ALLAH
# Bismillahir rahmanir rahim
# allah mujhe himmat,takat,akal,dimag,shifa ata farma or nek amal karne ki or galat amal se bachne ki tahfik ata farma
# me bs koshish kr sakta hu or me sirf tujhse hi ummed rakhta hu or tujhi se mangta or sirf tere aage sir jhukata