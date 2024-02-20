class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_pref = [0]
        n_pref = [0]
        res = []


        for i in customers:
            if i == "Y":
                y_pref.append(1)
            else:
                y_pref.append(0)

        for i in customers:
            if i == "N":
                n_pref.append(1)
            else:
                n_pref.append(0)

        
        for i in range(1, len(y_pref)):
            y_pref[i] += y_pref[i-1]

        for i in range(1, len(n_pref)):
            n_pref[i] += n_pref[i-1]
        
        for i in range(len(y_pref)):
            penalty = (y_pref[-1] - y_pref[i]) + n_pref[i]
            res.append(penalty)
        
        return res.index(min(res))
        


        