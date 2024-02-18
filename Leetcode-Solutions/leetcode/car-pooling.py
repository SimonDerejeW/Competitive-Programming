class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[2], reverse=True)
        maxDistance = trips[0][2]
        pref = [0] * (maxDistance + 2)
        

        for k,i,j in trips:
            pref[i] += k
            pref[j] -= k

        for i in range(1,len(pref)):
            pref[i] += pref[i-1]
        
        if max(pref) > capacity:
            return False
        return True


