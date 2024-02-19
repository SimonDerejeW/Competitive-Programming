class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(image[0]) for _ in range(len(image))]
        n = len(image)
        for row in range(len(image)):
            for col in range(len(image) - 1, -1, -1):
                if image[row][col] == 0:
                    res[row][n - col - 1] = 1
                else:
                    res[row][n - col - 1] = 0
        return res