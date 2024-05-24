# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.is_end = []
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
                curr.is_end = word
            
            @staticmethod
            def build_trie(words):
                trie = Trie()
                for word in words:
                    trie.insert(word)
                
                return trie
        
        trie = Trie.build_trie(words)
        possible = []
        def dfs(curr , count):
            for key in curr.children:
                node = curr.children[key]
                if len(node.is_end) > 0 and count == len(node.is_end)-1:
                    possible.append(node.is_end)
                    dfs(node, count + 1)
                elif len(node.is_end) > 0:
                    dfs(node, count + 1)
                else:
                    dfs(node, count)
        dfs(trie.root , 0)
        possible.sort(key = lambda x : (-len(x), x))

        # print(possible)
        return possible[0] if possible else ""









