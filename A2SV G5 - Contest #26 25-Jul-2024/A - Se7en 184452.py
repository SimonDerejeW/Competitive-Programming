# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

for _ in range(int(input())):
    n = int(input())
    s = str(n)
    if n % 7 == 0:
        print(n)
    else:
        s = list(s)
        s[-1] = "0"
        x = int("".join(s))
        for i in range(x, x+11):
            if i % 7 == 0:
                print(i)
                break