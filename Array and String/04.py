class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        flowerbed.append(1)
        ret = 0
        num = 0
        for flower in flowerbed:
            if flower == 0:
                num = num + 1
            else:
                ret = ret + (num - 1) // 2
                num = 0

        return ret >= n


sol = Solution()
print(sol.canPlaceFlowers([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 1))
