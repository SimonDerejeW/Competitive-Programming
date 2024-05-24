# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__(self):
                self.is_end = False
                self.children = {}
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str) -> None:  
                curr = self.root
                for char in word:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
                curr.is_end = True

            @staticmethod
            def build_trie(words: List[str]):
                trie = Trie()
                for word in words:
                    trie.insert(word)
                
                return trie
        
        trie = Trie.build_trie(dictionary)
        words = sentence.split()

        def search(word):
            # ans = []
            curr = trie.root
            for i in range(len(word)):
                if word[i] not in curr.children:
                    return word
                curr = curr.children[word[i]]
                if curr.is_end:
                    return word[:i+1]
            return word
        res = []
        for word in words:
            x = search(word)
            res.append(x)

        return " ".join(res)











