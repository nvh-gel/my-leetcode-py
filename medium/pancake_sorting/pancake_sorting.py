# Input: [3,2,4,1]
# Output: [4,2,4,3]
# Explanation:
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: A = [3, 2, 4, 1]
# 2 0 1 3
# After 1st flip (k=4): A = [1, 4, 2, 3]
# 0 2 1 1
# After 2nd flip (k=2): A = [4, 1, 2, 3]
# 3 1 1 1
# After 3rd flip (k=4): A = [3, 2, 1, 4]
# 2 0 2 0
# After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.


# [5,1,2,4,3]
# 4 1 1 1 1
# [3,4,2,1,5]
# 2 2 0 3 0
# [1,2,4,3,5]
# 0 0 1 1 0
# [4,2,1,3,5]
# 3 0 2 1 0
# [3,1,2,4,5]
# 2 1 1 0 0
# [2,1,3,4,5]
# 1 1 0 0 0
# [1,2,3,4,5]

class Solution:
    def pancakeSort(self, A: list) -> list:
        ans = []

        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        print(B)
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1

        return ans


# class Solution:
#     def pancakeSort(self, A: list) -> list:
#         a_sorted = sorted(A)
#         length = len(A)
#         flips = []
#         while a_sorted != A and len(flips) < 10:
#             heuristics = {}
#             flippable = {}
#             flip = 0
#             print('start = ' + str(A))
#             for i in range(2, length + 1):
#                 temp = self.flip(A, i)
#                 # print('temp = ' + str(temp))
#                 h = self.calculate_heuristic(temp)
#                 heuristics[i] = h
#                 flippable[i] = temp
#             print('h = ' + str(heuristics))\

#             while flip == 0 or (len(flips) > 0 and flips[len(flips) - 1] == flip):
#                 flip = min(heuristics, key=heuristics.get)
#                 del heuristics[flip]

#             print('flip = ' + str(flip))
#             A = flippable[flip]
#             flips.append(flip)
#             print('A =' + str(A))
#             print('')

#         return flips

#     def flip(self, A: list, k: int) -> list:
#         to_flip = A[0 : k]
#         to_flip.reverse()
#         to_flip.extend(A[k : len(A)])
#         return to_flip

#     def calculate_heuristic(self, A: list) -> int:
#         heuristic = 0
#         for val in A:
#             heuristic += abs(val - A.index(val) - 1)
#         return heuristic

solution = Solution()


# input = [3,2,4,1]
# output = solution.pancakeSort(input)
# print(output)


input = [1,2,4,3]
output = solution.pancakeSort(input)
print(output)

# input = [1,2,3]
# output = solution.pancakeSort(input)
# print(output)
