class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = [i for i in str(num)]
        digits2 = digits.copy()
        count = 0
        for i in digits2:
            if i == '0':
                digits.remove('0')
                count+=1
            elif i == '-':
                digits.remove(i)
        if num >= 0:
            digits.sort()
            while count > 0:
                digits.insert(1,'0')
                count-=1
        else:
            digits.sort(reverse = True)
            digits.insert(0, '-')
            while count > 0:
                digits.append('0')
                count-=1
        re_str = ''.join(digits)
        re_num = int(re_str)
        # print(rearranged)
        return re_num
        