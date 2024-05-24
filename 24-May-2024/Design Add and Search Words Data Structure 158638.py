# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True


    def search(self, word: str) -> bool:

        def dfs(curr , i):
            if i >= len(word):
                return curr.is_end
            if word[i] != "." and word[i] not in curr.children:
                return False
            if word[i] == ".":
                flag = False
                for key in curr.children:
                    flag = flag or dfs(curr.children[key], i+1)
                return flag
            else:
                return dfs(curr.children[word[i]] , i + 1)
        return dfs(self.root , 0)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)