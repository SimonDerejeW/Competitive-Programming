class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # return [0] * len(deck)
        # deck.sort()
        # new_deck = [0] * len(deck)
        # zero = len(deck)
        
        # i = 0
        # while i < len(new_deck):
        #     if i % 2 == 0:
        #         new_deck[i] = deck[i//2]
        #         zero -= 1
        #     i += 1
        # print(i)
        # return new_deck
        deck.sort(reverse=True)

        new_deck = deque()
        new_deck.append(deck[0])
        for i in range(1, len(deck)):
            new_deck.appendleft(new_deck.pop())
            new_deck.appendleft(deck[i])
        
        return new_deck



        

            
