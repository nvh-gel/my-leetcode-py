class Solution:
    def duplicateZeros(self, arr) -> None:
        length = len(arr)
        arr_copy = []
        for item in arr:
            if item == 0:
                arr_copy.extend([0,0])
            else:
                arr_copy.extend([item])
        arr.clear()
        arr.extend(arr_copy[0:length])



solution = Solution()

input = [1,0,2,3,0,4,5,0]
solution.duplicateZeros(input)
print(input)

input = [1,2,3]
solution.duplicateZeros(input)
print(input)
