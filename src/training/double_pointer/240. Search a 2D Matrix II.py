'''
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例 1：

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
示例 2：

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109
'''
class Solution:

    def searchMatrix(self, matrix, target: int) -> bool:#二分查找
        if not matrix or not matrix[0]:return False
        def binary_search(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return False
        m,n = len(matrix),len(matrix[0])
        # nums = [-1]*(m*n)
        # for i in range(m):
        #     for j in range(n):
        #         nums[i*n+j]=matrix[i][j]
        # print(nums)
        # return False
        # 时间复杂度O(m * logn)
        for i in range(m):
            
            if target == matrix[i][0] or target == matrix[i][-1]:
                return True
            elif matrix[i][0]<target<matrix[i][-1] and binary_search(matrix[i], target):
                return True
        return False

    def searchMatrix2(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:return False
        m,n = len(matrix),len(matrix[0])
        i,j=0,n-1
        #时间复杂度O(m+n)
        while i < m and j >=0:
            if matrix[i][j]< target:
                i+=1
            elif matrix[i][j] > target:
                j-=1
            else:
                return True
        return False
            




if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print('1', s.searchMatrix(matrix, target))
    print('2', s.searchMatrix2(matrix, target))
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 20
    print('1', s.searchMatrix(matrix, target))
    print('2', s.searchMatrix2(matrix, target))
