class Solution:
    def largestAltitude(self, gain):
        gain.insert(0, 0)
        print(gain)
        for i in range(1, len(gain)):
            gain[i] = gain[i]+gain[i-1]
        print(max(gain))


if __name__ == '__main__':
    s = Solution()
    gain = [-4, -3, -2, -1, 4, 3, 2]

    s.largestAltitude(gain)
