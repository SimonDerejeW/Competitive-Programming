class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_names = []
        dictionary = dict(zip(heights, names))
        sorted_dictionary = dict(sorted(dictionary.items()))
        for values in sorted_dictionary.values():
            sorted_names.append(values)
        sorted_names.reverse()
        return sorted_names

