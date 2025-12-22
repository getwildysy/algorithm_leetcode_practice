class Solution:
    def findDifference(self, nums1, nums2):

        hash_nums1, hash_nums2 = {},  {}
        answer1, answer2 = [], []
        # 建 hash map，用nums的值當作字典的鍵，字典的值為True,(或是任何東西都可以，不會用到)
        hash_nums1 = {val: True for val in nums1}
        hash_nums2 = {val: True for val in nums2}

        for key in nums1:
            if key not in hash_nums2:
                answer1.append(key)
        for key in nums2:
            if key not in hash_nums1:
                answer2.append(key)

        print([answer1, answer2])


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    s.findDifference(nums1, nums2)
