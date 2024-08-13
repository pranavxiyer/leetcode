# 3096. Minimum Levels to Gain More Points
# https://leetcode.com/problems/minimum-levels-to-gain-more-points/description/
# difficulty: medium

class Solution(object):
    def minimumLevels(self, possible):
        """
        :type possible: List[int]
        :rtype: int
        """
        prefix = []
        total = 0
        for i in range(len(possible)):
            if possible[i] == 0:
                val = -1
            else:
                val = 1
            total += val
            prefix.append(total)
        
        for i in range(len(prefix) - 1):
            alice = prefix[i]
            bob = prefix[len(prefix) - 1] - alice
            if alice > bob:
                return i + 1
        return -1