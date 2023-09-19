"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""

"""Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]"""

strs = ["eat","tea","tan","ate","nat","bat"]

dic = {}

for i in range(len(strs)):

    x = "".join(sorted(strs[i]))

    if x not in dic:
        dic[x] = [strs[i]]             
    else:
        dic[x].append(strs[i])

  print(list(dic.values()))
