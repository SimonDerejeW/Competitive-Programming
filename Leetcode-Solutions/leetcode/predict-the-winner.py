class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def minimax(left , right, turn, score):

            if left == right:
                if turn:
                    score += nums[left]
                    return score >= 0
                else:
                    score -= nums[left]
                    return score >= 0


            if turn:
                score1 = score + nums[left]
                score2 = score + nums[right]
                return minimax(left+1 , right , False , score1) or minimax(left , right - 1 , False , score2)
            else:
                score1 = score - nums[left]
                score2 = score - nums[right]
                return minimax(left+1 , right , True , score1) and minimax(left , right - 1 , True , score2)
            
        return minimax(0 , len(nums) - 1, True, 0)