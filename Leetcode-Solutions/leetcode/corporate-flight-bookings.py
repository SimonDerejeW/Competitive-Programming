class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n+1)

        for i,j,k in bookings:
            answer[i-1] += k
            answer[j] -= k
        
        for i in range(1,len(answer)):
            answer[i] += answer[i-1]
        answer.pop()
        return answer
