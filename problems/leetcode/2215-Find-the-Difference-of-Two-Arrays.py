class Solution:
    def findDifference(self, nums1, nums2):

        # 將列表轉為集合，自動去重，且查詢時間複雜度為 O(1)
        set1 = set(nums1)
        set2 = set(nums2)

        # 使用集合運算的「差集」
        ans1 = list(set1 - set2)
        ans2 = list(set2 - set1)

        return [ans1, ans2]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    s.findDifference(nums1, nums2)
