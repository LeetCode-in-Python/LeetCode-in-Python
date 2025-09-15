# #Medium #Bit_Manipulation #Algorithm_II_Day_19_Bit_Manipulation
# #Top_Interview_150_Bit_Manipulation #2025_09_14_Time_1_ms_(82.83%)_Space_18.01_MB_(19.55%)

class Solution:
    def __init__(self):
        # Precomputed masks for different bit positions
        self.masks = [
            0,
            0x80000000,
            0xC0000000,
            0xE0000000,
            0xF0000000,
            0xF8000000,
            0xFC000000,
            0xFE000000,
            0xFF000000,
            0xFF800000,
            0xFFC00000,
            0xFFE00000,
            0xFFF00000,
            0xFFF80000,
            0xFFFC0000,
            0xFFFE0000,
            0xFFFF0000,
            0xFFFF8000,
            0xFFFFC000,
            0xFFFFE000,
            0xFFFFF000,
            0xFFFFF800,
            0xFFFFFC00,
            0xFFFFFE00,
            0xFFFFFF00,
            0xFFFFFF80,
            0xFFFFFFC0,
            0xFFFFFFE0,
            0xFFFFFFF0,
            0xFFFFFFF8,
            0xFFFFFFFC,
            0xFFFFFFFE
        ]

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        return right & self.masks[self._numberOfLeadingZeros(left ^ right)]

    def _numberOfLeadingZeros(self, n: int) -> int:
        """Count leading zeros in 32-bit integer"""
        if n == 0:
            return 32
        count = 0
        if n < 0:
            return 0
        while n > 0:
            n = n >> 1
            count += 1
        return 32 - count

