class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {"2":["a" , "b" , "c"],
                "3": ["d" , "e" , "f"],
                "4": ["g" , "h", "i"],
                "5": ["j" , "k" , "l"],
                "6": ["m", "n", "o"], 
                "7": ["p", "q" , "r", "s"],
                "8": ["t" , "u" , "v"],
                "9": ["w" , "x" , "y", "z"]}
        
        res = []
        
        if len(digits) == 0:
            return []

        def backtrack(combs , i):
            if len(combs) == len(digits):
                res.append("".join(combs[:]))
                return
            
            for letter in mapp[digits[i]]:
                combs.append(letter)
                backtrack(combs , i + 1)
                combs.pop()
        
        backtrack([] , 0)
        return res
