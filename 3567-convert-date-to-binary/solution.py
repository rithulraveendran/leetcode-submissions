class Solution:
    def convertDateToBinary(self, date: str) -> str:
        parts = date.split('-')
        binary_parts = [bin(int(x))[2:] for x in parts]
        return "-".join(binary_parts)

