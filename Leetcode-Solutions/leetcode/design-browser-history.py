class ListNode:
    def __init__(self,val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.next = None
        self.prev = None
        self.head = homepage
        self.home = ListNode(self.head)
        self.currPage = self.home

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.currPage.next = new_node
        new_node.prev = self.currPage
        self.currPage = self.currPage.next
        

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.currPage.prev:
            self.currPage = self.currPage.prev
            i+=1
        return self.currPage.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.currPage.next:
            self.currPage = self.currPage.next
            i += 1
        return self.currPage.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)