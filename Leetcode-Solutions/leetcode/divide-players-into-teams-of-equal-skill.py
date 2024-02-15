class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        chem = 0
        checker = skill[l] + skill[r]
        while l < r:
            if checker == skill[l] + skill[r]:
                chem += (skill[l]) * (skill[r])
                l+=1
                r-=1
            else:
                return -1
        return chem