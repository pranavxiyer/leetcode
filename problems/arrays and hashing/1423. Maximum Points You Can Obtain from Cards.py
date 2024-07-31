# 1423. Maximum Points You Can Obtain from Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description
# difficulty: medium

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sums = []
        points_sum = 0
        for point in cardPoints:
         points_sum += point
         prefix_sums.append(points_sum)

        def query(sums_array, l, r):
            if l == 0:
             return sums_array[r]
            else:
             return sums_array[r] - sums_array[l - 1]

        max_points = float("-inf")
        for left_cards in range(k + 1):
            right_cards = k - left_cards

            if left_cards == 0:
                left_sum = 0
            else:
                left_sum = query(prefix_sums, 0, left_cards - 1)

            if right_cards == 0:
                right_sum = 0
            else:
                right_sum = query(prefix_sums, len(prefix_sums) - right_cards, len(prefix_sums) - 1)

            max_points = max(max_points, left_sum + right_sum)

        return max_points