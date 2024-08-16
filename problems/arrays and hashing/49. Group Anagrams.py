# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/
# difficulty: medium

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}
        for word in strs:
            anagram_key = "".join(sorted(word))
            if anagram_key in anagram_map:
                anagram_map[anagram_key].append(word)
            else:
                 anagram_map[anagram_key] = [word]
        
        return [anagram_map[key] for key in anagram_map]

        # solution 2
        # anagram_map = {}
        # for word in strs:
        #     char_count = [0 for i in range(26)]
        #     for char in word:
        #         char_count[ord(char) - ord('a')] += 1
        #     tuple_count = tuple(char_count)
        #     if tuple_count in anagram_map:
        #         anagram_map[tuple_count].append(word)
        #     else:
        #         anagram_map[tuple_count] = [word]
        # return [anagram_map[tuple_count] for tuple_count in anagram_map]