class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        time = []
        x=0
        for i in range(len(processorTime)):
            time.append(max(list(map(add,[processorTime[i]]*4,tasks[x:x+5] ))))
            x+=4
        return max(time)


        