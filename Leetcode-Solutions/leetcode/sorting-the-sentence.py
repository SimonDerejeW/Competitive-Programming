class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split()

        sentence.sort(key= lambda x:x[-1])
        for i in range(len(sentence)):
            sentence[i] = sentence[i][:-1]
        return " ".join(sentence)